"""
Merge overlapping intervals from a list of intervals.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    no_overlaping_intervals = []

    for index in range(len(intervals)):
        left = intervals[index][0]
        right = intervals[index][1]

        if index == len(intervals) - 1:  # it's the last pair
            no_overlaping_intervals.append([left, right])

            return no_overlaping_intervals

        next_left = intervals[index + 1][0]
        next_right = intervals[index + 1][1]

        if right >= next_left:
            no_overlaping_intervals.append([left, next_right])

    return no_overlaping_intervals
