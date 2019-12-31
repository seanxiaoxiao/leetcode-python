from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        queue = []
        queue.append([start[0], start[1], 0])
        dis = 0
        cache = [[None for x in range(len(maze[0]))] for y in range(len(maze))]
        visited = [[False for x in range(len(maze[0]))] for y in range(len(maze))]
        while len(queue) > 0:
            size = len(queue)
            element_to_remove = []
            for i in range(size):
                element = queue[i]
                i_index = element[0]
                j_index = element[1]
                visited[i_index][j_index] = True
                if cache[element[0]][element[1]] == None:
                    cache[i_index][j_index] = {}
                    for i in range(4):
                        result = self.destinationAndDistance(maze, i_index, j_index, i)
                        if result[2] != 0 and not visited[result[0]][result[1]]:
                            cache[i_index][j_index][i] = result
                for i in range(4):
                    if len(cache[i_index][j_index]) > 0 and cache[i_index][j_index].get(i) and cache[i_index][j_index][i][2] != 0 and dis == element[2] + cache[i_index][j_index][i][2]:
                        target_i = cache[i_index][j_index][i][0]
                        target_j = cache[i_index][j_index][i][1]
                        if target_i == destination[0] and target_j == destination[1]:
                            return dis
                        if not visited[target_i][target_j]:
                            queue.append([target_i, target_j, dis])
                        del cache[i_index][j_index][i]
                if len(cache[i_index][j_index].keys()) == 0:
                    element_to_remove.append(element)
            for element in element_to_remove:
                queue.remove(element)
            dis += 1
        return -1

    def destinationAndDistance(self, maze: List[List[int]], i, j, direction):
        if direction == 0:
            for index in reversed(range(-1, i)):
                if index == -1:
                    return [0, j, i]
                elif maze[index][j] == 1:
                    return [index + 1, j, i - index - 1]
        elif direction == 1:
            for index in range(i + 1, len(maze) + 1):
                if index == len(maze):
                    return [len(maze) - 1, j, len(maze) - i - 1]
                elif maze[index][j] == 1:
                    return [index - 1, j, index - i - 1]
        elif direction == 2:
            for index in reversed(range(-1, j)):
                if index == -1:
                    return [i, 0, j]
                elif maze[i][index] == 1:
                    return [i, index + 1, j - index - 1]
        elif direction == 3:
            for index in range(j + 1, len(maze[0]) + 1):
                if index == len(maze[0]):
                    return [i, len(maze[0]) - 1, len(maze[0]) - j - 1]
                elif maze[i][index] == 1:
                    return [i, index - 1, index - j - 1]

s = Solution()
print(s.shortestDistance([[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]],[0,0],[8,6]))