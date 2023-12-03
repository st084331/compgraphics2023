from lab1.maze_solver import Maze_Solver

def generate_maze_cell(i, j, n):
    # Placeholder function for maze cell generation
    return '.' if i < n / 2 else '#'

def test_maze_solver():
    labyrinth = [
        ['#', '.', '#', '#'],
        ['#', '.', '.', '#'],
        ['.', '#', '.', '#'],
        ['#', '.', '.', '.'],
    ]

    n = 4
    maze_solver = Maze_Solver(n)

    for i in range(n):
        for j in range(n):
            if i + 1 < n and labyrinth[i][j] == labyrinth[i + 1][j] == '.':
                maze_solver.dsu.union(maze_solver.index(i, j), maze_solver.index(i + 1, j))
            if j + 1 < n and labyrinth[i][j + 1] == labyrinth[i][j] == '.':
                maze_solver.dsu.union(maze_solver.index(i, j), maze_solver.index(i, j + 1))

    exit_point = (3, 3)
    assert maze_solver.query(0, 0, exit_point[0], exit_point[1]) == False
    assert maze_solver.query(2, 0, exit_point[0], exit_point[1]) == False
    assert maze_solver.query(2, 2, exit_point[0], exit_point[1]) == True


def test_maze_solver_big():
    n = 1000000
    maze_solver = Maze_Solver(n)

    for i in range(n):
        for j in range(n):
            cell = generate_maze_cell(i, j, n)
            if i + 1 < n and cell == generate_maze_cell(i + 1, j, n) == '.':
                maze_solver.dsu.union(maze_solver.index(i, j), maze_solver.index(i + 1, j))
            if j + 1 < n and cell == generate_maze_cell(i, j + 1, n) == '.':
                maze_solver.dsu.union(maze_solver.index(i, j), maze_solver.index(i, j + 1))

    assert maze_solver.query(0, 0, 999999, 999999)
