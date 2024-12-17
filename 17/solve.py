def run(reg, prog):
    pc = 0
    out = []

    def combo(arg):
        if 0 <= arg <= 3:
            return arg

        return reg[arg - 4]

    while pc < len(prog):
        op_code = prog[pc]

        match op_code:
            case 0:  # adv
                reg[0] >>= combo(prog[pc + 1])
                pc += 2
            case 1:  # bxl
                reg[1] ^= prog[pc + 1]
                pc += 2
            case 2:  # bst
                reg[1] = combo(prog[pc + 1]) % 8
                pc += 2
            case 3:  # jnz
                if reg[0]:
                    pc = prog[pc + 1]
                else:
                    pc += 2
            case 4:  # bxc
                reg[1] ^= reg[2]
                pc += 2
            case 5:  # out
                out.append(combo(prog[pc + 1]) % 8)
                pc += 2
            case 6:  # bdv
                reg[1] = reg[0] >> combo(prog[pc + 1])
                pc += 2
            case 7:  # cdv
                reg[2] = reg[0] >> combo(prog[pc + 1])
                pc += 2
            case _:
                raise ValueError(f"unknown op code {op_code}")

    return out


def solve_p1(path):
    with open(path) as f:
        a, b, c, _, p = f.read().splitlines()
        a = int(a.split(": ")[1])
        b = int(b.split(": ")[1])
        c = int(c.split(": ")[1])
        p = [int(x) for x in p.split(": ")[1].split(",")]

    out = run([a, b, c], p)

    return ",".join(str(x) for x in out)


def solve_p2(path):
    """Tack Astrid!"""
    with open(path) as f:
        a, b, c, _, p = f.read().splitlines()
        a = int(a.split(": ")[1])
        b = int(b.split(": ")[1])
        c = int(c.split(": ")[1])
        p = tuple(int(x) for x in p.split(": ")[1].split(","))

    candidates = [0]
    for i in range(len(p) - 1, -1, -1):
        place = 8 ** i
        new_candidates = []
        for prefix in candidates:
            for dig in range(8):
                a = prefix + dig * place
                out = tuple(run([a, b, c], p))

                if len(out) != len(p):
                    continue

                if out[i:] == p[i:]:
                    new_candidates.append(a)

        candidates = new_candidates

    return min(candidates)


def main():
    assert solve_p1("example") == "4,6,3,5,6,3,5,2,1,0"
    print(solve_p1("input"))

    assert solve_p2("example2") == 117440
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
