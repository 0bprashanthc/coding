class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        i, current_sum, count = 0, 0, 0
        hm = {}
        while i < length:
            current_sum = current_sum + nums[i]
            if current_sum == k:
                count = count + 1
            if current_sum-k in hm:
                count = count + hm[current_sum-k]
            if current_sum in hm:
                hm[current_sum] += 1
            else:
                hm[current_sum] = 1
            i = i + 1
        return count