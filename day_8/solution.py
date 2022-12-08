import collections


def read_input(path="input.txt"):
    with open(path) as file:
        lines = file.readlines()

    inputs = [[int(elem) for elem in line.rstrip()] for line in lines]
    return inputs


def test_solution():
    test_trees = read_input("test_input.txt")
    visible_trees = check_rows(test_trees).union(check_columns(test_trees))

    assert (len(visible_trees) == 21)


def solution_1():
    trees = read_input()

    visible_trees = check_rows(trees).union(check_columns(trees))

    print("Solution 1:", len(visible_trees))


def check_rows(trees):
    visible_trees = set()

    m = len(trees)
    for rx, row in enumerate(trees):
        max_left = -1
        max_right = -1

        for cx, elem in enumerate(trees[rx]):
            if elem > max_left:
                visible_trees.add((rx, cx))
                max_left = elem
            if trees[rx][-cx-1] > max_right:
                visible_trees.add((rx, m-cx-1))
                max_right = trees[rx][-cx-1]
    return visible_trees


def check_columns(trees):
    visible_trees = set()

    n = len(trees[0])
    for cx in range(n):
        max_top = -1
        max_bottom = -1

        for rx in range(len(trees)):
            if trees[rx][cx] > max_top:
                visible_trees.add((rx, cx))
                max_top = trees[rx][cx]
            if trees[-rx-1][cx] > max_bottom:
                visible_trees.add((n-rx-1, cx))
                max_bottom = trees[-rx-1][cx]

    return visible_trees


def solution_2():
    trees = read_input()

    scores = [[True]*len(trees[0]) for _ in range(len(trees))]

    score_rows(trees, scores)
    score_columns(trees, scores)

    result = max(max(row) for row in scores)
    print("Solution 2:", result)


def score_rows(matrix, scores):

    for rx, row in enumerate(matrix):

        stack_left = collections.deque()
        stack_right = collections.deque()

        for cx, elem in enumerate(row):

            while stack_left and stack_left[-1][0] < elem:
                stack_left.pop()
            while stack_right and stack_right[-1][0] < row[-cx-1]:
                stack_right.pop()

            scores[rx][cx] *= cx - stack_left[-1][1] if stack_left else cx
            scores[rx][-cx-1] *= cx - stack_right[-1][1] if stack_right else cx

            stack_left.append((elem, cx))
            stack_right.append((row[-cx-1], cx))


def score_columns(matrix, scores):

    for cx in range(len(matrix[0])):

        stack_top = collections.deque()
        stack_bottom = collections.deque()

        for rx in range(len(matrix)):

            while stack_top and stack_top[-1][0] < matrix[rx][cx]:
                stack_top.pop()
            while stack_bottom and stack_bottom[-1][0] < matrix[-rx-1][cx]:
                stack_bottom.pop()

            scores[rx][cx] *= rx - stack_top[-1][1] if stack_top else rx
            scores[-rx-1][cx] *= rx - \
                stack_bottom[-1][1] if stack_bottom else rx

            stack_top.append((matrix[rx][cx], rx))
            stack_bottom.append((matrix[-rx-1][cx], rx))


if __name__ == '__main__':
    test_solution()
    solution_1()
    solution_2()
