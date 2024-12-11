"""Advent of Code 2024 Solution Template"""

from typing import List, Tuple


def get_word(
    letter_map: List[List[str]],
    start: Tuple[int, int],
    increment: Tuple[int, int],
    length: int,
) -> str:
    """Get word from the letter_map"""
    word = ""
    i, j = start
    i_incr, j_incr = increment
    for _ in range(length):
        if (i < 0) or (i >= len(letter_map)) or (j < 0) or (j >= len(letter_map[i])):
            continue
        word += letter_map[i][j]
        i += i_incr
        j += j_incr
    return word


def solve_part1(input_lines: List[str]) -> str:
    """Solution for part 1 routine function"""
    result = 0
    letter_map = []
    search_word = "XMAS"
    search_len = len(search_word)
    for line in input_lines:
        line_letters = list(line.strip())
        letter_map.append(line_letters)

    for i, row in enumerate(letter_map):
        for j, _ in enumerate(row):
            words = []
            # horizontal - right
            words.append(get_word(letter_map, (i, j), (0, 1), search_len))
            # horizontal - left
            words.append(get_word(letter_map, (i, j), (0, -1), search_len))
            # vertical - down
            words.append(get_word(letter_map, (i, j), (1, 0), search_len))
            # vertical - up
            words.append(get_word(letter_map, (i, j), (-1, 0), search_len))
            # diagonal - down, right
            words.append(get_word(letter_map, (i, j), (1, 1), search_len))
            # diagonal - down, left
            words.append(get_word(letter_map, (i, j), (1, -1), search_len))
            # diagonal - up, right
            words.append(get_word(letter_map, (i, j), (-1, 1), search_len))
            # diagonal - up, left
            words.append(get_word(letter_map, (i, j), (-1, -1), search_len))
            result += words.count(search_word)

    return str(result)


def solve_part2(input_lines: List[str]) -> str:
    """Solution for part 2 routine function"""
    result = 0
    letter_map = []
    search_word = "MAS"
    search_word_r = "".join(reversed(search_word))
    search_len = len(search_word)
    for line in input_lines:
        line_letters = list(line.strip())
        letter_map.append(line_letters)

    for i, row in enumerate(letter_map):
        for j, _ in enumerate(row):
            word_a = get_word(letter_map, (i, j), (1, 1), search_len)
            word_b = get_word(letter_map, (i, j + search_len - 1), (1, -1), search_len)
            word_a_valid = word_a == search_word or word_a == search_word_r
            word_b_valid = word_b == search_word or word_b == search_word_r
            if word_a_valid and word_b_valid:
                result += 1
    return str(result)


def solve(input_lines: List[str], input_lines2: List[str] | None = None) -> str:
    """Return solutions for part 1 and part 2"""
    results = filter(
        len, [solve_part1(input_lines), solve_part2(input_lines2 or input_lines)]
    )
    return ",".join(results)
