from lab1.maze_solver import Maze_Solver


def test_maze_solver():
    labyrinth = [
        ['#', '.', '#', '#'],
        ['#', '.', '.', '#'],
        ['.', '#', '.', '#'],
        ['#', '.', '.', '.'],
    ]

    n = 4
    maze_solver = Maze_Solver(labyrinth, n)
    exit_point = (3, 3)

    assert maze_solver.query(0, 0, exit_point, n) == False
    assert maze_solver.query(2, 0, exit_point, n) == False
    assert maze_solver.query(2, 2, exit_point, n) == True


def test_maze_solver_big():
    n = 1920

    temp1 = ["."]
    temp2 = ["#"] * (n - 1)
    temp1.extend(temp2)
    labyrinth = [temp1] * n

    maze_solver = Maze_Solver(labyrinth, n)

    for i in range(1, 1920):
       assert maze_solver.query(0, 0, (n - i, 0), n) == True

