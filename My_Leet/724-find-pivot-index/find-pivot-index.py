class Solution(object):
    def pivotIndex(self, nums):
        sumleft=[0]*len(nums)
        sumright=[0]*len(nums)
        currentsum=0
        for i in range(0,len(nums)):
            currentsum+=nums[i]
            sumleft[i]=currentsum
        currentsum=0
        for i in range(len(nums)-1,-1,-1):
            currentsum+=nums[i]
            sumright[i]=currentsum
        for i in range(len(nums)):
            if sumright[i]==sumleft[i]:
                return i
        return -1
            
        