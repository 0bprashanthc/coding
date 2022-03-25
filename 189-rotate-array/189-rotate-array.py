class Solution:
    def reverse(self, arr, length, start, end) -> List[int]:
        while start <= end and start < length and end < length:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        start, end = 0, length-1
        # reverse whole array
        nums = self.reverse(nums, length, start, end)
        # reverse 0:k+1 array
        start, end = 0, k-1
        nums = self.reverse(nums, length, start, end)
        # reverse k:length-1
        start, end = k, length-1
        nums = self.reverse(nums, length, start, end)