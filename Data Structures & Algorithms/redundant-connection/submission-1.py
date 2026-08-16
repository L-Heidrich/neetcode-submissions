
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        def dfs(u, v):
            if u == v:
                return True

            for n in graph[u]:
                if n in visited:
                    continue
                else:
                    visited.add(n)
                    if dfs(n, v):
                        return True
            return False

        for u,v in edges:
            visited = set()

            if dfs(u,v):
                return [u,v]
            else:
                graph[u].append(v)
                graph[v].append(u)