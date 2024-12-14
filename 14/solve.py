def solve_p1(path, w=101, h=103):
    robots = []
    with open(path) as f:
        for line in f:
            p, v = line.split(" ")
            p = [int(x) for x in p.split("=")[1].split(",")]
            v = [int(x) for x in v.split("=")[1].split(",")]

            robots.append([*p, *v])

    for _ in range(100):
        for robot in robots:
            x, y, vx, vy = robot

            robot[:2] = ((x + vx) % w, (y + vy) % h)

    q = [[0, 0], [0, 0]]
    for x, y, vx, vy in robots:
        if x == w // 2 or y == h // 2:
            continue

        qx = x > w // 2
        qy = y > h // 2

        q[qy][qx] += 1

    return q[0][0] * q[0][1] * q[1][0] * q[1][1]


def print_grid(robots, w, h):
    grid = [[" "] * w for _ in range(h)]

    for x, y, dx, dy in robots:
        grid[y][x] = "*"

    for line in grid:
        print("".join(line))


def solve_p2(path, w=101, h=103):
    robots = []
    with open(path) as f:
        for line in f:
            p, v = line.split(" ")
            p = [int(x) for x in p.split("=")[1].split(",")]
            v = [int(x) for x in v.split("=")[1].split(",")]

            robots.append([*p, *v])

    def min_dists(robots, w, h):
        grid = [[0] * w for _ in range(h)]

        for x, y, dx, dy in robots:
            grid[y][x] = 1

        s = 0
        DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y, _, _ in robots:
            close = False
            for dx, dy in DELTA:
                xx = x + dx
                yy = y + dy
                if xx < 0 or xx >= w or yy < 0 or yy >= h:
                    continue

                if grid[yy][xx] == 1:
                    close = True
                    break
            s += close

        return s

    for t in range(w * h):
        for robot in robots:
            x, y, vx, vy = robot

            robot[:2] = ((x + vx) % w, (y + vy) % h)

        # if min_dists(robots) <= thresh:
        q = [[0, 0], [0, 0]]
        for x, y, vx, vy in robots:
            if x == w // 2 or y == h // 2:
                continue

            qx = x > w // 2
            qy = y > h // 2

            q[qy][qx] += 1

        if min_dists(robots, w, h) > 300:
            print_grid(robots, w, h)
            return t + 1


def main():
    print(solve_p1("input"))

    print(solve_p2("input"))


if __name__ == "__main__":
    main()
