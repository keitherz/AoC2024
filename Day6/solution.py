"""Advent of Code 2024 Solution Template"""

import copy

from typing import List, Literal, Set, Tuple

CornerKey = Literal["bl", "tl", "tr", "br"]


def traverse_path(
    input_map: List[List[str]], initial_pos: Tuple[int, int]
) -> Tuple[Set[Tuple[int, int]], bool]:
    """Traverse guard path on given map, returns visited locations and if loop is found"""
    guard_pos: Tuple[int, int] = initial_pos
    guard_dir: Tuple[int, int] = (-1, 0)
    visited_pos: Set[Tuple[int, int]] = set()
    path_history: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()

    # include guard starting position
    visited_pos.add(guard_pos)
    path_history.add((guard_pos, guard_dir))
    while True:
        next_guard_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        if (next_guard_pos, guard_dir) in path_history:
            return (visited_pos, True)
        path_history.add((next_guard_pos, guard_dir))
        # if out of bounds, guard has left the area
        if (
            next_guard_pos[0] < 0
            or next_guard_pos[0] >= len(input_map)
            or next_guard_pos[1] < 0
            or next_guard_pos[1] >= len(input_map[guard_pos[0]])
        ):
            break
        # if obstacle detected, turn right 90 degrees
        if input_map[next_guard_pos[0]][next_guard_pos[1]] == "#":
            guard_dir = (guard_dir[1], -guard_dir[0])
        else:
            guard_pos = next_guard_pos
            visited_pos.add(guard_pos)
    return (visited_pos, False)


def solve_part1(input_lines: List[str]) -> str:
    """Solution for part 1 routine function"""
    input_map: List[List[str]] = []
    initial_pos = (-1, -1)
    for line in input_lines:
        line_chars = list(line.strip())
        if "^" in line_chars:
            initial_pos = (len(input_map), line_chars.index("^"))
        input_map.append(line_chars)
    visited_pos, _ = traverse_path(input_map, initial_pos)
    return str(len(visited_pos))


def solve_part2(input_lines: List[str]) -> str:
    """Solution for part 2 routine function"""
    input_map: List[List[str]] = []
    initial_pos = (-1, -1)
    for line in input_lines:
        line_chars = list(line.strip())
        if "^" in line_chars:
            initial_pos = (len(input_map), line_chars.index("^"))
        input_map.append(line_chars)
    result = 0
    visited_pos, _ = traverse_path(input_map, initial_pos)
    visited_pos.remove(initial_pos)
    for pos in visited_pos:
        test_map = copy.deepcopy(input_map)
        test_map[pos[0]][pos[1]] = "#"
        _, is_loop_found = traverse_path(test_map, initial_pos)
        if is_loop_found:
            result += 1
    return str(result)


def solve(input_lines: List[str], input_lines2: List[str] | None = None) -> str:
    """Return solutions for part 1 and part 2"""
    results = filter(
        len, [solve_part1(input_lines), solve_part2(input_lines2 or input_lines)]
    )
    return ",".join(results)
