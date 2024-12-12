def solve_p1(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    w, h = len(grid[0]), len(grid)

    visited = set()

    def visit_region(seed_x, seed_y):
        reg_type = grid[seed_y][seed_x]
        reg = {(seed_x, seed_y)}
        visited.add((seed_x, seed_y))

        q = [(seed_x, seed_y)]
        while q:
            x, y = q.pop()

            for dx, dy in DELTA:
                xx, yy = x + dx, y + dy

                if (
                    0 <= xx < w
                    and 0 <= yy < h
                    and (xx, yy) not in visited
                    and grid[yy][xx] == reg_type
                ):
                    visited.add((xx, yy))
                    reg.add((xx, yy))
                    q.append((xx, yy))

        return reg

    regs = []

    for y in range(h):
        for x in range(w):
            if (x, y) not in visited:
                reg = visit_region(x, y)
                regs.append(reg)

    def perimeter(reg):
        perim = 0
        for x, y in reg:
            for dx, dy in DELTA:
                s = (x + dx, y + dy)
                if s not in reg:
                    perim += 1

        return perim

    res = 0
    for reg in regs:
        cost = len(reg) * perimeter(reg)
        res += cost

    return res


def solve_p2(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    w, h = len(grid[0]), len(grid)

    visited = set()

    def visit_region(seed_x, seed_y):
        reg_type = grid[seed_y][seed_x]
        reg = {(seed_x, seed_y)}
        visited.add((seed_x, seed_y))

        q = [(seed_x, seed_y)]
        while q:
            x, y = q.pop()

            for dx, dy in DELTA:
                xx, yy = x + dx, y + dy

                if (
                    0 <= xx < w
                    and 0 <= yy < h
                    and (xx, yy) not in visited
                    and grid[yy][xx] == reg_type
                ):
                    visited.add((xx, yy))
                    reg.add((xx, yy))
                    q.append((xx, yy))

        return reg

    regs = []

    for y in range(h):
        for x in range(w):
            if (x, y) not in visited:
                reg = visit_region(x, y)
                regs.append(reg)

    def perimeter(reg):
        perim = set()
        for x, y in reg:
            for dx, dy in DELTA:
                s = (x + dx, y + dy)
                if s not in reg:
                    perim.add((x, y, dx, dy))

        covered = set()
        sections = 0
        for x, y, dx, dy in perim:
            if (x, y, dx, dy) in covered:
                continue

            # flood fill section
            q = [(x, y)]
            covered.add((x, y, dx, dy))
            sections += 1
            while q:
                xx, yy = q.pop()

                for dx2, dy2 in DELTA:
                    x3, y3 = xx + dx2, yy + dy2
                    nxt = (x3, y3, dx, dy)
                    if nxt in perim and nxt not in covered:
                        covered.add((x3, y3, dx, dy))
                        q.append((x3, y3))

        return sections

    res = 0
    for reg in regs:
        cost = len(reg) * perimeter(reg)
        res += cost

    return res


def main():
    assert solve_p1("example") == 1930
    print(solve_p1("input"))

    assert solve_p2("example") == 1206
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
