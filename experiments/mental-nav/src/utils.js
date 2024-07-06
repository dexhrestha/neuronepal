

function rearrangeArray(array, index=0) {
    // Ensure the index is within bounds
    if (index < 0 || index >= array.length) {
        throw new Error("Index out of bounds");
    }

    // Split and concatenate the array parts
    const part1 = array.slice(index); // From the index to the end
    const part2 = array.slice(0, index); // From the start to one before the index

    return [...part1, ...part2]; // Combine the two parts
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


export {rearrangeArray,sampleDelay}
