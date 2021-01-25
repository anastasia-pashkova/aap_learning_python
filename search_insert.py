class Solution:
    def searchInsertIndex(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left >= right:
            if nums[left] < target:
                return left + 1
            else:
                return left
        
        mid = ( right - left ) // 2 + left 
        mid_val = nums[mid]
        
        if mid_val == target:
            return mid;
        elif mid_val < target:
            return self.searchInsertIndex(nums, target, mid + 1, right)
        else:
            return self.searchInsertIndex(nums, target, left, mid - 1)
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchInsertIndex(nums, target, 0, len(nums) - 1)
        
