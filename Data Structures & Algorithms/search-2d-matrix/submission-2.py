class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        l,r = 0, ROWS-1
        m = l + ((r-l) // 2)
        while(l <= r):
            m = l + ((r-l) // 2)
            if matrix[m][0] > target :
                r = m-1
            elif matrix[m][COLUMNS-1] < target :
                l = m+1
            else:
                break
            
        l1,r1 = 0, COLUMNS-1
        while (l1 <= r1 ):
            n = l1 + (r1-l1) // 2
            if matrix[m][n] > target :
                r1 = n-1
            elif matrix[m][n] < target :
                l1 = n+1
            else :
                return True
        return False