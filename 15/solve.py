def solve_p1(path):
    with open(path) as f:
        grid, moves = f.read().split("\n\n")
        grid = [list(line.strip()) for line in grid.split("\n")]
        moves = "".join(line.strip() for line in moves)

    x, y = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "@"
    )
    DELTA = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}

    def push(x, y, dx, dy):
        nx = x
        ny = y
        while True:
            nx += dx
            ny += dy

            if grid[ny][nx] == "#":
                return False

            if grid[ny][nx] == ".":
                grid[ny][nx] = "O"
                grid[y][x] = "."
                return True

    for i, move in enumerate(moves):
        dx, dy = DELTA[move]
        xx, yy = x + dx, y + dy

        if grid[yy][xx] == "O" and push(xx, yy, dx, dy):
            grid[y][x] = "."
            grid[yy][xx] = "@"
            x, y = xx, yy

        if grid[yy][xx] == ".":
            grid[y][x] = "."
            grid[yy][xx] = "@"
            x, y = xx, yy

    res = 0
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == "O":
                res += 100 * y + x
    return res


def solve_p2(path):
    with open(path) as f:
        grid, moves = f.read().split("\n\n")
        grid = [
            list(
                row.strip()
                .replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
            for row in grid.split("\n")
        ]
        moves = "".join(line.strip() for line in moves)

    x, y = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "@"
    )
    DELTA = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}

    def push(x, y, dx, dy):
        q = [(x, y)]
        to_push = []
        mark_empty = []
        visited = set()
        while q:
            x, y = q.pop()

            xx, yy = x + dx, y + dy
            if grid[yy][xx] == "#":
                return False

            if grid[yy][xx] == ".":
                to_push.append((xx, yy, grid[y][x]))
            elif (xx, yy) not in visited:
                q.append((xx, yy))
                to_push.append((xx, yy, grid[y][x]))
                visited.add((xx, yy))

            if dy:
                if grid[y][x] == "[":
                    xx = x + 1
                    assert grid[y][xx] == "]"
                else:
                    xx = x - 1
                    assert grid[y][xx] == "["

                yy = y + dy
                mark_empty.append((xx, y))
                if grid[yy][xx] == "#":
                    return False

                if grid[yy][xx] == ".":
                    to_push.append((xx, yy, grid[y][xx]))
                elif (xx, yy) not in visited:
                    q.append((xx, yy))
                    to_push.append((xx, yy, grid[y][xx]))
                    visited.add((xx, yy))

        for x, y in mark_empty:
            grid[y][x] = "."

        for x, y, new in to_push:
            grid[y][x] = new

        return True

    for i, move in enumerate(moves):
        dx, dy = DELTA[move]
        xx, yy = x + dx, y + dy

        if grid[yy][xx] in "[]" and push(xx, yy, dx, dy):
            grid[y][x] = "."
            grid[yy][xx] = "@"
            x, y = xx, yy

        if grid[yy][xx] == ".":
            grid[y][x] = "."
            grid[yy][xx] = "@"
            x, y = xx, yy

    res = 0
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == "[":
                res += 100 * y + x
    return res


def main():
    assert solve_p1("example") == 10092
    print(solve_p1("input"))

    assert solve_p2("example") == 9021
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
