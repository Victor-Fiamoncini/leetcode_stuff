"""
Given an array of integers and a target, find two numbers such that they add up to the target.
"""


def two_sum(items: list[int], target: int) -> list[int] | None:
    # Brute force approach
    # for i in range(len(items)):
    #     for j in range(i + 1, len(items)):
    #         if items[i] + items[j] == target:
    #             return [i, j]

    # Hashmap approach
    # visited = {}

    # for index, item in enumerate(items):
    #     complement = target - item

    #     if complement in visited:
    #         return [visited[complement], index]

    #     visited[item] = index

    # Two pointers approach
    start = 0
    end = len(items) - 1

    while start < end:
        sum = items[start] + items[end]

        if sum == target:
            return [start, end]
        elif sum < target:
            start = start + 1
        else:
            end = end - 1

    return None
