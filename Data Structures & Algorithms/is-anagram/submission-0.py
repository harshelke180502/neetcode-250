class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        if len(s)!=len(t):
            return False

        for letter in s:
            count[letter]=count.get(letter,0)+1
        for letter in t:
            if letter not in count.keys():
                return False
            count[letter]-=1
            if count[letter]<0:
                return False
        return True
            


        

        