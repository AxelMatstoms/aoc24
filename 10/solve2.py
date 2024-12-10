def score(grid, x0, y0, b=False):
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    w, h = len(grid[0]), len(grid)
    visited = {(x0, y0)}
    to_visit = [(x0, y0)]

    reachable = 0

    while to_visit:
        x, y = to_visit.pop()
        level = grid[y][x]

        if level == 9:
            reachable += 1

        for dx, dy in DELTAS:
            xx, yy = x + dx, y + dy

            if 0 <= xx < w and 0 <= yy < h and (b or (xx, yy) not in visited) and grid[yy][xx] == level + 1:
                to_visit.append((xx, yy))
                visited.add((xx, yy))

    return reachable


def solve(path):
    with open(path) as f:
        grid = [[int(ch) for ch in line.strip()] for line in f]

    res_a = 0
    res_b = 0
    for y, line in enumerate(grid):
        for x, s in enumerate(line):
            if s == 0:
                res_a += score(grid, x, y)
                res_b += score(grid, x, y, b=True)

    return res_a, res_b


def main():
    assert solve("example") == (36, 81)
    a, b = solve("input")
    print(a)
    print(b)


if __name__ == "__main__":
    main()
