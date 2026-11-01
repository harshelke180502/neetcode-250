class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candies=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)
        total=sum(candies)
        return total

        # sums=1
        # prev=ratings[0]
        # for i in range(1,len(ratings)):
        #     if i+1<len(ratings) and ratings[i]<prev and ratings[i]<ratings[i+1]:
                

        