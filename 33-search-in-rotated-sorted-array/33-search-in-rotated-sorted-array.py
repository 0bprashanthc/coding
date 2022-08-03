class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start, end = 0, length-1
        while start <= end:
            pivot = start + (end - start) // 2
            _value = nums[pivot]
            if target == _value:
                return pivot
            if nums[start] <= _value:
                if target > _value or target < nums[start]:
                    start = pivot + 1
                else:
                    end = pivot - 1
            else:
                if target < _value or target > nums[end]:
                    end = pivot - 1
                else:
                    start = pivot + 1
        return -1