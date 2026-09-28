class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1count,s2count=[0]*26,[0]*26

        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1
        
        matches=0
        for i in range(26):
            if s1count[i]==s2count[i]:
                matches+=1
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            index=ord(s2[r])-ord('a')
            s2count[index]+=1
            if s2count[index]==s1count[index]:
                matches+=1
            elif s1count[index]+1==s2count[index]:
                matches-=1
            
            index=ord(s2[l])-ord('a')
            s2count[index]-=1
            if s2count[index]==s1count[index]:
                matches+=1
            elif s1count[index]-1==s2count[index]:
                matches-=1
            l+=1
        return matches==26



        # count1={}
        # for i in range(len(s1)):
        #     count1[s1[i]]=1+count1.get(s1[i],0)
        # count2={}
        # l=0
        # for r in range(len(s2)):
        #     count2[s2[r]]=1+count2.get(s2[r],0)
        #     if r-l+1>len(s1):
        #         count2[s2[l]]-=1
        #         if count2[s2[l]]==0:
        #             count2.pop(s2[l],None)
        #         l+=1
        #     if r-l+1==len(s1) and count1==count2:
        #         return True
        # return False
