class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            if tuple(arr) in hashmap:
                hashmap[tuple(arr)].append(s)
            else:
                hashmap[tuple(arr)] = [s]
        return list(hashmap.values())

