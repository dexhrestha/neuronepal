function rnorm(mean, stdDev) {
    let u1 = Math.random();
    let u2 = Math.random();
    let z0 = Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);
    return z0 * stdDev + mean;
}

function change(param){
    return param
}

function exponentialRandom(lambda) {
    return -Math.log(1 - Math.random()) / lambda;
}

// Function to get inter-trial interval between 500ms and 1500ms
function sampleDelay(minDelay=500,maxDelay=1500) {
    const meanDelay = (maxDelay - minDelay) / 2; // mean of the desired range

    // Compute lambda for the exponential distribution
    const lambda = 1 / meanDelay;

    // Get a sample from the exponential distribution
    let interval = exponentialRandom(lambda);

    // Scale and shift the interval to fit within the desired range
    interval = interval * (maxDelay - minDelay) + minDelay;

    // Ensure the interval is within the bounds
    interval = Math.max(minDelay, Math.min(interval, maxDelay));

    return interval;
}


function correlationScore(x,y){
    return Math.round(Math.random());
}

export {rnorm,sampleDelay,change};
