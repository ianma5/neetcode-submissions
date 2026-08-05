class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        for num in counts:
            frequency[counts[num]].append(num)
        
        result = []
        for i in range(len(frequency)-1,0,-1):
            if len(frequency[i]) != 0:
                for n in frequency[i]:
                    result.append(n)
                    if len(result) >= k:
                        return result
        return result