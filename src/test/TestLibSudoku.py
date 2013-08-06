'''
Created on 26/07/2013

@author: dominik
'''
import unittest
from lib.libSudoku import get_new_board, is_board_valid


class Test(unittest.TestCase):

    def testBoardCreationAndValidation(self):
        for i in range(1,100):
            newBoard = get_new_board()
            self.assertTrue(is_board_valid(newBoard), "newly created board is not valid")

        newBoard = get_new_board()
        newBoard[0][0] = newBoard[2][2]
        self.assertFalse(is_board_valid(newBoard), "invalid board deemed to be valid - group")
        newBoard= get_new_board()
        newBoard[0][8] = newBoard[0][0]
        self.assertFalse(is_board_valid(newBoard), "invalid board deemed to be valid - row") 
        newBoard= get_new_board()
        newBoard[8][8] = newBoard[0][8]
        self.assertFalse(is_board_valid(newBoard), "invalid board deemed to be valid - col") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()