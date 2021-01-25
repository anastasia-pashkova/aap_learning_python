class Solution:
    def reverseString(self, s: List[str]) -> None:

        if not s:
            return
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            temp_val = s[left]
            s[left] = s[right]
            s[right] = temp_val
            left +=1
            right -=1
