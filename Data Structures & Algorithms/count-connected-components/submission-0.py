class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # building the graph without edges.

        graph = {node: [] for node in range(n)}

        # tracking neighbours 

        for node1, node2 in edges: 
            graph[node1].append(node2)
            graph[node2].append(node1)

        #defining the depth first search
        visited = set() 
        components = 0

        # recursively adding all the neighbors to visited in order to skip nodes later, that are connected
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for node in graph:
            if node in visited:
                continue
            else: 
                visited.add(node)
                components += 1
                dfs(node)
        return components
