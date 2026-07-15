class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix)-1) * (len(matrix[0])-1)

        while l<=r:
            m = l + (r-l)//2
            r,c = m//len(matrix),m%len(matrix)
            
            if matrix[r][c] < target:
                l = m+1
            elif matrix[r][c] > target:
                r = m+1
            else:
                return True
        
        return False