class Solution:
    # def shiftRemoveIndex(self, nums: List[int], index_to_remove: int):
    #     for i in range(index_to_remove + 1, len(nums)):
    #         nums[i - 1] = nums [i]
    #     return
    
    def removeDuplicates(self, nums: List[int]) -> int:
    
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        
        i = 0;
        for j in range(1, len(nums)):
             if nums[j] != nums[i]:
                    i+=1
                    nums[i]=nums[j]
        return i + 1
            
        
#         last_unique_index = 0
#         for j in range(1, len(nums)):
#             if nums[j-1] == nums[j]:
#                 self.shiftRemoveIndex(nums, j)
#                 # not efficient to shift every time. Keep in a hash map of indexes to remove, and shift once
#             else:
#                 last_unique_index+=1
        
#         return last_unique_index
    

            
    # ? Python questions - make the helper private
    # throws exception and throw exception
    # elegant python way check for null arrays/lists and not null, or not null, but empty (0 length)
    # == and is that's pointer and reference same memory. does == work with objects? or just primatives?
