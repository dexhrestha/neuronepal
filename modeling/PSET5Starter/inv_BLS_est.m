function tm = inv_BLS_est(ts,tm0, te, sigma)
% Finds the tm that generates the te closest to the observed value. It does
% so by empirically inverting the BLS function
% 
%  inputs
% ts: column vector
% tm0: column vector 
% sigma standard deviation of likelihood
% te: column vector

tehat = BLS_est(ts, tm0, sigma); 

this = abs(tehat - te');
[thismin, idxmin] = min(this, [], 1);

tm = tm0(idxmin);

% 
% Output:
% tm: column vector

end
