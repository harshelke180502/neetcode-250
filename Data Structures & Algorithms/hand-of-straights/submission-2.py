class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        #Using Heap

        if len(hand)%groupSize!=0:
            return False
        count=Counter(hand)
        minH=list(count.keys())
        heapq.heapify(minH)
        
        while minH:
            first=minH[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

        #TC-O(N), SC-O(N)- USING HASHMAP
        # if len(hand)%groupSize!=0:
        #     return False
        # count=Counter(hand)
        # print(count)
        # for num in hand:
        #     start=num
        #     while count[start-1]:
        #         start-=1
        #     while start<=num:
        #         while count[start]:
        #             for i in range(start,start+groupSize):
        #                 if not count[i]:
        #                     return False
        #                 count[i]-=1
        #         start+=1
        # return True







        
            




                
            


        