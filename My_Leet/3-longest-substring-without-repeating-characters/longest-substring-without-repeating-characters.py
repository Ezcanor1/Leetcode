class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans=""
        # index=0
        current_count=max_count=0
        for i in s:
            if i not in ans:
                ans+=i
                max_count=max(max_count,len(ans))
            else:
                temp=ans.index(i)
                ans=ans[temp+1:]
                ans+=i
        return max_count
    
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         arr=""
#         max_len=0
#         index=0
#         for i in s:
#             if i not in arr:
#                 arr+=i
#                 max_len=max(max_len,len(arr))
#             else:
#                 # arr+=i
#                 duplicate_position = arr.index(i)
#                 arr=arr[duplicate_position+1:]
                
#                 arr+=i
            
#         return max_len

        