from random import sample, choice, randint

_field_prototype = [
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [2, 3, 4, 5, 6, 7, 8, 9, 1],
         [5, 6, 7, 8, 9, 1, 2, 3, 4],
         [8, 9, 1, 2, 3, 4, 5, 6, 7],
         [3, 4, 5, 6, 7, 8, 9, 1, 2],
         [6, 7, 8, 9, 1, 2, 3, 4, 5],
         [9, 1, 2, 3, 4, 5, 6, 7, 8]]


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
def get_new_board():
    for i in range(100):
        _call_unpacked(_permute_rows, _get_random_group_pair())
        _call_unpacked(_permute_cols, _get_random_group_pair())
        _call_unpacked(_permute_group_rows, [ y * 3 for y in sample([0, 1, 2], 2) ])
        _call_unpacked(_permute_group_cols, [ x * 3 for x in sample([0, 1, 2], 2) ])
        _permute_inc_by(randint(1, 9))
        _call_unpacked(_swap_values, sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)[:2])
    return _field_prototype

def _is_row_valid(board, y):
    value_seen = [False] * 10
    for field in board[y]:
        if value_seen[field]: 
            return False
        else:
            value_seen[field] = True;
    return True

def _is_col_valid(board, x):
    value_seen = [False] * 10
    for row in board:
        if value_seen[row[x]]:
            return False
        else:
            value_seen[row[x]] = True;
    return True

def _is_group_valid(board, groupx, groupy): 
    value_seen = [False] * 10 
    for x in range(0, 3):
        for y in range(0, 3):
            nextx = x + groupx;
            nexty = y + groupx;
            if value_seen[board[nextx][nexty]]:
                return False
        else:
            value_seen[board[nextx][nexty]] = True;
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
