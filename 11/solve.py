from collections import Counter


def solve_p1(path):
    with open(path) as f:
        stones = [int(x) for x in f.read().strip().split()]

    for _ in range(25):
        new_stones = []
        for n in stones:
            if n == 0:
                new_stones.append(1)
            elif len(str(n)) % 2 == 0:
                s = str(n)
                l, r = int(s[:len(s)//2]), int(s[len(s)//2:])
                new_stones.append(l)
                new_stones.append(r)
            else:
                new_stones.append(n * 2024)

        stones = new_stones

    return len(stones)


def solve_p2(path, loop=75):
    with open(path) as f:
        nums = [int(x) for x in f.read().strip().split()]

    counts = Counter(nums)

    for i in range(loop):
        new_counts = Counter()
        for n, count in counts.items():
            if n == 0:
                new_counts[1] += count
            elif len(str(n)) % 2 == 0:
                s = str(n)
                l, r = int(s[:len(s)//2]), int(s[len(s)//2:])
                new_counts[l] += count
                new_counts[r] += count
            else:
                new_counts[n * 2024] += count

        counts = new_counts

    return sum(counts.values())


def main():
    assert solve_p1("example") == 55312
    print(solve_p1("input"))

    assert solve_p2("example", loop=25) == 55312
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
