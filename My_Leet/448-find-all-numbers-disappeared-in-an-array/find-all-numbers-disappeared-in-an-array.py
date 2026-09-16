import copy
class Solution(object):
    def findDisappearedNumbers(self, nums):
        hashmap={}
        ans=[]
        for i in range(1,len(nums)+1):
            hashmap[i]=hashmap.get(i,0)
        print(hashmap)
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        print(hashmap)
        for k,v in hashmap.items():
            if v==0:
                ans.append(k)
        print(ans)
        return ans