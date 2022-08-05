class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = max(piles)
        start, end = 1, maxBananas
        while start < end:
            currentSpeed = ( end + start ) // 2
            totalHours = 0
            for each_pile in piles:
                totalHours = totalHours + math.ceil(each_pile / currentSpeed)
            if totalHours <= h:
                end = currentSpeed
            else:
                start = currentSpeed + 1
        return end