from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        
        def dfs(r, c, index):
            if index == n:
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            board[r][c] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False


def test_exist():
    solution = Solution()
    
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    
    test_cases = [
        (board1, "ABCCED", True, "Пример 1"),
        (board1, "SEE", True, "Пример 2"),
        (board1, "ABCB", False, "Пример 3"),
    ]
    
    # Создаём копии board для каждого теста, так как решение изменяет board
    def copy_board(board):
        return [row[:] for row in board]
    
    passed = 0
    for i, (board, word, expected, desc) in enumerate(test_cases, 1):
        board_copy = copy_board(board)
        result = solution.exist(board_copy, word)
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}: word='{word}' → {result} (ожидалось {expected})")
        if result == expected:
            passed += 1

if __name__ == "__main__":
    test_exist()