ccclc

%% prepare data
d = RSnGm_combine_sessions; 
id = (d.trialResult == 1 | d.trialResult == 1.5) & d.totalBeats == 1; 
ts = d.beatLenAll(id); 
tp = d.tpVecAll(2, id);
tp = RSnGm_rm_outliers_alex(ts, tp); % remove outliers (replaces with NaNs)
%now remove NaNs
tp_temp = tp; 
tp(isnan(tp_temp)) = []; 
ts(isnan(tp_temp)) = []; 

%% find wm, wp
%fminsearch for wm
if 1
opts = optimset('fminsearch');
opts.Display = 'final';

ints = 0.5:0.1:1.5; %integration limits 
w_init = [0.5, 0.5, 0];
w_opt = fminsearch(@(w) NegLogLike(ts, tp, w, ints), w_init, opts);
disp(w_opt)
save('w_opt.mat', 'w_opt');
else 
    load w_opt.mat   
end 
%% generative model for tp

wm_opt = w_opt(1); wp_opt = w_opt(2); 
ts_gen = ts; 
tm = normrnd(ts, wm_opt); 
te = fbls(ts, tm, wm_opt); 
tp_gen = normrnd(te, wp_opt); 

for idx = 1:numel(d.tsVals)
    tp_mean(idx) = nanmean(tp(ts == d.tsVals(idx)));
    tp_mean_gen(idx) = nanmean(tp_gen(ts_gen == d.tsVals(idx)));
end

figure; hold on; 
plot(ts_gen, tp_gen, 'k.', 'MarkerSize', 1); 
h1 = plot(d.tsVals, tp_mean_gen, 'b*');
h2 = plot(d.tsVals, tp_mean, 'r*');
plot((0.2:0.1:1.8),(0.2:0.1:1.8),'k--');
legend([h1, h2], {'model', 'tp'})



%% functions 

%%%fit params
function out = NegLogLike(ts_exp, tp_exp, params, ints)

wm = params(1); wp = params(2); offset = params(3);
out = -sum(log(Ptp(tp_exp-offset, ts_exp, wm, wp, ints)));
if wm < 0 || wp <0
    out = out +1000;
end


end

%%%%%%%% Low-level functions: calculating probabilities

function p = Ptp(tp, ts, wm, wp, ints)
% Calculate p(tp|ts,wm,wp)
lower = 0;
upper = max(ints)*2;
fun = @(x) Ptpte(fbls(ts, x, wm), tp, wp).*Ptmts(ts, x, wm);
p = integral(fun, lower, upper, 'ArrayValued', true);
end

function te = fbls(ts, tm, wm)

numer = integral(@(ts)ts.*Ptmts(ts, tm, wm), min(ts), max(ts), 'ArrayValued', true);
denom = integral(@(ts)Ptmts(ts, tm, wm), min(ts), max(ts), 'ArrayValued', true);
te = numer./denom;

end

function p = Ptmts(ts, tm, wm)
% Calculate p(tm|ts,wm)
x = (ts-tm).^2;
wmts2 = (wm*ts).^2;
p = 1./sqrt(2*pi*wmts2).*exp(-0.5*x./wmts2);

end

function p = Ptpte(te, tp, wp)
% Calculate p(tp|te,wp)
x = (te-(tp)).^2;
wpte2 = (wp*te).^2;
p = 1./sqrt(2*pi*wpte2).*exp(-0.5*x./wpte2);

end