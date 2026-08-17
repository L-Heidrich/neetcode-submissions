
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        q = deque()
        fresh = 0

        length = len(grid[0])
        height = len(grid)

        for i in range(len(grid)): 
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        while q: 
            for _ in range(len(q)):
                r, c = q.popleft()


                neighbors = [(r-1, c),
                            (r+1, c),
                            (r, c-1),
                            (r, c+1)]
                
                for n in neighbors: 
                    
                    if height > n[0] >= 0 and length > n[1] >= 0: 
                        if grid[n[0]][n[1]] == 1: 

                            grid[n[0]][n[1]] = 2
                            q.append((n[0],n[1]))
                            fresh -= 1
            
            if q:
                minutes += 1

        if fresh == 0: 
            return minutes
        else: 
            return -1


