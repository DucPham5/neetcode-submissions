class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left < right:
            mid = left + ((right-left) // 2)

            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][-1]:
                right = mid
            else:
                return True
        
        row = left
        left = 0
        right = len(matrix[right])-1

        while left <= right:
            mid = left + ((right-left)//2)
            
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid -1
            else: return True

        return False
        