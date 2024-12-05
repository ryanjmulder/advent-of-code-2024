#! /bin/env python3
# pylint: disable=missing-docstring


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
    left.sort()
    right.sort()

    distances = [abs(right[i] - left[i]) for i in range(0, len(left))]
    print(sum(distances))


if __name__ == "__main__":
    main()
