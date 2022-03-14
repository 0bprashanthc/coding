class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] in hm:
                return True
            else:
                hm[nums[i]] = i
            i = i + 1
        return False
        