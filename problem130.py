from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if not visited[i][j] and board[i][j] == 'O':
                    res = []
                    result = self.gatherO(board, i, j, res, visited)
                    if not result:
                        for coordinate in res:
                            board[coordinate[0]][coordinate[1]] = 'X'


    def gatherO(self, board, i, j, res, visited):
        if i == -1 or j == -1 or i == len(board) or j == len(board[0]):
            return
        elif not visited[i][j] and board[i][j] == 'O' and (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1):
            visited[i][j] = True
            res.append([i, j])
            self.gatherO(board, i - 1, j, res, visited)
            self.gatherO(board, i + 1, j, res, visited)
            self.gatherO(board, i, j - 1, res, visited)
            self.gatherO(board, i, j + 1, res, visited)
            return True
        elif board[i][j] == 'X':
            return False
        elif not visited[i][j]:
            res.append([i, j])
            visited[i][j] = True
            result = self.gatherO(board, i - 1, j, res, visited)
            result = self.gatherO(board, i + 1, j, res, visited) or result
            result = self.gatherO(board, i, j - 1, res, visited) or result
            result = self.gatherO(board, i, j + 1, res, visited) or result
            return result

s = Solution()
s.solve([["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]])