class Solution:
    def climbStairs(self, n: int) -> int:

        # 31ms beats 87.33%
        values = [-1] * (n +3)
        values[0], values[1], values[2] = 0, 1, 2

        def solve(n, values):
            
            if(values[n] != -1):
                return values[n]

            values[n] = solve(n-1, values) + solve(n-2, values)
            return values[n]

        return solve(n, values)



        
