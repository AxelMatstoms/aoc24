from collections import defaultdict
from itertools import chain, combinations


def solve_p1(path):
    adj = defaultdict(list)
    with open(path) as f:
        for line in f:
            left, right = line.strip().split("-")
            adj[left].append(right)
            adj[right].append(left)

    sets = set()
    for n1, neighbours in adj.items():
        for n2 in neighbours:
            for n3 in adj[n2]:
                if n3 in adj[n1]:
                    sets.add(frozenset({n1, n2, n3}))

    ans = 0
    for group in sets:
        if any(comp[0] == "t" for comp in group):
            ans += 1

    return ans


def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def solve_p2(path):
    adj = defaultdict(list)
    with open(path) as f:
        for line in f:
            left, right = line.strip().split("-")
            adj[left].append(right)
            adj[right].append(left)

    ans = set()
    marked = set()
    for n1 in adj:
        if n1 in marked:
            continue

        marked |= {*adj[n1]}
        nodes = {n1, *adj[n1]}

        for clique in powerset(nodes):
            clique = set(clique)
            if all(clique <= {n2, *adj[n2]} for n2 in clique):
                ans = max(ans, clique, key=len)


    return ",".join(sorted(ans))


def main():
    assert solve_p1("example") == 7
    print(solve_p1("input"))

    assert solve_p2("example") == "co,de,ka,ta"
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
