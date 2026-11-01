class Solution:
    def checkValidString(self, s: str) -> bool:
        star=[]
        left=[]
        for i,ch in enumerate(s):
            if ch=="(":
                left.append([ch,i])
            elif ch=="*":
                star.append([ch,i])
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while star and left:
            if star[-1][1]>left[-1][1]:
                left.pop()
                star.pop()
            else:
                return False
        
        return not left
        # if star:
        #     return True
        # if left:
        #     return False 
        # return True
        
            
        
                

        