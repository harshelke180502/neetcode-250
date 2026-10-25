class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        #bfs solution - jump game 2 and 7
        #TC-O(N) AND SC-O(1)
        q=deque([0])
        farthest=0
        while q:
            i=q.popleft()
            start=max(i+minJump,farthest+1)
            for j in range(start,min(i+maxJump+1,len(s))):
                if s[j]=="0":
                    q.append(j)
                    if j==len(s)-1:
                        return True
            farthest=i+maxJump
        return False

        # dp={}
        # def dfs(i):
        #     if i>=len(s) or s[i]=="1":
        #         return False
        #     if i==len(s)-1:
        #         return True
        #     if i in dp:
        #         return dp[i]
        #     end=min(i+maxJump+1,len(s))
        #     for j in range(i+minJump,end):
        #         if dfs(j):
        #             dp[i]=True
        #             return True
        #     dp[i]=False
        #     return False
        # return dfs(0)


             
