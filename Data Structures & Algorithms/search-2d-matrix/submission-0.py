class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get dimensions of matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # first search over rwos
        # scan top and bottom rows
        # compare target with row's first and last elements
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                # shift row up for big vals
                top = row + 1
            elif target < matrix[row][0]:
                # shift row down for small val
                bot = row - 1
            else:
                # if target val is in row
                break
        
        # no rows contain target
        if not (top <= bot):
            return False

        # run second binary search on current row found in prev search
        # scan inside row
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False