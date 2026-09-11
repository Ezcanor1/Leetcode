class Solution(object):
    def minimumDeletions(self, nums):
        f=nums.index(max(nums))+1
        b=nums.index(min(nums))+1
        if len(nums)<=1:
            return 1
        print(f,b)
        print(max(f,b))
        print(len(nums))
        print((b+len(nums)-f))+1
        print(f+(len(nums)-b)+1)
        print(min(f+(len(nums)-b)+1,b+(len(nums)-f)+1))
        # if max(f,b)<(f+len(nums)-b):
        #     return max(f,b)
        
        print(max(len(nums)-f,len(nums)-b))+1
        # print(min(len(nums)-f),len(nums)-b)
        return min(max(len(nums)-f,len(nums)-b)+1,max(f,b),f+(len(nums)-b)+1,b+(len(nums)-f)+1)
            

        