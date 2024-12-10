"""Advent of Code 2024 Solution Template"""

from typing import List


def solve(input_lines: List[str]) -> str:
    """Solution routine function"""
    result = 0
    for line in input_lines:
        line_split = line.split()
        for val in line_split:
            result += int(val)
    return str(result)
