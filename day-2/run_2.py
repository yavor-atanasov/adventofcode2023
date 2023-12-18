import math
import sys


def minimal_set_power(sets):
    minimal_set = {}
    for s in sets:
        for colour_cubes in s.split(","):
            n, colour = colour_cubes.strip().split(" ")
            n = int(n)
            colour = colour.strip()
            if minimal_set.get(colour, n) <= n:
                minimal_set[colour] = n
    return math.prod(minimal_set.values())


def main(input_file):
    with open(input_file, "r") as f:
        s = 0
        for l in f.readlines():
            game, rest = l.split(":")
            sets = rest.split(";")
            s += minimal_set_power(sets)

        print(s)


if __name__ == '__main__':
    main(sys.argv[-1])
