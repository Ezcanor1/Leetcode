class Solution(object):
    def judgeSquareSum(self, c):
        i=0
        j=int(c**0.5)
        
        while i<=j:
            if i*i == c or j*j == c:
                return True
            if (i*i+j*j)==c:
                return True
            elif (i*i+j*j)>c:
                j-=1
            elif (i*i+j*j)<c:
                i+=1
        return False