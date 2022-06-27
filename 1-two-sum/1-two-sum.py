class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = dict()
        size = len(nums)
        for i in range(size):
            diff = target-nums[i]
            if diff in _map:
                return i,_map[diff]
            _map[nums[i]] = i
        return -1,-1