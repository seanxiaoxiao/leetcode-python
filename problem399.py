from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = self.makeGraph(equations, values)
        res = []
        for query in queries:
            res.append(self.queryValue(nodes, query))
        return res


    def makeGraph(self, equations: List[List[str]], values: List[float]):
        nodes = {}
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            start = equation[0]
            end = equation[1]
            if not nodes.get(start):
                nodes[start] = {}
            if not nodes.get(end):
                nodes[end] = {}
            nodes[start][end] = value
            nodes[end][start] = 1.0 / value
        return nodes

    def queryValue(self, nodes, query: List[str]) -> float:
        visited = set()
        visited.add(query[0])
        return self.calculateValue(nodes, nodes.get(query[0]), query[1], 1, visited)

    def calculateValue(self, nodes, node, end, value, visited) -> float:
        if not node:
            return -1
        next_nodes = node.keys()
        for next_node in next_nodes:
            if next_node == end:
                visited.add(next_node)
                return value * node[next_node]
            elif next_node not in visited:
                visited.add(next_node)
                next_value = value * node[next_node]
                val = self.calculateValue(nodes, nodes[next_node], end, next_value, visited)
                if val >= 0:
                    return val
        return -1

s = Solution()
print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))