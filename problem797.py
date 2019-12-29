from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        res = []
        nodes = self.makeGraph(graph)
        visited = set()
        visited.add(0)
        self.makeRoute(nodes, nodes[0], visited, N, res, [0])
        return res

    def makeGraph(self, graph: List[List[int]]):
        nodes = {}
        for i in range(len(graph)):
            routes = graph[i]
            nodes[i] = set()
            for dst in routes:
                nodes[i].add(dst)
        return nodes

    def makeRoute(self, nodes, node, visited, N, res, route):
        if not node:
            return
        for next_node_val in node:
            new_route = route[:]
            if next_node_val == N:
                new_route.append(next_node_val)
                res.append(new_route)
            elif next_node_val not in visited:
                next_node = nodes[next_node_val]
                visited.add(next_node_val)
                new_route.append(next_node_val)
                self.makeRoute(nodes, next_node, visited, N, res, new_route)
                visited.remove(next_node_val)
s = Solution()
print(s.allPathsSourceTarget([[4,3,1,8,6],[2,4,7],[8,4,6,5,3],[8,6,5,4],[7,6,5,8],[6,7],[7],[8],[]]))