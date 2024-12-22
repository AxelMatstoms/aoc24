import collections


def solve_p1(path):
    with open(path) as f:
        nums = [int(x) for x in f.read().splitlines()]

    res = 0
    for init in nums:
        secret = init
        for _ in range(2000):
            secret ^= secret << 6
            secret &= 0xffffff

            secret ^= secret >> 5
            secret &= 0xffffff

            secret ^= secret << 11
            secret &= 0xffffff
        res += secret

    return res


def solve_p2(path):
    with open(path) as f:
        nums = [int(x) for x in f.read().splitlines()]

    res = 0
    scores = collections.Counter()
    for init in nums:
        secret = init
        suffix = tuple()
        last = init % 10
        buyer_score = collections.Counter()

        for _ in range(2000):
            secret ^= secret << 6
            secret &= 0xffffff

            secret ^= secret >> 5
            secret &= 0xffffff

            secret ^= secret << 11
            secret &= 0xffffff
            digit = secret % 10

            delta = digit - last
            last = digit

            suffix = (*suffix, delta)
            if len(suffix) > 4:
                suffix = suffix[1:]
            else:
                continue

            if suffix not in buyer_score:
                buyer_score[suffix] = digit

        scores += buyer_score

    res = max(scores.values())

    return res


def main():
    assert solve_p1("example") == 37327623
    print(solve_p1("input"))

    assert solve_p2("example2") == 23
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
