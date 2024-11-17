"""
Given an array of integers and a target, find two numbers such that they add up to the target.
"""


def two_sum(items: list[int], target: int) -> list[int]:
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

    # return []

    # Two pointers approach
    start = 0
    end = len(items) - 1

    for _ in range(len(items)):
        sum = items[start] + items[end]

        if sum < target:
            start = start + 1
        elif sum > target:
            end = end - 1
        else:
            return [start, end]

    return []
