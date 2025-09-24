"""
Link -> https://adventofcode.com/2024/day/2
====================================================================================
So we need to analyse a list of numbers and check the sequence
We can only say the report is unsafe if
 - the previous score is equal to the currnet one
 - if theres inconsistencies, if we see the first and second scores
 are increasing: we are assuming that, anything less than
====================================================================================

"""

from typing import Sequence


def check_stats(report: Sequence[int]) -> bool:
    # if first item is bigger than the 2nd item we know its decreasing
    return report[0] > report[1]


def decrease_check(report: Sequence[int]) -> bool:
    is_safe = True
    for i in range(0, len(report)-1):
        if report[i] > report[i+1] and ((report[i] - report[i+1]) <= 3):
            is_safe
            print(f"{report[i]}, {report[i+1]}")
        else:
            is_safe = False
            break

    return is_safe


def increase_check(report: Sequence[int]) -> bool:
    is_safe = True

    for i in range(0, len(report) - 1):
        if report[i] < report[i+1] and ((report[i+1] - report[i] <= 3)):
            print(f"{report[i]}, {report[i+1]}")
        else:
            is_safe = False
            break

    return is_safe


def main(report: Sequence[int]) -> None:
    is_decreasing = check_stats(report)
    if is_decreasing:
        print(decrease_check(report))
    else:
        print("the function verified that this report is increasing")
        print(increase_check(report))
    pass


decr = [7, 6, 4, 2, 1]
incr = [1, 3, 6, 7, 9]
t1 = [1, 2, 7, 8, 9]
t2 = [9, 7, 6, 2, 1]
t3 = [1, 3, 2, 4, 5]
t4 = [8, 6, 4, 4, 1]

main(t4)

# NOTE:Needs to be adjusted to work with 2d-arrays instead of 1d-arrays
# inside the main() you could just loop through the loop or if feeling fancy
# could use numpy. Mainly becuase I can't auth with my github on this PC
