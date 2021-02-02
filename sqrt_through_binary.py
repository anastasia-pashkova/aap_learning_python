class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
            
        left = 1
        right = x
        
        
        while left <= right:
            mid = (left + right)//2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared > x:
                right = mid - 1    
            else:
                left = mid + 1     
                
        return right
            
# 8 
# left 1 right 8
# mid = 4 squared 16
# left 1 right 3
# mid  2 sq 4 
# left 3
# right 2
    
    
    
#     8
    
#     0 ... 4
    
#     x * x 
    
#     8 
    
#     x  s.t x * x = 8
    
#     8 / 2 -> 0 -> 4 mid
    
#     4 x 4 = 16 >  ==target return  if >  -> keep dividing 
    
#     2 * 2 = 4 < target  2 and  3 * 3 = 9 
