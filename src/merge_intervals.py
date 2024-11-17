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
    # Stack approach
    stack = []

    for interval in intervals:
        if len(stack) == 0 or stack[-1][1] < interval[0]:
            stack.append(interval)
        else:
            stack[-1][1] = max(stack[-1][1], interval[1])

    return stack
