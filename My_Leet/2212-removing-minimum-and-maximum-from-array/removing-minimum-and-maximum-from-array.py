class Solution(object):
    def minimumDeletions(self, nums):
        f=nums.index(max(nums))+1
        b=nums.index(min(nums))+1
        if len(nums)<=1:
            return 1
        return min(max(len(nums)-f,len(nums)-b)+1,max(f,b),f+(len(nums)-b)+1,b+(len(nums)-f)+1)
        
            

        