import sys
import re


CUBES = {"red": 12, "green": 13, "blue": 14}

def game_valid(sets):
    for s in sets:
        for colour_cubes in s.split(","):
            n, colour = colour_cubes.strip().split(" ")
            if CUBES[colour.strip()] < int(n.strip()):
                return False
    return True

def main(input_file):
    with open(input_file, "r") as f:
        s = 0
        for l in f.readlines():
            game, rest = l.split(":")
            game_points = game.split(" ")[-1]
            sets = rest.split(";")
            if game_valid(sets):
                s += int(game_points)

        print(s)


if __name__ == '__main__':
    main(sys.argv[-1])
