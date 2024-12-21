def solve_p1(path):
    with open(path) as f:
        codes = f.read().strip().splitlines()

    numeric = ["789", "456", "123", " 0A"]
    directional = [" ^A", "<v>"]

    num_by_key = {
        ch: (x, y) for y, row in enumerate(numeric) for x, ch in enumerate(row)
    }
    dir_by_key = {
        ch: (x, y) for y, row in enumerate(directional) for x, ch in enumerate(row)
    }

    def enter(keypad, by_key, seq):
        x, y = by_key["A"]

        out = []
        for ch in seq:
            nx, ny = by_key[ch]
            dx, dy = nx - x, ny - y

            if dx > 0 and dy >= 0:  # right-down
                if keypad[ny][x] == " ":
                    out += [">"] * dx
                    out += ["v"] * dy
                else:
                    out += ["v"] * dy
                    out += [">"] * dx
            elif dx > 0 and dy <= 0:  # right-up
                if keypad[ny][x] == " ":
                    out += [">"] * dx
                    out += ["^"] * -dy
                else:
                    out += ["^"] * -dy
                    out += [">"] * dx
            elif dy < 0:  # up-left
                if keypad[y][nx] == " ":
                    out += ["^"] * -dy
                    out += ["<"] * -dx
                else:
                    out += ["<"] * -dx
                    out += ["^"] * -dy
            else:  # down-left
                if keypad[y][nx] == " ":
                    out += ["v"] * dy
                    out += ["<"] * -dx
                else:
                    out += ["v"] * dy
                    out += ["<"] * -dx

            out += "A"
            x, y = nx, ny

        return out

    def type_(keypad, seq):
        x, y = next(
            (x, y)
            for y, row in enumerate(keypad)
            for x, ch in enumerate(row)
            if ch == "A"
        )
        DELTA = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
        out = []
        for ch in seq:
            if ch == "A":
                out += keypad[y][x]
            else:
                dx, dy = DELTA[ch]
                x += dx
                y += dy

        return out

    res = 0
    for code in codes:
        seq = enter(numeric, num_by_key, code)
        dir1 = enter(directional, dir_by_key, seq)
        dir2 = enter(directional, dir_by_key, dir1)

        dir11 = type_(directional, dir2)
        assert dir11 == dir1

        seq2 = type_(directional, dir11)
        assert seq2 == seq

        code2 = "".join(type_(numeric, seq2))
        assert code2 == code

        res += len(dir2) * int(code.strip("A"))

    return res


def solve_p2(path, n=25):
    with open(path) as f:
        codes = f.read().strip().splitlines()

    numeric = ["789", "456", "123", " 0A"]
    directional = [" ^A", "<v>"]

    num_by_key = {
        ch: (x, y) for y, row in enumerate(numeric) for x, ch in enumerate(row)
    }
    dir_by_key = {
        ch: (x, y) for y, row in enumerate(directional) for x, ch in enumerate(row)
    }

    def enter(keypad, by_key, seq):
        x, y = by_key["A"]

        out = []
        for ch in seq:
            nx, ny = by_key[ch]
            dx, dy = nx - x, ny - y

            if dx > 0 and dy >= 0:  # right-down
                if keypad[ny][x] == " ":
                    out += [">"] * dx
                    out += ["v"] * dy
                else:
                    out += ["v"] * dy
                    out += [">"] * dx
            elif dx > 0 and dy <= 0:  # right-up
                if keypad[ny][x] == " ":
                    out += [">"] * dx
                    out += ["^"] * -dy
                else:
                    out += ["^"] * -dy
                    out += [">"] * dx
            elif dy < 0:  # up-left
                if keypad[y][nx] == " ":
                    out += ["^"] * -dy
                    out += ["<"] * -dx
                else:
                    out += ["<"] * -dx
                    out += ["^"] * -dy
            else:  # down-left
                if keypad[y][nx] == " ":
                    out += ["v"] * dy
                    out += ["<"] * -dx
                else:
                    out += ["v"] * dy
                    out += ["<"] * -dx

            out += "A"
            x, y = nx, ny

        return out

    def from_to(keypad, by_key, first, second):
        x, y = by_key[first]
        nx, ny = by_key[second]
        dx, dy = nx - x, ny - y

        vert = "^" if dy < 0 else "v"
        hori = "<" if dx < 0 else ">"
        dx = abs(dx)
        dy = abs(dy)

        out = []
        if keypad[ny][x] != " ":
            out.append(vert * dy + hori * dx + "A")
        if keypad[y][nx] != " ":
            out.append(hori * dx + vert * dy + "A")

        return out

    dp = {(first, second): 1 for first in "<>v^A" for second in "<>v^A"}
    for _ in range(n):
        new_dp = {}
        for prev, nxt_ in dp:
            cost = min(
                sum(dp[(x1, x2)] for x1, x2 in zip("A" + alt, alt))
                for alt in from_to(directional, dir_by_key, prev, nxt_)
            )

            new_dp[(prev, nxt_)] = cost
        dp = new_dp

    res = 0
    for code in codes:
        seq = ["A"] + enter(numeric, num_by_key, code)
        x = sum(dp[(x1, x2)] for x1, x2 in zip(seq, seq[1:]))
        res += x * int(code.strip("A"))

    return res


def main():
    assert solve_p1("example") == 126384
    print(solve_p1("input"))

    solve_p2("example", n=3)
    assert solve_p2("example", n=2) == 126384
    assert solve_p2("input", n=2) == solve_p1("input")
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
