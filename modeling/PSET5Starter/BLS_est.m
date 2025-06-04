function te = BLS_est( ts, tm, sigma)
% Computes te by means of the BLS. Which is equivalent to the mean of the
% posterior distribution.

% inputs
% ts: column vector
% tm: column vector 
% sigma standard deviation of likelihood

numer = integral(@(ts)ts.*Ptmts(ts, tm, sigma), min(ts), max(ts), 'ArrayValued', true);
denom = integral(@(ts)Ptmts(ts, tm, sigma), min(ts), max(ts), 'ArrayValued', true);
te = numer./denom;

% Output:
% te: column vector


end