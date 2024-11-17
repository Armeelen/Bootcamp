matrix =[['7', 'i', 'i'], ['T', 's', 'x'], ['h', '%', '?'], ['i', ' ', '#'], ['s', 'M', ' '], ['$', 'a', ' '], ['#', 't', '%'], ['^','r','!'] ]

def search_matrix(matrix):
    colums = len(matrix[0])
    rows = len(matrix)
    
    for row in matrix:
        print(''.join(row))
search_matrix(matrix)