class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        hashmap = {}

        for s in strs:
            c_arr = [0] * 26
            for c in s:
                c_arr[ord(c) - ord('a')] += 1
            tuple_c = tuple(c_arr)


            if tuple_c in hashmap:
                hashmap[tuple_c] += [s]
            else:
                hashmap[tuple_c] = [s]


        return list(hashmap.values())