import re


def solve_p1(path):
    with open(path) as f:
        line = f.read()

    acc = 0
    for lhs, rhs in re.findall(r"mul\((\d+),(\d+)\)", line):
        acc += int(lhs) * int(rhs)

    return acc


def solve_p2(path):
    with open(path) as f:
        line = f.read()

    on = True
    acc = 0
    for mul, lhs, rhs, do, dont in re.findall(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", line):
        if dont:
            on = False
        elif do:
            on = True
        elif mul:
            if on:
                acc += int(lhs) * int(rhs)

    return acc


def main():
    assert solve_p1("example") == 161
    print(solve_p1("input"))

    assert solve_p2("example2") == 48
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
