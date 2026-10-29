class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        n=len(senate)
        D,R=deque(),deque()

        for idx,c in enumerate(senate):
            if c=="R":
                R.append(idx)
            else:
                D.append(idx)
        while R and D:
            dTurn=D.popleft()
            rTurn=R.popleft()
            if rTurn<dTurn:
                R.append(rTurn+n)
            else:
                D.append(dTurn+n)

        return "Radiant" if R else "Dire"

        