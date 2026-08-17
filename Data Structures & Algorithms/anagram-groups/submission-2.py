class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            tuple_arr = tuple(arr)
            if tuple_arr in hashmap:
                hashmap[tuple_arr].append(s)
            else:
                hashmap[tuple_arr] = [s]
        return list(hashmap.values())

