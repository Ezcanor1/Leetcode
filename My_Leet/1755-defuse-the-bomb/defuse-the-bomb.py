import copy
class Solution(object):
    def decrypt(self, code, k):
        temp=copy.deepcopy(code)
        n=len(code)
        if k==0:
            return [0]*n
        if k>0:
            j=k+1
            code[0]=sum(temp[1:k+1])
            for i in range(1,n):
                j=j%n
                code[i]=code[i-1]-temp[i]+temp[j]
                j+=1
        else:
            k=abs(k)
            code[0]=sum(temp[n-k:])
            j=n-k
            for i in range(1,n):
                j=j%n
                code[i]=code[i-1]-temp[j]+temp[i-1]
                j+=1
            
        return code