class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _map = collections.defaultdict(list)
        for string in strs:
            counter = [0]*26
            for char in string:
                counter[ord(char)-ord('a')] += 1
            _map[tuple(counter)].append(string)
        return _map.values()