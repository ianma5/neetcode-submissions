class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # determine frequency (hashmap)
        # sort items into buckets
        # return k most frequent elements
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]

        for key, value in hashmap.items():
            buckets[value].append(key)
        
        final_list = []
        for i in range(len(buckets)-1, -1, -1):
            if k == 0: break
            if not buckets[i]: continue
            for item in buckets[i]:
                final_list.append(item)
                k -= 1
                if k == 0: return final_list
        return final_list
