class Solution(object):
    def countCommas(self, n):
        value=len(str(n))
        v=999
        t=n
        if n<1000:
            return 0
        if value>3 and value<7:
            return n-999
        if value>6 and value<10:
            v=999999 
        if value>9 and value<13:
            v=999999999  
        if value>12 and value<16:
            v=999999999999
        if value>=16:
            v=999999999999999
        while(v>=999):
            t=t-v
            v=v//1000
        if len(str(n))>=16:
            return (t+n+n+n+n)
        if len(str(n))>12 and len(str(n))<16:
            return (t+n+n+n)
        if len(str(n))>=10:
            return (t+n+n)
        
        return t+n