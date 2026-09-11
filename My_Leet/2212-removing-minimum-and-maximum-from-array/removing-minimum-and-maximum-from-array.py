class Solution(object):
    def minimumDeletions(self, nums):
        f=nums.index(max(nums))+1
        b=nums.index(min(nums))+1
        if len(nums)<=1:
            return 1
        n=len(nums)
        return min(max(n-f,n-b)+1,max(f,b),f+(n-b)+1,b+(n-f)+1)
        
            

        