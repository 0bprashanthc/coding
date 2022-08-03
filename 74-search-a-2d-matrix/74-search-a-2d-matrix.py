class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array: List[int], target) -> bool:
            length = len(array)
            start, end = 0, length-1
            while start <= end:
                pivot = start + (end - start) // 2
                if array[pivot] > target:
                    end = pivot - 1
                elif array[pivot] < target:
                    start = pivot + 1
                else:
                    return True
            return False
        length = len(matrix)
        start, end = 0, length-1
        while start <= end:
            pivot = start + (end - start) // 2
            found = binarySearch(matrix[pivot], target)
            if not found:
                _value = matrix[pivot][-1]
                if _value > target:
                    end = pivot - 1
                elif _value < target:
                    start = pivot + 1
            else:
                return found
        return False