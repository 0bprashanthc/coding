class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start, end = 0, length-1
        while start <= end:
            pivot = start + (end - start) // 2
            if nums[pivot] > target:
                end = pivot - 1
            elif nums[pivot] < target:
                start = pivot + 1
            else:
                return pivot
        return -1