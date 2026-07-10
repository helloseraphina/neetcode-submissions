# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # if empty grid (no island)
#         if not grid:
#             return 0 
        
#         # get dimension of grid
#         rows, cols = len(grid), len(grid[0])

#         # make cells visited when marking island masses
#         visit = set()
#         # init count num islands
#         islands = 0

#         def bfs(r, c):
#             q = collections.deque()
#             visit.add((r, c))
#             q.append((r,c))

#             # while queue not empty, expand island
#             while q:
#                 row, col = q.popleft()
#                 # check adjacent poisiton of popped position
#                 # 4 directions: [right, left, above, below]
#                 directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

#                 # for each direction (dir row, dir col)
#                 # and if it is a land position 1
#                 # and position univisited
#                 for dr, dc in directions:
#                     r, c = row + dr, col + dc
#                     if ((r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r + dr, c + dc) not in visit):
#                         q.append((r, c))
#                         visit.add((r, c))


#         for r in range(rows):
#             for c in range(cols):
#                 # if visit a 1 (land), traverse
#                 # strs not ints
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     bfs(r, c)
#                     # increment num islands
#                     # if its a 1 we havent visited
#                     islands += 1
        
#         return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Possible movement directions:
        # Down, Up, Right, Left
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        # Number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Counts the number of separate islands
        islands = 0

        # ------------------------------------------------------------------
        # Breadth-First Search (BFS)
        # Explores an entire island starting from (r, c)
        # ------------------------------------------------------------------
        def bfs(r, c):
            # Queue stores cells waiting to be explored
            q = deque()

            # Mark the starting cell as visited by turning it into water.
            # This prevents revisiting the same cell.
            grid[r][c] = "0"

            # Add the starting cell to the queue
            q.append((r, c))

            # Continue until there are no more connected land cells
            while q:

                # Get the next cell to explore
                row, col = q.popleft()

                # Check all four neighboring cells
                for dr, dc in directions:

                    # Coordinates of the neighboring cell
                    nr = row + dr
                    nc = col + dc

                    # Skip this neighbor if:
                    # 1. It is outside the grid
                    # 2. It is already water ("0")
                    # 3. It has already been visited
                    if (
                        nr < 0 or
                        nc < 0 or
                        nr >= ROWS or
                        nc >= COLS or
                        grid[nr][nc] == "0"
                    ):
                        continue

                    # Neighbor is unvisited land ("1")

                    # Add it to the queue so we explore it later
                    q.append((nr, nc))

                    # Immediately mark it as visited.
                    # This prevents other neighboring cells from
                    # adding the same cell to the queue again.
                    grid[nr][nc] = "0"

        # ------------------------------------------------------------------
        # Scan every cell in the grid
        # ------------------------------------------------------------------
        for r in range(ROWS):
            for c in range(COLS):

                # If we find unvisited land,
                # we've discovered a NEW island.
                if grid[r][c] == "1":

                    # Visit every connected land cell
                    bfs(r, c)

                    # Finished exploring one entire island
                    islands += 1

        # Return the total number of islands found
        return islands