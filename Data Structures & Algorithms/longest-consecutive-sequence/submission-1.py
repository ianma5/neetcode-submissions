class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        count = 0

        for num in hash_set:
            if num-1 in hash_set:
                continue
            else:
                test = num
                tempcount = 1
                while test+1 in hash_set:
                    tempcount+=1
                    test +=1
                if tempcount > count: count = tempcount
        return count