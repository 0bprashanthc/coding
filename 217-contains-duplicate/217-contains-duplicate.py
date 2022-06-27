class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        i = 0
        size = len(nums)
        while i < size:
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            i = i + 1
        return False
        
        