class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [[] for _ in range(len(nums)+1)]
        for num, freq in counter.items():
            frequency[freq].append(num)
        result = list()
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                result.append(n)
            if len(result) == k:
                return result