"""Advent of Code 2024 Solution for Day 1"""

from typing import List


def solve_part1(input_lines: List[str]) -> str:
    """Solution for part 1 routine function"""
    result = 0
    left_list = []
    right_list = []
    for line in input_lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    for i in range(len(input_lines)):
        result += abs(left_list[i] - right_list[i])
    return str(result)


def solve_part2(input_lines: List[str]) -> str:
    """Solution for part 2 routine function"""
    result = 0
    left_list = []
    right_list = []
    for line in input_lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    for i in range(len(input_lines)):
        result += left_list[i] * right_list.count(left_list[i])
    return str(result)


def solve(input_lines: List[str]) -> List[str]:
    """Return solutions for part 1 and part 2"""
    return [solve_part1(input_lines), solve_part2(input_lines)]
