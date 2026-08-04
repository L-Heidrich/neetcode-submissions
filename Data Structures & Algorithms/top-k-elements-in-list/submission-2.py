class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # ---- PHASE 1: count every element (global, one pass) ----
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # .get(num, 0) returns current count, or 0 if unseen, then +1.
        # After the loop for [1,1,1,2,2,3]:
        #   count = {1: 3, 2: 2, 3: 1}

        # ---- PHASE 2: bucket elements by their frequency ----
        buckets = [[] for _ in range(len(nums) + 1)]
        # One empty list per possible frequency, 0..len(nums).
        # len(nums)=6, so 7 bins, indices 0–6:
        #   buckets = [[], [], [], [], [], [], []]
        #              0   1   2   3   4   5   6   <- index = frequency

        for num, freq in count.items():
            buckets[freq].append(num)
        # Drop each element into the bin matching its count:
        #   (1, 3) -> buckets[3].append(1)
        #   (2, 2) -> buckets[2].append(2)
        #   (3, 1) -> buckets[1].append(3)
        # Result:
        #   buckets = [[], [3], [2], [1], [], [], []]
        #              0   1    2    3    4   5   6

        # ---- PHASE 3: read bins high frequency -> low, take k ----
        result = []
        for freq in range(len(nums), 0, -1):   # 6,5,4,3,2,1
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
