class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Runtime O(n)
        
        if not nums:
            return 0
        
        # current running sum
        sum = nums[0]
        max_sum = sum
        i = 1
        
        while(i < len(nums)):       
            if ( sum < 0 and sum < nums[i]):
                # restart the max running sum
                sum = nums[i]
            else:
                sum += nums[i]
            
            if max_sum < sum:
                max_sum = sum
            i+=1
            
        return max_sum
    
        # brute first first approach O(n^2)   
        # for lo in range(len(nums)):
        #     sum = 0
        #     for hi in range(lo, len(nums)): #first param inclusive, second exclusive
        #         sum += nums[hi]
        #         if(sum > max_found):
        #             max_found = sum
        # return max_found
    # [-2,1,-3,4,-5,6,-1,2,1,-5,4]
    #[1]
    # [-2,1]
    # [1,2]
