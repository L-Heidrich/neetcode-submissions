
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

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

        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                return [u, v]
            parent[rv] = ru
            
        for u,v in edges:
            visited = set()

            if dfs(u,v):
                return [u,v]
            else:
                graph[u].append(v)
                graph[v].append(u)