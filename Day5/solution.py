"""Advent of Code 2024 Solution Template"""

from typing import Dict, List, Literal


def solve_part1(input_lines: List[str]) -> str:
    """Solution for part 1 routine function"""
    result = 0
    rules_l: Dict[int, List[int]] = {}
    rules_r: Dict[int, List[int]] = {}
    mode: Literal["rules"] | Literal["updates"] = "rules"
    for line in input_lines:
        if not line.strip():
            mode = "updates"
        elif mode == "rules":
            l, r = map(int, line.split("|"))
            rules_l[l] = (rules_l.get(l, [])) + [r]
            rules_r[r] = (rules_r.get(r, [])) + [l]
        elif mode == "updates":
            updates = list(map(int, line.split(",")))
            is_correct = True
            for i, update in enumerate(updates):
                for j in range(i):
                    if updates[j] in rules_l.get(update, []):
                        is_correct = False
                        break
                for j in range(i + 1, len(updates)):
                    if updates[j] in rules_r.get(update, []):
                        is_correct = False
                        break
                if not is_correct:
                    break
            if is_correct:
                result += updates[(len(updates) - 1) // 2]
    return str(result)


def solve_part2(input_lines: List[str]) -> str:
    """Solution for part 2 routine function"""
    result = 0
    rules_l: Dict[int, List[int]] = {}
    rules_r: Dict[int, List[int]] = {}
    mode: Literal["rules"] | Literal["updates"] = "rules"
    for line in input_lines:
        if not line.strip():
            mode = "updates"
        elif mode == "rules":
            l, r = map(int, line.split("|"))
            rules_l[l] = (rules_l.get(l, [])) + [r]
            rules_r[r] = (rules_r.get(r, [])) + [l]
        elif mode == "updates":
            updates = list(map(int, line.split(",")))
            is_correct = False
            was_incorrect = False
            while not is_correct:
                is_correct = True
                for i, update in enumerate(updates):
                    for j in range(i):
                        if updates[j] in rules_l.get(update, []):
                            is_correct, was_incorrect = False, True
                            updates[i], updates[j] = updates[j], updates[i]
                            break
                    for j in range(i + 1, len(updates)):
                        if updates[j] in rules_r.get(update, []):
                            is_correct, was_incorrect = False, True
                            updates[i], updates[j] = updates[j], updates[i]
                            break
                    if not is_correct:
                        break
            if was_incorrect:
                result += updates[(len(updates) - 1) // 2]
    return str(result)


def solve(input_lines: List[str], input_lines2: List[str] | None = None) -> str:
    """Return solutions for part 1 and part 2"""
    results = filter(
        len, [solve_part1(input_lines), solve_part2(input_lines2 or input_lines)]
    )
    return ",".join(results)
