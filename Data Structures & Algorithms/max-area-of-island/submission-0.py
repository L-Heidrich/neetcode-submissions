class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_size = 0

        height = len(grid)
        length = len(grid[0])

        visited = set()

        def dfs(node):
            r, c = node
            visited.add((r, c))

            neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            
            total = 0

            for nr, nc in neighbors:
                if not (0 <= nr < height and 0 <= nc < length):
                    continue
                if (nr, nc) in visited:
                    continue
                if grid[nr][nc] != 1:
                    continue
                total += dfs((nr, nc))

            return 1 + total


        for x in range(height):
            for y in range(length):
                if grid[x][y] == 1 and (x,y) not in visited:
                    max_size = max(max_size, dfs((x,y)))

        return max_size