import sys
import re

SPECIAL_CHARS = r"[^\d.\n]"

def find_neighbour_numbers(x, y, grid):
    number_identified = False
    neighbours = []
    for y_offset in [-1, 0, 1]:
        for x_offset in [-1, 0, 1]:
            _x = x + x_offset
            _y = y + y_offset
            try:
                p = grid[_y][_x]
            except IndexError:
                continue

            if re.match(r"\d", p):
                if not number_identified:
                    number_identified = True
                    right_part = re.findall(r"^\d+", grid[_y][_x:])
                    left_part = re.findall(r"\d+$", grid[_y][:_x])
                    neighbours.append(int("".join(left_part + right_part)))
            else:
                number_identified = False
    print(neighbours)
    return sum(neighbours)


def main(input_file):
    with open(input_file, "r") as f:
        s = 0
        grid = f.readlines()
        for y, l in enumerate(grid):
            for x, p in enumerate(l):
                if re.match(SPECIAL_CHARS, p):
                    s += find_neighbour_numbers(x, y, grid)

        print(s)


if __name__ == '__main__':
    main(sys.argv[-1])
