class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
            return u

        # Iterative path compression
        stack = []
        while u != self.parent[u]:
            stack.append(u)
            u = self.parent[u]
        for v in stack:
            self.parent[v] = u
        return u

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v


class Maze_Solver:
    def __init__(self, n):
        self.dsu = DSU()
        self.n = n

    def process_path(self, labyrinth):
        for i in range(self.n):
            for j in range(self.n):
                if i + 1 < self.n and labyrinth(i, j) == labyrinth(i + 1, j) == '.':
                    self.dsu.union(self.index(i, j), self.index(i + 1, j))
                if j + 1 < self.n and labyrinth(i, j) == labyrinth(i, j + 1) == '.':
                    self.dsu.union(self.index(i, j), self.index(i, j + 1))

    def query(self, x, y, exit_x, exit_y):
        return self.dsu.find(self.index(x, y)) == self.dsu.find(self.index(exit_x, exit_y))

    def index(self, i, j):
        return i * self.n + j
