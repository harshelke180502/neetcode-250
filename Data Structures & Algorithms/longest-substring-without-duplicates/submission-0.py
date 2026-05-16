class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            max_count=0
            for i in range(0,len(s)):
                l=[s[i]]
                j=i+1

                if len(s)==0:
                    max_count=0
                    break
                
                if len(s)==1:
                    max_count=1
                    break

                while(j<len(s) and s[j] not in l):
                    
                    l.append(s[j])
                    # print(l)
                    j=j+1
                max_count=max(len(l),max_count)
            return (max_count)
                