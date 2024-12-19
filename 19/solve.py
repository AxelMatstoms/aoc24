import functools


def solve_p1(path):
    with open(path) as f:
        lines = f.read().splitlines()

        towels = lines[0].strip().split(", ")
        designs = [line.strip() for line in lines[2:]]

    @functools.cache
    def possible(design):
        if design == "":
            return True

        for towel in towels:
            if design.startswith(towel) and possible(design[len(towel):]):
                return True

        return False

    return sum(possible(design) for design in designs)


def solve_p2(path):
    with open(path) as f:
        lines = f.read().splitlines()

        towels = lines[0].strip().split(", ")
        designs = [line.strip() for line in lines[2:]]

    @functools.cache
    def numways(design):
        if design == "":
            return 1

        num = 0
        for towel in towels:
            if design.startswith(towel):
                num += numways(design[len(towel):])

        return num

    return sum(numways(design) for design in designs)


def main():
    assert solve_p1("example") == 6
    print(solve_p1("input"))

    assert solve_p2("example") == 16
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
