class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, _ in enumerate(numbers): 
            for x, _ in enumerate(numbers):
                if i == x:
                    continue
                elif (numbers[i] + numbers[x] == target) and i < x:
                    return [i + 1, x + 1 ]
        return 
