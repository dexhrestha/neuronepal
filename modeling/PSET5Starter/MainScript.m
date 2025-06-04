clear all; close all; clc
% Load data
load('short_prior.mat');
ts_short = ts;
te_short = te;

clearvars te ts;
% Set range of tm's to invert BLS estimate
tm0 = (0:0.5:2000)';

% Options for fminsearch
opts = optimset('fminsearch');
opts.Display = 'final';

% Initialize sigma
sigma_init = 200;

sigma_short = fminsearch(@(s) NegLogLike(ts_short, tm0, te_short, s), sigma_init, opts);

% Load data
load('long_prior.mat');
ts_long = ts;
te_long = te;

clearvars te ts;
% Set range of tm's to invert BLS estimate
tm0 = (0:0.5:2000)';

% Options for fminsearch
opts = optimset('fminsearch');
opts.Display = 'final';

% Initialize sigma
sigma_init = 200;

sigma_long = fminsearch(@(s) NegLogLike(ts_long, tm0, te_long, s), sigma_init, opts);

