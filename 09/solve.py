def solve_p1(path):
    with open(path) as f:
        sizes = [int(ch) for ch in f.read().strip()]

    file = True

    blocks = [-1] * sum(sizes)
    i = 0
    fd = 0
    for n in sizes:
        if file:
            blocks[i:i+n] = [fd] * n
            fd += 1

        i += n
        file = not file

    space = 0
    end = len(blocks) - 1

    while space < end:
        if blocks[end] == -1:
            end -= 1
            continue

        if blocks[space] != -1:
            space += 1
            continue

        blocks[space], blocks[end] = blocks[end], blocks[space]

    res = 0
    for i, block in enumerate(blocks):
        if block != -1:
            res += i * block

    return res


def solve_p2(path):
    with open(path) as f:
        sizes = [int(ch) for ch in f.read().strip()]

    file = True
    table = []
    fd = 0
    for n in sizes:
        if file:
            table.append((n, fd))
            fd += 1
        else:
            table.append((n, -1))

        file = not file

    space = 0

    while space < len(table):
        if table[space][1] != -1:
            space += 1
            continue

        free = table[space][0]
        # find rightmost file that fits
        for i in range(len(table) - 1, -1, -1):
            n, fd = table[i]
            if n <= free and fd >= 0:
                break

        if i < space:
            space += 1
            continue

        free, _ = table[space]
        table[space] = (n, fd)
        table[i] = (n, -2)
        if free - n > 0:
            table.insert(space + 1, (free - n, -1))

    blocks = [-1] * sum(sizes)
    i = 0
    for n, fd in table:
        if fd >= 0:
            blocks[i:i+n] = [fd] * n
            fd += 1

        i += n

    res = 0
    for i, block in enumerate(blocks):
        if block != -1:
            res += i * block

    return res


def main():
    assert solve_p1("example") == 1928
    print(solve_p1("input"))

    assert solve_p2("example") == 2858
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
