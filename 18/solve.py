from collections import deque, defaultdict

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


def solve_p2(path, size=70):
    mem = []
    with open(path) as f:
        for line in f:
            mem.append(tuple(int(x) for x in line.split(",")))

    grid = [["."] * (size + 1) for _ in range(size + 1)]

    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for cx, cy in mem:
        grid[cy][cx] = "#"
        visited = {(0, 0)}
        to_visit = deque([(0, 0, 0)])
        ok = False
        while to_visit:
            cost, x, y = to_visit.popleft()

            if (x, y) == (size, size):
                ok = True
                break

            for dx, dy in DELTA:
                xx, yy = x + dx, y + dy
                new_cost = cost + 1
                if yy < 0 or yy > size or xx < 0 or xx > size:
                    continue

                if grid[yy][xx] != "#" and (xx, yy) not in visited:
                    to_visit.append((new_cost, xx, yy))
                    visited.add((xx, yy))

        if not ok:
            return f"{cx},{cy}"


def main():
    assert solve_p1("example", size=6, n=12) == 22
    print(solve_p1("input"))

    assert solve_p2("example", size=6) == "6,1"
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
