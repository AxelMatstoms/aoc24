from functools import cache


@cache
def dp(stone, n):
    if n == 0:
        return 1

    if stone == 0:
        return dp(1, n - 1)

    sstone = str(stone)
    if len(sstone) % 2 == 0:
        mid = len(sstone) // 2
        return dp(int(sstone[:mid]), n - 1) + dp(int(sstone[mid:]), n - 1)

    return dp(2024 * stone, n - 1)


def solve(path):
    with open(path) as f:
        stones = [int(x) for x in f.read().strip().split()]

    a = sum(dp(stone, 25) for stone in stones)
    b = sum(dp(stone, 75) for stone in stones)

    return a, b


def main():
    assert solve("example")[0] == 55312

    a, b = solve("input")
    print(a)
    print(b)


if __name__ == "__main__":
    main()
