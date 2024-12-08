from collections import Counter


def solve_p1(path):
    with open(path) as f:
        lines = [[int(x) for x in line.split()] for line in f]
    left, right = zip(*lines)

    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))


def solve_p2(path):
    with open(path) as f:
        lines = [[int(x) for x in line.split()] for line in f]
    left, right = zip(*lines)

    counts = Counter(right)
    return sum(x * counts[x] for x in left)


def main():
    assert solve_p1("example") == 11
    print(solve_p1("input"))

    assert solve_p2("example") == 31
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
