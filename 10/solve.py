def score(grid, x0, y0):
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

            if 0 <= xx < w and 0 <= yy < h and (xx, yy) not in visited and grid[yy][xx] == level + 1:
                to_visit.append((xx, yy))
                visited.add((xx, yy))

    return reachable


def solve_p1(path):
    with open(path) as f:
        grid = [[int(ch) for ch in line.strip()] for line in f]

    res = 0
    for y, line in enumerate(grid):
        for x, s in enumerate(line):
            if s == 0:
                res += score(grid, x, y)

    return res


def solve_p2(path):
    with open(path) as f:
        grid = [[int(ch) for ch in line.strip()] for line in f]

    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    w, h = len(grid[0]), len(grid)
    order = [(x, y) for x in range(w) for y in range(h)]
    order.sort(key=lambda xy: grid[xy[1]][xy[0]], reverse=True)
    score = [[0] * w for _ in range(h)]

    res = 0
    for x, y in order:
        level = grid[y][x]
        if level == 9:
            score[y][x] = 1
            continue

        for dx, dy in DELTAS:
            xx, yy = x + dx, y + dy

            if 0 <= xx < w and 0 <= yy < h and grid[yy][xx] == level + 1:
                score[y][x] += score[yy][xx]

        if level == 0:
            res += score[y][x]

    return res


def main():
    assert solve_p1("example") == 36
    print(solve_p1("input"))

    assert solve_p2("example") == 81
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
