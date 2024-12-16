import heapq


def solve_p1(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    start = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "S"
    )
    end = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "E"
    )

    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dist = {(start, 0): 0}
    to_visit = [(0, start, 0)]

    best = float("inf")

    while to_visit:
        cost, (x, y), facing = heapq.heappop(to_visit)

        if (x, y) == end:
            best = min(best, cost)
            continue

        dx, dy = DELTA[facing]

        xx, yy = x + dx, y + dy
        new_cost = cost + 1
        key = ((xx, yy), facing)
        if grid[yy][xx] != "#" and (key not in dist or dist[key] > new_cost):
            heapq.heappush(to_visit, (new_cost, (xx, yy), facing))
            dist[key] = new_cost

        for d in [-1, 1]:
            key2 = ((x, y), (facing + d) % 4)
            cost2 = cost + 1000
            if key2 not in dist or dist[key2] > cost2:
                heapq.heappush(to_visit, (cost2, (x, y), (facing + d) % 4))
                dist[key2] = cost2

    return best


def solve_p2(path):
    with open(path) as f:
        grid = [line.strip() for line in f]

    start = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "S"
    )
    end = next(
        (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "E"
    )

    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dist = {(start, 0): 0}
    to_visit = [(0, start, 0)]
    pred = {(start, 0): None}
    best = float("inf")

    while to_visit:
        cost, (x, y), facing = heapq.heappop(to_visit)

        if (x, y) == end:
            best = min(best, cost)
            continue

        dx, dy = DELTA[facing]

        xx, yy = x + dx, y + dy
        new_cost = cost + 1
        key = ((xx, yy), facing)
        if grid[yy][xx] != "#" and (key not in dist or new_cost <= dist[key]):
            heapq.heappush(to_visit, (new_cost, (xx, yy), facing))

            if key not in dist or new_cost < dist[key]:
                pred[key] = [((x, y), facing)]
            else:
                pred[key].append(((x, y), facing))

            dist[key] = new_cost

        for d in [-1, 1]:
            new_facing = (facing + d) % 4
            key2 = ((x, y), new_facing)
            cost2 = cost + 1000
            if key2 not in dist or cost2 <= dist[key2]:
                heapq.heappush(to_visit, (cost2, (x, y), new_facing))

                if key2 not in dist or cost2 < dist[key2]:
                    pred[key2] = [((x, y), facing)]
                else:
                    pred[key2].append(((x, y), facing))

                dist[key2] = cost2

    best_tiles = set()

    def follow(pos, facing):
        visit = {(pos, facing)}
        visited = {(pos, facing)}

        while visit:
            key = visit.pop()

            pos, facing = key
            best_tiles.add(pos)

            if key == (start, 0):
                continue

            for pos2, facing2 in pred[(pos, facing)]:
                if (pos2, facing2) not in visited:
                    visit.add((pos2, facing2))
                    visited.add((pos, facing2))

    for i in range(4):
        if (end, i) in dist and dist[(end, i)] == best:
            follow(end, i)
    return len(best_tiles)


def main():
    assert solve_p1("example") == 7036
    print(solve_p1("input"))

    assert solve_p2("example") == 45
    print(solve_p2("input"))


if __name__ == "__main__":
    main()
