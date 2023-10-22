class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n * n)]
        self.rank = [0] * (n * n)

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                root1, root2 = root2, root1
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1


def index(i, j, n):
    return i * n + j


def preprocess(labyrinth, n):
    dsu = DSU(n)
    for i in range(n):
        for j in range(n):
            if i + 1 < n and labyrinth[i + 1][j] == labyrinth[i][j] == '.':
                dsu.union(index(i, j, n), index(i + 1, j, n))
            if j + 1 < n and labyrinth[i][j + 1] == labyrinth[i][j] == '.':
                dsu.union(index(i, j, n), index(i, j + 1, n))
    return dsu


def query(dsu, x, y, exit_point, n):
    return dsu.find(index(x, y, n)) == dsu.find(index(exit_point[0], exit_point[1], n))


# Example:
labyrinth = [
    ['#', '.', '#', '#'],
    ['#', '.', '.', '#'],
    ['.', '#', '.', '#'],
    ['#', '.', '.', '.'],
]

n = 4
dsu = preprocess(labyrinth, n)
exit_point = (3, 3)

for x in range(n):
    for y in range(n):
        print(x, y, query(dsu, x, y, exit_point, n))
