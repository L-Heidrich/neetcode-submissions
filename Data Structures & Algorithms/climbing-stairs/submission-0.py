class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1}

        def caclulate_steps(steps):
            if steps in memo:
                return memo[steps] 
            
            minn = float("inf")
            total = 0
            for i in [1,2]:
                diff = steps - i
                if diff < 0:
                    break 
        
                total += caclulate_steps(diff)   # was: min(minn, 1 + ...)

            memo[steps] = total
            return total

        solution = caclulate_steps(n)
        return solution
        
        