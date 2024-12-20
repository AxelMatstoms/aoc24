def solve_p1(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    start = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "S"
    )
    w, h = len(grid[0]), len(grid)

    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dist = {start: 0}
    to_visit = [(0, start)]

    while to_visit:
        cost, (x, y) = to_visit.pop()

        for dx, dy in DELTA:
            xx, yy = x + dx, y + dy
            new_cost = cost + 1
            key = (xx, yy)
            if xx < 0 or xx >= w or yy < 0 or yy >= h:
                continue

            if grid[yy][xx] != "#" and (key not in dist or dist[key] > new_cost):
                to_visit.append((new_cost, (xx, yy)))
                dist[key] = new_cost

    CHEAT_DELTA = [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    res = 0
    for sy in range(h):
        for sx in range(w):
            for dx, dy in CHEAT_DELTA:
                ex, ey = sx + dx, sy + dy

                if ex < 0 or ex >= w or ey < 0 or ey >= h:
                    continue

                if grid[ey][ex] == "#":
                    continue

                if grid[sy][sx] == "#":
                    continue

                delta_cost = dist[(ex, ey)] - dist[(sx, sy)] - 2
                if delta_cost >= 100:
                    res += 1

    return res


def solve_p2(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    start = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "S"
    )
    w, h = len(grid[0]), len(grid)

    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dist = {start: 0}
    to_visit = [(0, start)]

    while to_visit:
        cost, (x, y) = to_visit.pop()

        for dx, dy in DELTA:
            xx, yy = x + dx, y + dy
            new_cost = cost + 1
            key = (xx, yy)
            if xx < 0 or xx >= w or yy < 0 or yy >= h:
                continue

            if grid[yy][xx] != "#" and (key not in dist or dist[key] > new_cost):
                to_visit.append((new_cost, (xx, yy)))
                dist[key] = new_cost

    res = 0
    for sy in range(h):
        for sx in range(w):
            for dy in range(-20, 21):
                for dx in range(-20, 21):
                    d = abs(dy) + abs(dx)
                    if d > 20:
                        continue

                    ex, ey = sx + dx, sy + dy

                    if ex < 0 or ex >= w or ey < 0 or ey >= h:
                        continue

                    if grid[ey][ex] == "#":
                        continue

                    if grid[sy][sx] == "#":
                        continue

                    delta_cost = dist[(ex, ey)] - dist[(sx, sy)] - d

                    if delta_cost >= 100:
                        res += 1

    return res


def main():
    # assert solve_p1("example") == ...
    print(solve_p1("input"))

    # assert solve_p2("example") == ...
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
