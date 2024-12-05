#! /bin/env python3
# pylint: disable=missing-docstring
from collections import Counter


def parse_lists() -> tuple[list[int], list[int]]:
    with open("day1.txt", "r", encoding="utf-8") as in_file:
        lines = in_file.readlines()

    left: list[int] = []
    right: list[int] = []
    for line in lines:
        items = line.split()
        left.append(int(items[0]))
        right.append(int(items[1]))

    return (left, right)


def main() -> None:
    left, right = parse_lists()

    counts = Counter(right)
    similarities = [number * counts[number] for number in left]
    print(sum(similarities))


if __name__ == "__main__":
    main()
