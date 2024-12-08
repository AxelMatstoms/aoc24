def can_solve(cur, nums, idx, b=False):
    n = nums[idx]
    if idx == 0:
        return n == cur

    if cur < 0:
        return False

    if can_solve(cur - n, nums, idx - 1, b=b):
        return True

    if cur % n == 0 and can_solve(cur // n, nums, idx - 1, b=b):
        return True

    cur_str = str(cur)
    n_str = str(n)

    if b and cur_str.endswith(n_str):
        prefix = cur_str[: -len(n_str)]
        if prefix:
            return can_solve(int(prefix), nums, idx - 1, b=b)

    return False


def solve(path):
    with open(path) as f:
        eqs = []
        for line in f:
            res, xs = line.split(": ")
            res = int(res)
            xs = [int(x) for x in xs.split()]
            eqs.append((res, xs))

    a, b = 0, 0
    for res, nums in eqs:
        if can_solve(res, nums, len(nums) - 1):
            a += res
        if can_solve(res, nums, len(nums) - 1, b=True):
            b += res

    return a, b


def main():
    assert solve("example") == (3749, 11387)
    a, b = solve("input")
    print(a)
    print(b)


if __name__ == "__main__":
    main()
