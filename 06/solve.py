def solve_p1(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    pos = next((x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "^")
    facing = (0, -1)
    w, h = len(grid[0]), len(grid)

    visited = set()

    def in_bounds(x, y):
        return x >= 0 and x < w and y >= 0 and y < h

    while True:
        nx, ny = pos[0] + facing[0], pos[1] + facing[1]
        visited.add(pos)

        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            break

        if grid[ny][nx] == "#":
            facing = (-facing[1], facing[0])
        else:
            pos = (nx, ny)

    return len(visited)


def solve_p2(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    pos = next((x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "^")
    facing = (0, -1)
    w, h = len(grid[0]), len(grid)

    to_check = set()
    while True:
        nx, ny = pos[0] + facing[0], pos[1] + facing[1]

        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            break

        to_check.add((nx, ny))

        if grid[ny][nx] == "#":
            facing = (-facing[1], facing[0])
        else:
            pos = (nx, ny)

    def causes_loop(pos, facing, new):
        vv = set()
        while True:
            if (pos, facing) in vv:
                return True

            vv.add((pos, facing))

            nx, ny = pos[0] + facing[0], pos[1] + facing[1]

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                return False

            new_facing = (-facing[1], facing[0])
            if grid[ny][nx] == "#" or (nx, ny) == new:
                facing = new_facing
            else:
                pos = (nx, ny)

    # ŕeset pos, facing
    start = next((x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "^")
    facing = (0, -1)

    loop = 0
    for pos in to_check:
        if pos != start and causes_loop(start, facing, pos):
            loop += 1

    return loop


def main():
    assert solve_p1("example") == 41
    print(solve_p1("input"))

    assert solve_p2("example") == 6
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
