class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
            [0,2,3,1,8,6,9]
                   . .
                 3,1,8,6
                 _min,_max = 1,8
             (0,2) > _min; _min = i+1
             (9) < _max; _max = j-1
        """
        length = len(nums)
        if length == 0 or length == 1:
            return 0
        front, back = 0, length-1
        while front < length-1:
            if nums[front] > nums[front+1]:
                break
            front += 1
        while back > 0:
            if nums[back] < nums[back-1]:
                break
            back -= 1
        result = nums[front:back+1]
        if not result:
            return 0
        _min, _max = min(result), max(result)
        i = 0
        while i < front:
            if nums[i] > _min:
                front = i
                break
            i += 1
        j = length-1
        while j > back:
            if nums[j] < _max:
                back = j
                break
            j -= 1
        result = nums[front:back+1]
        return len(result)
        