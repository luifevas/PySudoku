from random import sample, choice, randint
from copy import deepcopy

__table_cache = {}

_field_prototype = [
         [1, 2, 3,  4, 5, 6,  7, 8, 9],
         [4, 5, 6,  7, 8, 9,  1, 2, 3],
         [7, 8, 9,  1, 2, 3,  4, 5, 6],
         
         [2, 3, 4,  5, 6, 7,  8, 9, 1],
         [5, 6, 7,  8, 9, 1,  2, 3, 4],
         [8, 9, 1,  2, 3, 4,  5, 6, 7],
         
         [3, 4, 5,  6, 7, 8,  9, 1, 2],
         [6, 7, 8,  9, 1, 2,  3, 4, 5],
         [9, 1, 2,  3, 4, 5,  6, 7, 8]]


def _permute_rows(y1, y2):
    tmp = _field_prototype[y1]
    _field_prototype[y1] = _field_prototype[y2]
    _field_prototype[y2] = tmp;
    
def _permute_cols(x1, x2):
    for i, tmp in enumerate(_field_prototype[x1]):
        _field_prototype[x1][i] = _field_prototype[x2][i]
        _field_prototype[x1][i] = tmp
            
def _permute_group_rows(y1, y2):
    for i in range(3):
        _permute_rows(y1 + i, y2 + i)
        
def _permute_group_cols(x1, x2):
    for i in range(3):
        _permute_rows(x1 + i, x2 + i)

def _permute_inc_by(n):
    for i, row in enumerate(_field_prototype):
        for j, field in enumerate(row):
            _field_prototype[i][j] = ((field + n - 1) % 9 + 1);
       
def _swap_values(v1, v2):
    for i, row in enumerate(_field_prototype):
        for j, field in enumerate(row):
            if field == v1:
                _field_prototype[i][j] = v2;
            elif field == v2:
                _field_prototype[i][j] = v1;

""" wrapper function 

    lets me call any function with a list of arguments instead
    heaving to pass each one individually. This can safe a lot of 
    time/code.
"""
def _call_unpacked(f, args):
    f(*args)
                
def _get_random_group_pair():
    group = choice([0, 1, 2]) * 3
    xy = sample([0, 1, 2], 2)
    return [ c + group for c in xy ] 
    
""" Factory function to create board

    Creates fully populated valid Sudoku board. It does so by 
    permuting a valid protoype
"""
def get_new_board(level):
    while True:
        try:
            for i in range(100):
                _call_unpacked(_permute_rows, _get_random_group_pair())
                _call_unpacked(_permute_cols, _get_random_group_pair())
                _call_unpacked(_permute_group_rows, [ y * 3 for y in sample([0, 1, 2], 2) ])
                _call_unpacked(_permute_group_cols, [ x * 3 for x in sample([0, 1, 2], 2) ])
                _permute_inc_by(randint(1, 9))
                _call_unpacked(_swap_values, sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)[:2])
            return (deepcopy(_field_prototype), _digHoles(deepcopy(_field_prototype), level))
        except noFieldGeneratedException:
            a = "b" #dummy 

class noFieldGeneratedException(Exception):
    pass

def _digHoles(table, level):
    if ( level == "Easy"): return _digEasyHoles(table, 30, level)
    if ( level == "Medium"): return _digEasyHoles(table, 40, level)
    if ( level == "Hard"): return _digHardHoles(table, 40, level)

def _digEasyHoles(table, n, level):
    safeWholesToBeDug = n
    canBeDug = [];
    for i in range(0,9):
        canBeDug.append([True] * 9)
    endLessPrevention = 300;
    while n > 0 and endLessPrevention > 0:
        endLessPrevention -= 1
        x = randint(0,8)
        y = randint(0,8)
        if canBeDug[x][y]:
            canBeDug[x][y] = False
            safeValue = table[x][y]
            table[x][y] = -1
            if _hasUniqueSolution(table): n -= 1
            else: table[x][y] = safeValue

    if endLessPrevention > 0:
        return table
    raise noFieldGeneratedException()

def _digHardHoles(table, n, level):
    canBeDug = [];
    for i in range(0,9):
        canBeDug.append([True] * 9)
    for x in range(0,9):
        for y in range(0,9):
            if randint(0,n//2) == 1:
                x = randint(0,8)
                y = randint(0,8)
                while not canBeDug[x][y]:
                    x = x + 1
                    if x % 8 != 0:
                        x = x % 8
                        y = (y + 1) % 8 
            if canBeDug[x][y]:
                safeValue = table[x][y]
                canBeDug[x][y] = False
                table[x][y] = -1
                if _hasUniqueSolution(table):
                    n -= 1
                else: table[x][y] = safeValue
                if n < 1: return table
    raise noFieldGeneratedException()
            



def _hasUniqueSolution(origTable):
    noOfSolutions = _numberOfSolutions(origTable);
    return _numberOfSolutions(origTable) == 1

""" counts valid solutions until 2
    
    DFS Backtracking algorithm that tries to find out if there is more than
    one valid solution
"""
def _numberOfSolutions(origTable):
    numberOfSolutions = __table_cache.get(str(origTable))
    if numberOfSolutions != None: return numberOfSolutions
    toSolve = deepcopy(origTable)
    stillLooking = True
    for x, row in enumerate(toSolve):
        for y, field in enumerate(row):
            if ( field < 1 or field > 9 ):
                stillLooking = False
                break
        else: #is executed if we did not break
            continue
        break
    # We have a valid solution!
    if stillLooking:
        return 1
    numberOfSolutions = 0
    for v in range(1,10):
        toSolve[x][y] = v;
        if is_board_valid(toSolve):
            numberOfSolutions += _numberOfSolutions(toSolve)
            # let's do not continue looking for solutions
            if numberOfSolutions > 1:
                __table_cache[str(origTable)] = numberOfSolutions
                return numberOfSolutions
    __table_cache[str(origTable)] = numberOfSolutions
    return numberOfSolutions
    
def _isValidSudokuValue(v):
    return v >= 1 and v <= 9

def _is_row_valid(board, y):
    value_seen = [False] * 10
    for field in board[y]:
        if _isValidSudokuValue(field):
            if value_seen[field]: 
                return False
            else:
                value_seen[field] = True;
    return True

def _is_col_valid(board, x):
    value_seen = [False] * 10
    for row in board:
        field = row[x];
        if _isValidSudokuValue(field):
            if value_seen[field]:
                return False
            else:
                value_seen[field] = True;
    return True

def _is_group_valid(board, groupx, groupy): 
    value_seen = [False] * 10 
    for x in range(0, 3):
        for y in range(0, 3):
            nextx = x + groupx;
            nexty = y + groupx;
            field = board[nextx][nexty]
            if _isValidSudokuValue(field):
                if value_seen[field]:
                    return False
                else:
                    value_seen[field] = True;
    return True

def is_board_valid(board): 
    for i in range(0, 9):
        if not _is_row_valid(board, i) or not _is_col_valid(board, i):
            return False
    for i in range(0, 3):
        for j in range(0, 3):
            if not _is_group_valid(board, i * 3, j * 3):
                return False 
    return True

if __name__ == "__main__":
