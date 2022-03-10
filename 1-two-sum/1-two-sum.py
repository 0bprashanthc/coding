class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = dict()
        for index,value in enumerate(nums):
            diff = target-value
            if diff in hs:
                return [hs[diff],index]
            else:
                hs[value] = index
        return