# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        first_bad_version = n
        
        while left <= right: 
            mid = ( left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
                if first_bad_version > mid:
                    first_bad_version = mid
            else:
                left = mid + 1 
                
        return first_bad_version    
