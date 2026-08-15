class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        memo = {0:0}

        def calculate_min_coins(amt):
            if amt in memo: 
                return memo[amt]
            else: 
                minn = float('inf')
                for c in coins: 
                    diff = amt - c
                    if diff < 0: # coin too big, break. coins are sorted. if say, first entry is negative already, the diff is only getting more and more negative 
                        break 
                    minn = min(minn, 1 + calculate_min_coins(diff)) # 1+ .. since we definetlky using one coin 'c' in this loop. calculate_min_coins establishes the recursion relationship and returns how many coins ar eneeded for the diff.

            memo[amt] = minn
            return minn

        result = calculate_min_coins(amount)

        if result < float('inf'):
            return result
        else:
            return -1
        





