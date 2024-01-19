/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {

    # 47ms beats 80.69%

    let dp = Array(n + 3)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    function solve(n, dp) {
        if(dp[n] != undefined) {
            return dp[n]
        }

        dp[n] = solve(n - 1, dp) + solve(n - 2, dp)

        return dp[n]
    }

    return solve(n, dp)

};

climbStairs(5)
