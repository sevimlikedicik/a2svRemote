class Solution(object):
    def isValidSudoku(self, board):
        return self.checkSquares(board) and self.checkRows(board) and self.checkColumns(board)

    def checkSquares(self, board):
        return self.checkNumbers(board, 0, 0, 2, 2) and self.checkNumbers(board, 0, 3, 2, 5) and self.checkNumbers(
            board, 0, 6, 2, 8) and self.checkNumbers(board, 3, 0, 5, 2) and self.checkNumbers(board, 3, 3, 5,
                                                                                              5) and self.checkNumbers(
            board, 3, 6, 5, 8) and self.checkNumbers(board, 6, 0, 8, 2) and self.checkNumbers(board, 6, 3, 8,
                                                                                              5) and self.checkNumbers(
            board, 6, 6, 8, 8)

    def checkRows(self, board):
        for i in range(0, 9):
            if not self.checkNumbers(board, i, 0, i, 8):
                return False

        return True

    def checkColumns(self, board):
        for i in range(0, 9):
            if not self.checkNumbers(board, 0, i, 8, i):
                return False

        return True

    def checkNumbers(self, board, x1, y1, x2, y2):
        numbers = set()
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if num in numbers:
                        return False
                    numbers.add(num)
        return True
