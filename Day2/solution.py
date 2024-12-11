"""Advent of Code 2024 Solution Template"""

from typing import List, Tuple


def check_safe(report: List[int], skip_index: int = -1) -> Tuple[bool, int]:
    """Checks the given report if the levels are safe, returns if safe and the unsafe level index"""
    levels = report
    if skip_index >= 0:
        levels = report[:skip_index] + report[skip_index + 1 :]
    full_slope = levels[-1] - levels[0]
    for i in range(1, len(levels)):
        slope = levels[i] - levels[i - 1]
        # test if signs are not equal
        if slope ^ full_slope < 0:
            return (False, i)
        if abs(slope) < 1 or abs(slope) > 3:
            return (False, i)
    return (True, -1)


def solve_part1(input_lines: List[str]) -> str:
    """Solution for part 1 routine function"""
    result = 0
    for line in input_lines:
        line_split = list(map(int, line.split()))
        is_safe, _ = check_safe(line_split)
        if is_safe:
            result += 1
    return str(result)


def solve_part2(input_lines: List[str]) -> str:
    """Solution for part 2 routine function"""
    result = 0
    for line in input_lines:
        line_split = list(map(int, line.split()))
        is_safe, unsafe_index = check_safe(line_split)
        # if unsafe, try skipping unsafe_index (right hand side of pair)
        if not is_safe:
            is_safe, _ = check_safe(line_split, unsafe_index)
        # if still unsafe, try skipping unsafe_index - 1 (left hand side of pair)
        if not is_safe:
            is_safe, _ = check_safe(line_split, unsafe_index - 1)
        if is_safe:
            result += 1
    return str(result)


def solve(input_lines: List[str]) -> str:
    """Return solutions for part 1 and part 2"""
    results = filter(len, [solve_part1(input_lines), solve_part2(input_lines)])
    return ",".join(results)
