def solve_p1(path):
    with open(path) as f:
        reports = [[int(x) for x in line.split()] for line in f]

    num_safe = 0
    for report in reports:
        inc = report[1] > report[0]

        small_diff = all(abs(nxt - cur) <= 3 and nxt != cur for nxt, cur in zip(report[1:], report))
        monotonic = all((nxt > cur) == inc for nxt, cur in zip(report[1:], report))

        num_safe += monotonic and small_diff
    return num_safe


def solve_p2(path):
    with open(path) as f:
        reports = [[int(x) for x in line.split()] for line in f]

    num_safe = 0
    for report in reports:

        safe = False
        for i in range(len(report) + 1):
            report_fixed = report[:i] + report[i + 1:]
            inc = report_fixed[-1] > report_fixed[0]
            small_diff = all(abs(nxt - cur) <= 3 and nxt != cur for nxt, cur in zip(report_fixed[1:], report_fixed))
            monotonic = all((nxt > cur) == inc for nxt, cur in zip(report_fixed[1:], report_fixed))
            safe = safe or (monotonic and small_diff)
            if safe:
                break

        num_safe += safe

    return num_safe


def main():
    assert solve_p1("example") == 2
    print(solve_p1("input"))

    assert solve_p2("example") == 4
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
