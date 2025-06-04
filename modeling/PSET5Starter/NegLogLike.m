function NeglogLike = NegLogLike(ts, tm0, te, sigma)
% compute neg log likelihood
% Prior: proir distribution
% ts: ts per trial
% tm0: range of tm to invert BLS
% te: observed te
% wm: variance of likelihood
% scalar: switch for Weber fraction

% Find best tm from inverting BLS
% tm = inv_BLS_est(ts, tm0, te, wm, sigma);
tm = inv_BLS_est(ts, tm0, te, wm, sigma);
% Compute Likelihood
% p = Ptmts(ts, tm, wm, sigma);
p = Ptmts(ts, tm, wm, sigma);
% Take negative log
NeglogLike = -sum(log(p));
end
