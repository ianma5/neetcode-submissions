class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force solution
        window_max = []
        for i in range(len(nums)+1):
            current_max = -10000
            if i+k > len(nums):
                break
            for j in range(i, i+k):
                if nums[j] > current_max:
                    current_max = nums[j]
            window_max.append(current_max)
        return window_max