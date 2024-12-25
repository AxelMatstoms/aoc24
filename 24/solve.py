import itertools
import graphlib
from collections import defaultdict


def solve_p1(path):
    with open(path) as f:
        initial, gates = f.read().split("\n\n")

    values = {}
    for line in initial.splitlines():
        key, value = line.split(": ")
        values[key] = int(value)

    preds = defaultdict(set)
    which_op = {}
    for line in gates.splitlines():
        op, res = line.split(" -> ")
        in1, op, in2 = op.split()
        which_op[res] = op
        preds[res].add(in1)
        preds[res].add(in2)

    ts = graphlib.TopologicalSorter(preds)
    order = tuple(ts.static_order())

    for key in order:
        if key not in preds:
            continue

        in1, in2 = preds[key]
        in1 = values[in1]
        in2 = values[in2]

        match which_op[key]:
            case "XOR":
                out = in1 ^ in2
            case "OR":
                out = in1 | in2
            case "AND":
                out = in1 & in2
            case _:
                raise ValueError("bad")

        values[key] = out

    bitstring = ""
    for i in range(100):
        try:
            bitstring = str(values[f"z{i:02}"]) + bitstring
        except KeyError:
            break

    return int(bitstring, 2)


def solve_p2(path):
    with open(path) as f:
        initial, gates = f.read().split("\n\n")

    nodes = []
    for line in initial.splitlines():
        key, value = line.split(": ")
        nodes.append(key)

    # preds = defaultdict(set)
    # which_op = {}
    # parsed_gates = []

    edges = []
    for line in gates.splitlines():
        op, res = line.split(" -> ")
        in1, op, in2 = op.split()

        nodes.append(f"{res} [label=\"{op}{res}\"]")
        edges.append(f"{in1} -> {res}")
        edges.append(f"{in2} -> {res}")

        # which_op[res] = op
        # preds[res].add(in1)
        # preds[res].add(in2)
        # parsed_gates.append((in1, op, in2, res))

    print("digraph G {")
    print("{")
    for node in nodes:
        print(node)

    print("}")
    for edge in edges:
        print(edge)

    print("}")

    # half_add = [""] * bits
    # half_carry = [""] * bits
    # for in1, op, in2, res in parsed_gates:
    #     if in1[0] in "xy" and in2 in "xy" and op == "XOR":
    #         half_add[int(in1[1:])] = res

    #     if in1[0] in "xy" and in2 in "xy" and op == "AND":
    #         half_carry[int(in1[1:])] = res


    # def add(x, y, swaps):
    #     loc_preds = {(swaps[key] if key in swaps else key): preds[key] for key in preds}

    #     loc_values = {}
    #     for i in range(bits):
    #         if x & (1 << i):
    #             loc_values[f"x{i:02}"] = 1
    #         else:
    #             loc_values[f"x{i:02}"] = 0

    #         if y & (1 << i):
    #             loc_values[f"y{i:02}"] = 1
    #         else:
    #             loc_values[f"y{i:02}"] = 0

    #     ts = graphlib.TopologicalSorter(loc_preds)
    #     order = tuple(ts.static_order())

    #     for key in order:
    #         if key not in loc_preds:
    #             continue

    #         in1, in2 = loc_preds[key]
    #         in1 = loc_values[in1]
    #         in2 = loc_values[in2]

    #         match which_op[key]:
    #             case "XOR":
    #                 out = in1 ^ in2
    #             case "OR":
    #                 out = in1 | in2
    #             case "AND":
    #                 out = in1 & in2
    #             case _:
    #                 raise ValueError("bad")

    #         loc_values[key] = out

    #     bitstring = ""
    #     for i in range(100):
    #         try:
    #             bitstring = str(loc_values[f"z{i:02}"]) + bitstring
    #         except KeyError:
    #             break

    #     return int(bitstring, 2)

    # cases = [
    #     (0x1, 0x0),
    #     (0x1, 0x1),
    #     (0xFFFF_FFFF_FFFF, 0x0),
    #     (0xAAAA_AAAA_AAAA, 0x5555_5555_5555),
    #     (0x1234_5678_9ABC, 0x1234_5678_9ABC),
    #     (0x4321_8765_CBA9, 0x5678_9ABC_1234),
    # ]

    # bit_error = 0
    # for lhs, rhs in cases:
    #     lhs = lhs & ((1 << (bits + 1)) - 1)
    #     rhs = rhs & ((1 << (bits + 1)) - 1)

    #     actual = add(lhs, rhs, {})
    #     expected = lhs + rhs

    #     diff = actual ^ expected
    #     bit_error += diff.bit_count()

    # print("be:", bit_error)

    # swaps = {}
    # best = float("inf")
    # best_swaps = {}

    # for a, b in itertools.product(preds.keys(), repeat=2):
    #     new_bit_error = 0
    #     if a in swaps or b in swaps:
    #         continue

    #     new_swaps = {**swaps, a: b, b: a}
    #     cycle = False
    #     for lhs, rhs in cases:
    #         lhs = lhs & ((1 << (bits + 1)) - 1)
    #         rhs = rhs & ((1 << (bits + 1)) - 1)

    #         try:
    #             actual = add(lhs, rhs, new_swaps)
    #         except graphlib.CycleError:
    #             cycle = True
    #             break

    #         expected = lhs + rhs

    #         diff = actual ^ expected
    #         new_bit_error += diff.bit_count()

    #     if cycle:
    #         continue

    #     if new_bit_error < best:
    #         best_swaps = new_swaps
    #         best = new_bit_error

    # print(best_swaps)


def main():
    assert solve_p1("example") == 2024
    # print(solve_p1("input"))

    # assert solve_p2("example") == ...
    solve_p2("input")


if __name__ == "__main__":
    main()
