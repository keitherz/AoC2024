"""Advent of Code 2024 Solution Runner"""

import argparse
import importlib
import importlib.util
import os
import sys

from typing import List


TEST_INPUT_FILENAME = "test_input.txt"
TEST_INPUT2_FILENAME = "test_input2.txt"
TEST_OUTPUT_FILENAME = "test_output.txt"
PUZZLE_INPUT_FILENAME = "puzzle_input.txt"


def load_file_lines(
    solution_dir: str, filename: str, skip_error: bool = False
) -> List[str] | None:
    """Input file loader"""
    file_path = os.path.relpath(f"{solution_dir}/{filename}")
    try:
        with open(file_path, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
            return lines
    except Exception as ex:
        if skip_error:
            return None
        print(f"Error: failed to load input file: {ex}")
        sys.exit(1)


def load_solution(solution_dir: str):
    """Solution module loader"""
    file_path = os.path.relpath(f"{solution_dir}/solution.py")
    try:
        spec = importlib.util.spec_from_file_location("solution", file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules["solution"] = module
        spec.loader.exec_module(module)
        return module
    except Exception as ex:
        print(f"Error: failed to solution module: {ex}")
        sys.exit(1)


def main():
    """Main routine function"""
    parser = argparse.ArgumentParser(description="Solution runner script")
    parser.add_argument(
        "solution_dir",
        help="directory of the solution to run, e.g.: Day1",
    )

    args = parser.parse_args()
    solution_dir = args.solution_dir

    if not os.path.exists(solution_dir):
        print(f"Error: solution_dir does not exist: {solution_dir}")
        sys.exit(1)

    if not os.path.isdir(solution_dir):
        print(f"Error: solution_dir is not a directory: {solution_dir}")
        sys.exit(1)

    solution = load_solution(solution_dir)
    test_input_lines = load_file_lines(solution_dir, TEST_INPUT_FILENAME)
    test_input2_lines = load_file_lines(solution_dir, TEST_INPUT2_FILENAME, True)
    test_output_lines = load_file_lines(solution_dir, TEST_OUTPUT_FILENAME)
    test_solution_output = solution.solve(test_input_lines, test_input2_lines)
    test_output = ",".join(test_output_lines or [])
    is_passed = test_solution_output == test_output
    print(f"Solution test output: {test_solution_output}")
    print(f"Expected test output: {test_output}")
    print(f"Test run result: {'PASSED' if is_passed else 'FAILED'}")

    if is_passed:
        puzzle_input_lines = load_file_lines(solution_dir, PUZZLE_INPUT_FILENAME)
        puzzle_solution_output = solution.solve(puzzle_input_lines)
        print(f"Solution puzzle output: {puzzle_solution_output}")


if __name__ == "__main__":
    main()
