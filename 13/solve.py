def solve_p1(path):
    with open(path) as f:
        inp = f.read()

    blocks = inp.split("\n\n")

    syss = []
    for block in blocks:
        eqsys = {}

        for line in block.strip().split("\n"):
            label, rest = line.split(": ")
            x, y = rest.split(", ")
            eqsys[label] = (int(x[2:]), int(y[2:]))

        syss.append(eqsys)

    res = 0
    for sys in syss:
        x1, y1 = sys["Button A"]
        x2, y2 = sys["Button B"]
        xs, ys = sys["Prize"]

        best = (200, 200)
        win = False
        for a in range(100):
            for b in range(100):
                if a * x1 + b * x2 == xs and a * y1 + b * y2 == ys:
                    win = True
                    best = min(best, (a, b), key=lambda ab: 3 * ab[0] + ab[1])

        if win:
            res += 3 * best[0] + best[1]

    return res


def solve_p2(path, ofs=10000000000000):
    with open(path) as f:
        inp = f.read()

    blocks = inp.split("\n\n")

    syss = []
    for block in blocks:
        eqsys = {}

        for line in block.strip().split("\n"):
            label, rest = line.split(": ")
            x, y = rest.split(", ")
            eqsys[label] = (int(x[2:]), int(y[2:]))

        syss.append(eqsys)

    res = 0
    for sys in syss:
        ax, ay = sys["Button A"]
        bx, by = sys["Button B"]
        xs, ys = sys["Prize"]
        xs += ofs
        ys += ofs

        d = ax * by - ay * bx

        a = xs * by - bx * ys
        b = ax * ys - xs * ay

        if a % d == 0 and b % d == 0:
            aa = a // d
            bb = b // d
            res += 3 * aa + bb

    return res


def main():
    assert solve_p1("example") == 480
    print(solve_p1("input"))

    assert solve_p2("example", ofs=0) == 480
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
