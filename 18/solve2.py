"""For part 2, we can use the union-find data
structure to speed up checking connectivity."""

from collections import deque


def solve_p1(path, size=70, n=1024):
    mem = []
    with open(path) as f:
        for line in f:
            mem.append(tuple(int(x) for x in line.split(",")))

    grid = [["."] * (size + 1) for _ in range(size + 1)]
    for x, y in mem[:n]:
        grid[y][x] = "#"

    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visited = {(0, 0)}
    to_visit = deque([(0, 0, 0)])

    while to_visit:
        cost, x, y = to_visit.popleft()

        if (x, y) == (size, size):
            return cost

        for dx, dy in DELTA:
            xx, yy = x + dx, y + dy
            new_cost = cost + 1
            if yy < 0 or yy > size or xx < 0 or xx > size:
                continue

            if grid[yy][xx] != "#" and (xx, yy) not in visited:
                to_visit.append((new_cost, xx, yy))
                visited.add((xx, yy))

    print("bad")


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find_set(self, key):
        if key not in self.parent:
            self.parent[key] = key
            self.rank[key] = 0
            return key

        root = key
        while (new_root := self.parent[root]) != root:
            root = new_root

        while (parent := self.parent[key]) != root:
            self.parent[key] = root
            key = parent

        return root

    def union_set(self, x, y):
        x = self.find_set(x)
        y = self.find_set(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


def solve_p2(path, size=70):
    mem = []
    with open(path) as f:
        for line in f:
            mem.append(tuple(int(x) for x in line.split(",")))

    grid = [["."] * (size + 1) for _ in range(size + 1)]
    for x, y in mem:
        grid[y][x] = "#"

    connected = UnionFind()
    for y in range(size + 1):
        for x in range(size + 1):
            if grid[y][x] == "#":
                continue

            if x + 1 <= size and grid[y][x + 1] == ".":
                connected.union_set((x, y), (x + 1, y))

            if y + 1 <= size and grid[y + 1][x] == ".":
                connected.union_set((x, y), (x, y + 1))

    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for cx, cy in reversed(mem):
        grid[cy][cx] = "."

        for dx, dy in DELTA:
            xx, yy = cx + dx, cy + dy
            if yy < 0 or yy > size or xx < 0 or xx > size:
                continue

            if grid[yy][xx] == ".":
                connected.union_set((cx, cy), (xx, yy))

        if connected.find_set((0, 0)) == connected.find_set((size, size)):
            return f"{cx},{cy}"


def main():
    assert solve_p1("example", size=6, n=12) == 22
    print(solve_p1("input"))

    assert solve_p2("example", size=6) == "6,1"
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
