import functools


def solve_p1(path):
    rules = []
    updates = []
    with open(path) as f:
        itr = iter(f)
        for line in itr:
            if "|" not in line:
                break

            l, r = line.strip().split("|")
            rules.append((int(l), int(r)))

        for line in itr:
            updates.append([int(x) for x in line.strip().split(",")])

    print("n rules:", len(rules))
    print("n unique", len(set(x for update in updates for x in update)))

    res = 0
    for update in updates:
        indices = {v: i for i, v in enumerate(update)}
        correct = not any(
            left in indices and right in indices and indices[left] > indices[right]
            for left, right in rules
        )

        if correct:
            res += update[len(update) // 2]

    return res


def solve_p2(path):
    rules = set()
    updates = []
    with open(path) as f:
        itr = iter(f)
        for line in itr:
            if "|" not in line:
                break

            l, r = line.strip().split("|")
            rules.add((int(l), int(r)))

        for line in itr:
            updates.append([int(x) for x in line.strip().split(",")])

    res = 0

    def comp(left, right):
        if (left, right) in rules:
            return -1
        if (right, left) in rules:
            return 1
        return 0

    for update in updates:
        indices = {v: i for i, v in enumerate(update)}
        correct = not any(
            left in indices and right in indices and indices[left] > indices[right]
            for left, right in rules
        )

        if not correct:
            update.sort(key=functools.cmp_to_key(comp))
            res += update[len(update) // 2]

    return res


def main():
    assert solve_p1("example") == 143
    print(solve_p1("input"))

    assert solve_p2("example") == 123
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
