class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] = 1

        for item in counts:
            buckets[counts[item]].append(item)

        result = []
        for i in range(len(buckets)-1, 0, -1):
            for element in buckets[i]:
                result.append(element)
                if len(result) >= k:
                    return result

        return result