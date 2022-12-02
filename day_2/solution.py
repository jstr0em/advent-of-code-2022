with open("input.txt", "r") as f:
    strategy_guide = f.read().splitlines()
    strategy_guide = [round.split(" ") for round in strategy_guide]

shape_scores = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3 }

test_rounds = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]


def outcome(shape_1, shape_2):
    if shape_1 == 'A':
        if shape_2 == 'X' or shape_2 == 'A':
            return 3
        elif shape_2 == 'Y' or shape_2 == 'B':
            return 6
        elif shape_2 == 'Z' or shape_2 == 'C':
            return 0
    elif shape_1 == 'B':
        if shape_2 == 'X' or shape_2 == 'A':
            return 0
        elif shape_2 == 'Y' or shape_2 == 'B':
            return 3
        elif shape_2 == 'Z' or shape_2 == 'C':
            return 6
    elif shape_1 == 'C':
        if shape_2 == 'X' or shape_2 == 'A':
            return 6
        elif shape_2 == 'Y' or shape_2 == 'B':
            return 0
        elif shape_2 == 'Z' or shape_2 == 'C':
            return 3


def part_one(rounds):
    total_score = 0
    for round in rounds:
        opponent_choice = round[0]
        my_choice = round[1]

        outcome_score = outcome(opponent_choice, my_choice)
        shape_score = shape_scores[my_choice]

        total_score += outcome_score + shape_score
    return total_score


def get_correct_choice(opponent_choice, desired_outcome):
    if desired_outcome == 'X':
        if opponent_choice == 'A':
            return 'C'
        elif opponent_choice == 'B':
            return 'A'
        elif opponent_choice == 'C':
            return 'B'
    elif desired_outcome == 'Y':
        return opponent_choice
    elif desired_outcome == 'Z':
        if opponent_choice == 'A':
            return 'B'
        elif opponent_choice == 'B':
            return 'C'
        elif opponent_choice == 'C':
            return 'A'
            

def part_two(rounds):
    total_score = 0
    for round in rounds:
        opponent_choice = round[0]
        desired_outcome = round[1]
        my_choice = get_correct_choice(opponent_choice, desired_outcome)

        outcome_score = outcome(opponent_choice, my_choice)
        shape_score = shape_scores[my_choice]

        total_score += outcome_score + shape_score
    return total_score


assert(part_one(test_rounds) == 15)
assert(part_two(test_rounds) == 12)

print(part_one(strategy_guide))
print(part_two(strategy_guide))