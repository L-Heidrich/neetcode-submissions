class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        numss = sorted(nums)
        results = []

        for fixed in range(n - 2):                 # ← fixed now SWEEPS, not frozen at n//2
            if fixed > 0 and numss[fixed] == numss[fixed - 1]:
                continue                           # skip duplicate anchor

            l = fixed + 1                          # ← l starts just RIGHT of fixed, not at 0
            r = n - 1

            while l < r:                           # l and r converge toward each other
                total = numss[l] + numss[r] + numss[fixed]

                if total == 0:
                    results.append([numss[fixed], numss[l], numss[r]])   # values, in a list
                    l += 1
                    r -= 1
                    while l < r and numss[l] == numss[l - 1]:   # skip dup left
                        l += 1
                    while l < r and numss[r] == numss[r + 1]:   # skip dup right
                        r -= 1
                elif total < 0:
                    l += 1                         # too small → grow from left
                else:
                    r -= 1                         # ← too big → SHRINK from right (was r += 1)

        return results