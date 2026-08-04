class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n in counts:
                counts[n] +=1
            else:
                counts[n] = 1
        
        for item in counts:
            buckets[counts[item]].append(item)

        result = []
        for i in range(len(buckets) -1 , 0, -1):      
            for n in buckets[i]:
                result.append(n)
                if len(result) >=k:
                    return result
        return result