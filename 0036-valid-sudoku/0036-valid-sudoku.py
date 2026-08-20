class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        dicFilas = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

        dicColumnas = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

        dicBloques = {
            (0, 0): [],
            (0, 1): [],
            (0, 2): [],
            (1, 0): [],
            (1, 1): [],
            (1, 2): [],
            (2, 0): [],
            (2, 1): [],
            (2, 2): []
        }

        subTablas = {
            
        }

        for i in range (9):
            for j in range (9):
                if (board[i][j] in dicFilas[i] or board[i][j] in dicColumnas[j] or board[i][j] in dicBloques[(i//3, j//3)]):
                    return False
                if (board[i][j]!= '.'):
                    dicFilas[i].append(board[i][j])
                    dicColumnas[j].append(board[i][j])
                    dicBloques[(i//3),(j//3)].append(board[i][j])

        return True