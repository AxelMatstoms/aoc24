def solve_p1(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    tot = 0
    for line in grid:
        for x, _ in enumerate(line):
            tot += line[x:x+4] == "XMAS"
            tot += line[x:x+4] == "SAMX"

    transp = ["".join(col) for col in zip(*grid)]
    for line in transp:
        for x, _ in enumerate(line):
            tot += line[x:x+4] == "XMAS"
            tot += line[x:x+4] == "SAMX"

    for y in range(len(grid)-3):
        for x in range(len(grid[0])-3):
            diag = "".join(grid[y+d][x+d] for d in range(4))
            tot += diag == "XMAS"
            tot += diag == "SAMX"

    for y in range(len(grid)-3):
        for x in range(3, len(grid[0])):
            diag = "".join(grid[y+d][x-d] for d in range(4))
            tot += diag == "XMAS"
            tot += diag == "SAMX"

    return tot


def solve_p2(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    def is_xmas(sgrid):
        ok = ["MAS", "SAM"]
        diag1 = "".join(sgrid[d][d] for d in range(3))
        diag2 = "".join(sgrid[d][2-d] for d in range(3))

        return diag1 in ok and diag2 in ok

    tot = 0
    for y in range(len(grid)-2):
        for x in range(len(grid[0])-2):
            subgrid = [grid[yy][x:x+3] for yy in range(y, y+3)]
            tot += is_xmas(subgrid)

    return tot


def main():
    assert solve_p1("example2") == 4
    assert solve_p1("example") == 18
    print(solve_p1("input"))

    assert solve_p2("example") == 9
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
