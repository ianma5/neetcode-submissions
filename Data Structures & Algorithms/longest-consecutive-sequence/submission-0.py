class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq_length = 0
        for num in nums:
            if num-1 not in nums:
                x = num
                curr_length = 1
                while x+1 in nums:
                    curr_length +=1
                    x = x+1
                if curr_length > seq_length:
                    seq_length = curr_length
        return seq_length

            