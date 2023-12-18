import sys
import re


DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

DIGIT_SEARCH_PATTERN = "|".join(DIGIT_MAP.keys())
REGEX = r"({0}|\d)".format(DIGIT_SEARCH_PATTERN)
REVERSE_REGEX = r"({0}|\d)".format(DIGIT_SEARCH_PATTERN[::-1])

def main(input_file):
    with open(input_file, "r") as f:
        s = 0
        for l in f.readlines():
            d1 = re.findall(REGEX, l)[0]
            d2 = re.findall(REVERSE_REGEX, l[::-1])[0][::-1]
            dd = "".join(map(lambda x: DIGIT_MAP.get(x, x), [d1, d2]))
            s += int(dd)
        print(s)


if __name__ == '__main__':
    main(sys.argv[-1])
