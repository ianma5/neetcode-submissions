class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # o(n) optimal solution
        dq = deque() # create a monotonic deque
        max_list = [] # store list of maximum at each window

        #1. if the index at front of dq is out of bounds of the window, remove it as its no longer a valid maximum
        #2. constantly remove smaller elements; if the new number is larger than the smallest in the dq, remove as its not needed
        #3. add a new element, then if a first window has been already processed, append that number (from top of dq) to list of max
        for i in range(len(nums)): # loop thru nums
            if dq and dq[0] < i - (k-1): 
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i) # add new element
            if i >= k-1: # processed enough elements
                max_list.append(nums[dq[0]])

        return max_list