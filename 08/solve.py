import itertools
import collections


def solve_p1(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    antennas = collections.defaultdict(list)
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch.isalnum():
                antennas[ch].append((x, y))

    w, h = len(grid[0]), len(grid)
    antinodes = set()
    for ants in antennas.values():
        for p1, p2 in itertools.combinations(ants, 2):
            x1, y1 = p1
            x2, y2 = p2

            dx, dy = x2 - x1, y2 - y1

            ax1, ay1 = x2 + dx, y2 + dy
            ax2, ay2 = x1 - dx, y1 - dy

            if ax1 >= 0 and ax1 < w and ay1 >= 0 and ay1 < h:
                antinodes.add((ax1, ay1))

            if ax2 >= 0 and ax2 < w and ay2 >= 0 and ay2 < h:
                antinodes.add((ax2, ay2))

    return len(antinodes)


def solve_p2(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    antennas = collections.defaultdict(list)
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch.isalnum():
                antennas[ch].append((x, y))

    w, h = len(grid[0]), len(grid)
    antinodes = set()
    for ants in antennas.values():
        for p1, p2 in itertools.combinations(ants, 2):
            x1, y1 = p1
            x2, y2 = p2

            dx, dy = x2 - x1, y2 - y1

            i = 0

            while True:
                ax1, ay1 = x1 + dx * i, y1 + dy * i
                ax2, ay2 = x1 - dx * i, y1 - dy * i

                out = 0
                if ax1 >= 0 and ax1 < w and ay1 >= 0 and ay1 < h:
                    antinodes.add((ax1, ay1))
                else:
                    out += 1

                if ax2 >= 0 and ax2 < w and ay2 >= 0 and ay2 < h:
                    antinodes.add((ax2, ay2))
                else:
                    out += 1

                if out == 2:
                    break

                i += 1

    return len(antinodes)


def main():
    assert solve_p1("example") == 14
    print(solve_p1("input"))

    assert solve_p2("example") == 34
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
