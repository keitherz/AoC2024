"""Advent of Code 2024 Solution Template"""

import re

from typing import List


def solve_part1(input_lines: List[str]) -> str:
    """Solution for part 1 routine function"""
    result = 0
    for line in input_lines:
        muls = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for mul in muls:
            a, b = map(int, mul[4:-1].split(","))
            result += a * b
    return str(result)


def solve_part2(input_lines: List[str]) -> str:
    """Solution for part 2 routine function"""
    result = 0
    enabled = True
    for line in input_lines:
        instructions = re.findall(
            r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))", line
        )
        for mul, do, dont in instructions:
            print(mul, do, dont)
            if mul and enabled:
                a, b = map(int, mul[4:-1].split(","))
                result += a * b
            if do:
                enabled = True
            if dont:
                enabled = False
    return str(result)


def solve(input_lines: List[str], input_lines2: List[str] | None = None) -> str:
    """Return solutions for part 1 and part 2"""
    results = filter(
        len, [solve_part1(input_lines), solve_part2(input_lines2 or input_lines)]
    )
    return ",".join(results)
