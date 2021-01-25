class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slower_index = 0
        for index, element in enumerate(nums):
            if(element != val):
                nums[slower_index] = element
                slower_index+=1
                
        return slower_index
                
