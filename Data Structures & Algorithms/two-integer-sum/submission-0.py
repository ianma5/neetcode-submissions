class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                l = [index, hashmap[difference]]
                l.sort()
                return l
            hashmap[value] = index
