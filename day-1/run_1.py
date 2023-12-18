import sys
import re


def main(input_file):
    with open(input_file, "r") as f:
        s = 0
        for l in f.readlines():
            digits = re.findall(r"\d", l)
            if len(digits) == 1:
                digits = digits * 2
            s = sum([int("".join(digits[::len(digits) - 1])), s])
        print(s)


if __name__ == '__main__':
    main(sys.argv[-1])
