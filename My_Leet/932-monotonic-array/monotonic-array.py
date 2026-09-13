class Solution(object):
    def isMonotonic(self, nums):
        inc=True
        dec=True
        # if nums[0]<nums[len(nums)-1]:
        for i in range(1,len(nums)):
            if nums[i-1]<=nums[i]:
                continue
            else:
                inc=False
                break
        # if nums[0]>nums[len(nums)-1]:
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                continue
            else:
                dec=False
                break
        print(inc,dec)
        if inc==True or dec==True:
            return True
        return False
    