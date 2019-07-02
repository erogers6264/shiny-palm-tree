correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:

def contains_one_to_n(numlist, n):
    numlist_copy = numlist.copy()
    if len(numlist_copy) != n:
        return False
    for i in range(1, n+1):
        try:
            numlist_copy.remove(i)
        except ValueError:
            return False
        
    if not numlist_copy:
        return True
    else:
        return False


def check_sudoku(square):
    is_valid = True
    n = len(square[0])
    
    # check rows:
    for row in square:
        if not contains_one_to_n(row, n):
            is_valid = False
    
    # check columns:
    for col in range(n):
        column = [row[col] for row in square]
        if not contains_one_to_n(column, n):
            is_valid = False
    
    return is_valid


    
    
print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False


