class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         #   
        n = len(prices)-1

        b_index = 0
        s_index = 0

        profit = 0

        for i, j in enumerate(prices):
            
            if j < prices[b_index]:
                b_index = i
                continue

            if j - prices[b_index] > profit:
                profit = j - prices[b_index]
        return profit

                
            