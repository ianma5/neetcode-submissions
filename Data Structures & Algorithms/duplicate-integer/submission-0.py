class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final_set = set(nums)
        if (len(final_set) != len(nums)):
            return True
        return False