"""Advent of Code 2024 Solution Runner"""

import argparse
import importlib
import importlib.util
import os
import sys

from typing import List


TEST_INPUT_FILENAME = "test_input.txt"
TEST_OUTPUT_FILENAME = "test_output.txt"
PUZZLE_INPUT_FILENAME = "puzzle_input.txt"


def load_file_lines(dir: str, filename: str) -> List[str]:
    """Input file loader"""
    file_path = os.path.relpath(f"{dir}/{filename}")
    try:
        with open(file_path, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
            return lines
    except Exception as ex:
        print(f"Error: failed to load input file: {ex}")
        sys.exit(1)


def load_solution(dir: str):
    """Solution module loader"""
    file_path = os.path.relpath(f"{dir}/solution.py")
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
    parser.add_argument(
        "-t",
        "--test",
        help="run using the test input and validate output",
        action="store_true",
    )

    args = parser.parse_args()
    solution_dir = args.solution_dir
    input_filename = PUZZLE_INPUT_FILENAME

    if not os.path.exists(solution_dir):
        print(f"Error: solution_dir does not exist: {solution_dir}")
        sys.exit(1)

    if not os.path.isdir(solution_dir):
        print(f"Error: solution_dir is not a directory: {solution_dir}")
        sys.exit(1)

    if args.test:
        input_filename = TEST_INPUT_FILENAME

    input_lines = load_file_lines(solution_dir, input_filename)
    solution = load_solution(solution_dir)
    output = ",".join(solution.solve(input_lines))
    print(f"Solution output: {output}")

    if args.test:
        test_output_lines = load_file_lines(solution_dir, TEST_OUTPUT_FILENAME)
        test_output = ",".join(test_output_lines)
        print(f"Expected test output: {test_output}")
        print(f"Test run result: {'PASSED' if output == test_output else 'FAILED'}")


if __name__ == "__main__":
    main()
