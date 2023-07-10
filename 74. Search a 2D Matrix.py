class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = [a[0] for a in matrix]
        up, down = 0, len(m) -1
        row = None
        while up <= down:
            mid = (up+down)//2
            if target < m[mid]:
                down = mid -1
            elif target > m[mid]:
                up = mid + 1
                row = mid
            else:
                return True
        if row == None:
            return False
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left+right)//2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = left + 1
            else:
                return True
        return False
