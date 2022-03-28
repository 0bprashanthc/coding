class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0:
            return []
        result = []
        start, end = 0, length-1
        while start <= end:
            start_square = nums[start]*nums[start]
            end_square = nums[end]*nums[end]
            if start_square < end_square:
                result.insert(0,end_square)
                end -= 1
            elif start_square > end_square:
                result.insert(0,start_square)
                start += 1
            else:
                result.insert(0,start_square)
                if start != end:
                    result.insert(0,end_square)
                    end -= 1
                start += 1
        return result