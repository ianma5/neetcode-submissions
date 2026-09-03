class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, anchor in enumerate(nums):

            if i > 0 and nums[i-1] == anchor:
                continue
            left = i+1
            right = len(nums)-1

            while left < right:
                threesum = anchor + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    results.append([anchor, nums[left], nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return results
