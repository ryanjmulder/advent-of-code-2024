#! /bin/env python3
# pylint: disable=missing-docstring


def parse_reports() -> list[list[int]]:
    with open("day2.txt", "r", encoding="utf-8") as in_file:
        lines = in_file.readlines()

    return [[int(item) for item in line.split()] for line in lines]


def main() -> None:
    reports = parse_reports()
    print(reports)


if __name__ == "__main__":
    main()
