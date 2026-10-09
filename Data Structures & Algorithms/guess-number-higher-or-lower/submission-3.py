# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=0,n
        #using lower limit theorem as we want to find the exact number
        while l<r:
            m=l+(r-l)//2
            #if the target is smaller than the number we guessed
            if guess(m)<=0:
                r=m
            #if target is larger than the number we guessed
            else:
                l=m+1
        return l 
    






        