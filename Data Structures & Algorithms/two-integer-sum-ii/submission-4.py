class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, _ in enumerate(numbers): 
            for x, _ in enumerate(numbers):
                print(f"{i,x} , ({numbers[i]}, {numbers[x]})")   
                if numbers[i] == numbers[x]:
                    continue
                elif (numbers[i] + numbers[x] == target) and i < x:
                    return [i + 1, x + 1 ]
        return 
