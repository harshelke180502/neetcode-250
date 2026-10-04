class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(speed)
        times_stack=[0]*n
        for idx in range(n):
            time=(target-position[idx])/speed[idx]
            times_stack[idx]=(position[idx],time)
        times_stack.sort(key=lambda x:x[0],reverse=True)
        fleets=0
        previous_time=0
        # print(times_stack)
        for position,current_time in times_stack:
            if current_time>previous_time:
                fleets+=1
                previous_time=current_time
            # print(f" Fleet at {position,current_time}: {fleets}")
        return fleets


        



    

        
        