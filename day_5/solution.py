import re
import copy


def split_input(input):
    input = input.split("\n\n")

    stacks = input[0]
    moves = input[1]

    return stacks, moves


def generate_moves(moves_input):
    # Removes all the words from the string
    return re.sub("[^0-9]+", ",", moves_input).split(",")[1:]


def generate_stacks(stacks_input):
    stacks_input = stacks_input.split("\n")

    del stacks_input[-1]  # Don't need the last row of numbers
    n = 4
    stacks_input = [[line[i:i+n].strip() for i in range(0, len(line), n)]
                    for line in stacks_input]

    num_stacks = len(stacks_input[-1])

    stacks = [[i+1] for i in range(num_stacks)]
    for i in range(-1, -len(stacks_input)-1, -1):
        for j, cargo in enumerate(stacks_input[i]):
            if cargo != '':
                stacks[j].append(cargo)
    return stacks


def move_cargo(stacks, moves, cratemover_9001=False):
    for i in range(0, len(moves), 3):
        number, frm, to = int(moves[i]), int(moves[i+1])-1, int(moves[i+2])-1
        if cratemover_9001 is True:
            crates_to_move = stacks[frm][-1:-number-1:-1]
            crates_to_move.reverse()
            stacks[to] += crates_to_move
            for _ in range(number):
                stacks[frm].pop()
        else:
            for _ in range(number):
                stacks[to].append(stacks[frm].pop())

    return stacks


def get_top_cargo(stacks):
    return ''.join(re.sub(r"[^A-Z]", "", stack[-1]) for stack in stacks if stack)


def test_solution():
    test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    test_stacks_input, test_moves_input = split_input(test_input)

    test_moves = generate_moves(test_moves_input)
    test_stacks = generate_stacks(test_stacks_input)
    test_stacks_2 = copy.deepcopy(test_stacks)

    test_stacks = move_cargo(test_stacks, test_moves)
    test_stacks_2 = move_cargo(test_stacks_2, test_moves, cratemover_9001=True)

    assert (get_top_cargo(test_stacks) == "CMZ")
    assert (get_top_cargo(test_stacks_2) == "MCD")


test_solution()


def get_input():
    with open("input.txt", "r") as f:
        input = f.read()
    return input


def solutions():
    input = get_input()

    stacks_input, moves_input = split_input(input)
    moves = generate_moves(moves_input)
    stacks = generate_stacks(stacks_input)
    stacks_2 = copy.deepcopy(stacks)

    stacks = move_cargo(stacks, moves)
    stacks_2 = move_cargo(stacks_2, moves, cratemover_9001=True)

    print("Solution 1: " + get_top_cargo(stacks))
    print("Solution 2: " + get_top_cargo(stacks_2))


solutions()
