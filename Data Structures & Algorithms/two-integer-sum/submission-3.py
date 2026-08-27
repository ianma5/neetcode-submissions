class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] == target

        # nums[j] = target - nums[i]

        hashmap = {} # organize by number: index

        for i in range(len(nums)):
            if (target-nums[i]) in hashmap:
                result = [i, hashmap[target-nums[i]]]
                return sorted(result)
            else:
                hashmap[nums[i]] = i