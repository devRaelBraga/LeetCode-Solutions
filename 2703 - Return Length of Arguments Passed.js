/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {

    // 43ms beats 93.72%
    return(args.length)
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
