from typing import List

class Solution:
  def exist(self, board: List[List[int]], word: str):
    def dfs(i, j, cur):
      if cur == len(word):
        return True
      if ( i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[cur] or board[i][j] == "0" ):
        return False
      t = board[i][j]
      board[i][j] = "0"
      for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x, y = i + a, j + b
        if dfs(x, y, cur + 1):
          return True
      board[i][j] = t
      return False
    m, n = len(board), len(board[0])
    return any(dfs(i, j, 0) for i in range(m) for j in range(n))
  
sol = Solution()

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(sol.exist(board, word))