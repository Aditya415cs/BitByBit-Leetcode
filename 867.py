class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r=len(matrix)
        c=len(matrix[0])
        transpose=[]
        for k in range(c):
            row=[]
            for l in range(r):
                   row.append(0)
            transpose.append(row)       
        for i in range(r):
            for j in range(c):
                transpose[j][i]=matrix[i][j]
        return transpose     
        
