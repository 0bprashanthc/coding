class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = [0]*length, [0]*length
        left[0], right[length-1] = 1,1
        result = [0]*length
        for i in range(1,length):
            left[i] = left[i-1]*nums[i-1]
        right = 1
        for i in reversed(range(length)):
            result[i] = left[i]*right
            right = right * nums[i]
        return result