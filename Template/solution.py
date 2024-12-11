"""Advent of Code 2024 Solution Template"""

from typing import List


def solve_part1(input_lines: List[str]) -> str:
    """Solution for part 1 routine function"""
    result = 0
    for line in input_lines:
        line_split = map(int, line.split())
        for val in line_split:
            result += int(val)
    return str(result)


def solve_part2(input_lines: List[str]) -> str:
    """Solution for part 2 routine function"""
    result = 1
    for line in input_lines:
        line_split = map(int, line.split())
        for val in line_split:
            result *= int(val)
    return str(result)


def solve(input_lines: List[str]) -> str:
    """Return solutions for part 1 and part 2"""
    results = filter(len, [solve_part1(input_lines), solve_part2(input_lines)])
    return ",".join(results)
