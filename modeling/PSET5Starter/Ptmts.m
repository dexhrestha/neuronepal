function p = Ptmts(ts, tm, sigma)
% Computes Likelihood function
%
%Inputs:
% ts: ts values
% tm: tm values
% sigma: standard deviation of likelihood
% 

p = 1/(sqrt(2*pi)*sigma)*exp(-(tm-ts).^2/(2*sigma^2));

% Outputs
% p: column vector with likelihood values

end