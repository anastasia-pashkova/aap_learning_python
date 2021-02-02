class Solution:
#     def searchInsertIndex(self, nums: List[int], target: int, left: int, right: int) -> int:
#         if left >= right:
#             if nums[left] < target:
#                 return left + 1
#             else:
#                 return left
        
#         mid = ( right - left ) // 2 + left 
#         mid_val = nums[mid]
        
#         if mid_val == target:
#             return mid;
#         elif mid_val < target:
#             return self.searchInsertIndex(nums, target, mid + 1, right)
#         else:
#             return self.searchInsertIndex(nums, target, left, mid - 1)
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return self.searchInsertIndex(nums, target, 0, len(nums) - 1)
        
        left = 0
        right = len(nums) - 1 
        
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return left
            
        
# [1,3,5,6] 
#  0 1 2 3
# target 2
# left 0 right 3 mid 1 val 3
#left 0 right 0
