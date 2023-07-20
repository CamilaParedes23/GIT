def solve_n_queens(n):
    solutions = []
    board = [[0] * n for _ in range(n)]
    backtrack(board, 0, solutions)
    return solutions


def backtrack(board, col, solutions):
    if col == len(board):
        solutions.append(create_solution(board))
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            backtrack(board, col + 1, solutions)
            board[row][col] = 0


def is_safe(board, row, col):
    # Verificar si hay una reina en la misma fila
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Verificar si hay una reina en la misma diagonal superior
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verificar si hay una reina en la misma diagonal inferior
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def create_solution(board):
    solution = []
    for row in board:
        queen_col = row.index(1)
        solution.append(queen_col)
    return solution


def print_board(board):
    for row in board:
        for val in row:
            print(val, end=' ')
        print()


# Ejemplo de uso
n = 4

solutions = solve_n_queens(n)

print(f"Soluciones para {n} reinas:")
for solution in solutions:
    print_board([[1 if col == queen_col else 0 for col in range(n)] for queen_col in solution])
    print()
