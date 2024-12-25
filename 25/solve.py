import itertools


def solve_p1(path):
    with open(path) as f:
        grids = f.read().split("\n\n")

    keys = []
    locks = []

    for grid in grids:
        grid = grid.splitlines()
        if grid[0].count(".") == len(grid[0]):  # key
            key = []
            for x in range(len(grid[0])):
                h = next(y for y in range(len(grid) - 1) if grid[y + 1][x] == "#")
                key.append(len(grid) - 2 - h)
            keys.append(key)
        else:  # lock
            lock = []
            for x in range(len(grid[0])):
                h = next(y for y in range(len(grid) - 1) if grid[y + 1][x] == ".")
                lock.append(h)
            locks.append(lock)

    res = 0
    for lock, key in itertools.product(keys, locks):
        res += all(pin + bump <= 5 for pin, bump in zip(lock, key))

    return res


def main():
    assert solve_p1("example") == 3
    print(solve_p1("input"))


if __name__ == "__main__":
    main()
