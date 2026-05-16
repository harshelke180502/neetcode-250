class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        
        
        for i in range(0,len(board)):
            no_list_rows=set()
            no_list_columns=set()
            for j in range(0,len(board)):
                if(board[i][j]!="."):
                    if board[i][j] in no_list_rows:
                        return False
                    no_list_rows.add(board[i][j])
                
                if(board[j][i]!="."):
                    if board[j][i] in no_list_columns:
                        return False
                    no_list_columns.add(board[j][i])
                
               
           
            
       
        for row_block in range(0,9,3):
            
            for col_block in range(0,9,3):
                block=set()
                for k in range(0,3):
                    for l in range(0,3):
                        
                        if(board[row_block+k][col_block+l]!="."):

                            if board[row_block+k][col_block+l] in block:
                                return False

                            block.add(board[row_block+k][col_block+l])
                       
                        

        return True
                        
                    

        
                
                
                                
                
                

                            
             
            

        


