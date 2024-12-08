def solve_p1(path):
    with open(path) as f:
        eqs = []
        for line in f:
            res, xs = line.split(": ")
            res = int(res)
            xs = [int(x) for x in xs.split()]
            eqs.append((res, xs))

    ans = 0
    for res, xs in eqs:
        for mask in range(2**(len(xs)-1)):
            actual = xs[0]
            for i, r in enumerate(xs[1:]):
                if mask & (1 << i):
                    actual *= r
                else:
                    actual += r

            if res == actual:
                ans += res
                break

    return ans


def solve_p2(path):
    with open(path) as f:
        eqs = []
        for line in f:
            res, xs = line.split(": ")
            res = int(res)
            xs = [int(x) for x in xs.split()]
            eqs.append((res, xs))

    ans = 0
    for res, xs in eqs:
        for mask in range(3**(len(xs)-1)):
            actual = xs[0]
            for i, r in enumerate(xs[1:]):
                dig = mask % 3
                mask //= 3
                if dig == 0:
                    actual *= r
                elif dig == 1:
                    actual += r
                else:
                    actual = int(f"{actual}{r}")

            if res == actual:
                ans += res
                break

    return ans


def main():
    assert solve_p1("example") == 3749
    print(solve_p1("input"))

    assert solve_p2("example") == 11387
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
