class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        left, right = 0, size-1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum > target:
                right -= 1
            elif _sum < target:
                left += 1
            else:
                return [left+1, right+1]     
        return [-1,-1]