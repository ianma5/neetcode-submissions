class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create n buckets and a hashmap
        hashmap = {}
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for item in hashmap:
            buckets[hashmap[item]].append(item)

        result = []
        for i in range(len(nums),0,-1):
           for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result