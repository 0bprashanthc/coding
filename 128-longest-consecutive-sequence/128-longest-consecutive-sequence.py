class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums:
            if num-1 not in nums_set:
                current = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_num += 1
                    current += 1
                longest = max(longest, current)
        return longest