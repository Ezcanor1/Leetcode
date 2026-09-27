class Solution(object):
    def checkIfPangram(self, sentence):
        hash_map={}
        for i in sentence:
            hash_map[i]=hash_map.get(i,0)+1
        count=0
        for k,v in hash_map.items():
            count+=1
        return count>=26
        