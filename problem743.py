from typing import List

import sys

class Node:

    def __init__(self, val):
        self.connection = {}
        self.val = val
        self.time_to_arrive = 0

    def setConnection(self, target, weight):
        self.connection[target] = weight


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        nodes = []
        for i in range(N + 1):
            nodes.append(Node(i))
        for time in times:
            node = nodes[time[0]]
            node.setConnection(time[1], time[2])

        start_node = nodes[K]
        node_queue = []
        node_queue.append(start_node)
        visited = {}
        visited[K] = True
        res = 0
        while len(node_queue) > 0:
            min_time = sys.maxsize
            for node in node_queue:
                res = max(res, node.time_to_arrive)
                for key in node.connection:
                    min_time = min(min_time, node.connection[key])

            node_to_add = []
            for node in node_queue:
                key_to_remove = []
                for key in node.connection.keys():
                    if not visited.get(key) and min_time == node.connection[key]:
                        visited[key] = True
                        node_to_add.append(nodes[key])
                        key_to_remove.append(key)
                        nodes[key].time_to_arrive = node.time_to_arrive + min_time
                    elif visited.get(key):
                        key_to_remove.append(key)

                for key in key_to_remove:
                    del node.connection[key]

            node_to_remove = []
            for node in node_queue:
                if len(node.connection.keys()) == 0:
                    node_to_remove.append(node)


            for node in node_to_remove:
                node_queue.remove(node)

            for node in node_to_add:
                node_queue.append(node)

        return res if len(visited) == N else -1

s = Solution()
print(s.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))