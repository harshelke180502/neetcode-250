class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                n=len(matrix[0])
                candidate_row=-1
                boolean=False
                L=0
                H=len(matrix)-1
                while(L<=H):
                    M=(L+H)//2
                    if target<matrix[M][0]:
                        H=M-1
                    elif target>matrix[M][-1]:
                        L=M+1
                    else:
                        candidate_row=M
                        
                        break

                if candidate_row==-1:
                    return False


                search_matrix=matrix[candidate_row]
              


                l=0
                h=n-1
                while(l<=h):
                    m=(l+h)//2

                    if target>search_matrix[m]:
                        l=m+1
                    elif target<search_matrix[m]:
                        h=m-1
                    else:
                        return True
                return False


