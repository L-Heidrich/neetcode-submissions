class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        height = len(grid)
        length = len(grid[0])

        totals = 0

        def mark_neighbors(node):
            neighbors = [(node[0], node[1]-1),
                        (node[0], node[1]+1),
                        (node[0]+1, node[1]),
                        (node[0]-1, node[1])]

            for n in neighbors: 
                if height > n[0] >= 0 and length > n[1] >= 0:
                    if grid[n[0]][n[1]] == "1":
                        if (n[0],n[1]) in visited:
                            continue
                        else:
                            visited.add((n[0],n[1]))
                            mark_neighbors((n[0],n[1]))

        for i in range(height):
            for j in range(length):

                if grid[i][j] == "1":
                    if (i, j) in visited:
                        continue
                    else:
                        totals += 1
                        visited.add((i,j))
                        mark_neighbors((i,j))

        return totals

