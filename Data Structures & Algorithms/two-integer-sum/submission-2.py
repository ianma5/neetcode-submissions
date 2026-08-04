class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create hashmap for the list
        # loop through the nums with index
        # check if target - nums[i] exists
        # if it does we found the solution
        # otherwise add to hashmap
        hashmap = {}
        for index, element in enumerate(nums):
            if target - element in hashmap:
                return sorted([index, hashmap[target-element]])
            else:
                hashmap[element] = index