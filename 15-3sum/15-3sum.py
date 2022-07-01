class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        nums.sort()
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(i, nums, result)
            i += 1
        return result
    
    def twoSum(self, i, nums, result):
        left, right = i + 1, len(nums)-1
        _value = nums[i]
        while left < right:
            _sum = _value + nums[left] + nums[right]
            if _sum < 0:
                left += 1
            elif _sum > 0:
                right -= 1
            else:
                result.append([nums[left], nums[right], nums[i]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1