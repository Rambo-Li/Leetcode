class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = max_x_edge = len(matrix)
        n = max_y_edge = len(matrix[0])
        x = y = min_edge = 0
        cnt = 0
        res = []
        while cnt < m*n:
            res.append(matrix[x][y])
            cnt += 1
            if x == min_edge and y < max_y_edge-1:
                y += 1
            elif y == max_y_edge -1 and x < max_x_edge-1:
                x += 1
            elif x == max_x_edge-1 and y > min_edge:
                y -= 1
            elif y == min_edge and x > min_edge+1:
                x -= 1
            else:  # only when a line matrix
                x += 1
            
            if y == min_edge and x == min_edge+1:
                    min_edge += 1
                    max_x_edge -= 1
                    max_y_edge -= 1
            
        return res

        # result = []
        # while matrix:
        #     result.extend(matrix.pop(0))

        #     if matrix:
        #         for i in matrix:
        #             if i:
        #                 result.append(i.pop())

        #     if matrix:
        #         matrix[-1].reverse()
        #         result.extend(matrix.pop())

        #     for i in matrix[::-1]:
        #         if i:
        #             result.append(i.pop(0))

        # return result
'''
Concept: munipulate indexes and flags, dealing with different scenarios
DS: flags
Algo: flags and indexes, when to update what
'''