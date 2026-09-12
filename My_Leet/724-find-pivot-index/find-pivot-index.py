class Solution(object):
    def pivotIndex(self, nums):
        sumleft=[0]*len(nums)
        sumright=[0]*len(nums)
        currentleft=currentright=0
        j=len(nums)-1
        for i in range(0,len(nums)):
            currentleft+=nums[i]
            sumleft[i]=currentleft
            currentright+=nums[j]
            sumright[j]=currentright
            j-=1
        # currentsum=0
        # for i in range(len(nums)-1,-1,-1):
        #     currentsum+=nums[i]
        #     sumright[i]=currentsum
        print(sumleft)
        print(sumright)
        for i in range(len(nums)):
            if sumright[i]==sumleft[i]:
                return i
        return -1
            
        