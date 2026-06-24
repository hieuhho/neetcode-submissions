class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid_row = start + ((end - start) // 2)
            if matrix[mid_row][0] > target:
                end = mid_row - 1
            elif matrix[mid_row][-1] < target:
                start = mid_row + 1
            else:
                return target in matrix[mid_row]
        return False