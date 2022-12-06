def get_rugsacks():
    with open("input.txt", "r") as f:
        rugsacks = f.read().splitlines()
    return rugsacks


def get_compartments(rugsacks):
    compartments = [[items[:len(items)//2], items[len(items)//2:]]
                    for items in rugsacks]

    return compartments


def find_common_items(compartment_1, compartment_2):
    compartment_1 = set(compartment_1)
    compartment_2 = set(compartment_2)

    common_items = compartment_1 & compartment_2

    return ''.join(str(item) for item in common_items)


def get_item_value(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    elif item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return 0


def find_common_items_2(items):

    item1 = set(items[0])
    item2 = set(items[1])
    item3 = set(items[2])

    common_items = item1 & item2 & item3

    return ''.join(str(item) for item in common_items)


# Test solution
def test_solution():
    # Test data
    test_common_items = ['p', 'L', 'P', 'v', 't', 's']
    test_common_items_values = [16, 38, 42, 22, 20, 19]
    test_items_sum = sum(test_common_items_values)

    test_compartments = get_compartments(test_rugsacks)
    common_items = [find_common_items(compartment_1, compartment_2)
                    for compartment_1, compartment_2 in test_compartments]
    assert (test_common_items == common_items)

    common_items_values = [get_item_value(item) for item in common_items]
    assert (test_common_items_values == common_items_values)

    items_sum = sum(common_items_values)
    assert (test_items_sum == items_sum)


test_rugsacks = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg",
                 "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
test_solution()


# Solution 1
def solution_1(rugsacks):

    compartments = get_compartments(rugsacks)
    common_items = [find_common_items(
        compartment_1, compartment_2) for compartment_1, compartment_2 in compartments]
    common_items_values = [get_item_value(item) for item in common_items]
    items_sum = sum(common_items_values)

    print(items_sum)


rugsacks = get_rugsacks()
solution_1(rugsacks)

# Solution 2


def test_solution_2():
    test_common_items = ['r', 'Z']
    test_common_items_values = [18, 52]
    test_items_sum = 70

    common_items = []
    for i in range(0, len(test_rugsacks), 3):
        common_items.append(find_common_items_2(test_rugsacks[i:i+3]))

    assert (common_items == test_common_items)

    common_items_values = [get_item_value(item) for item in common_items]
    assert (test_common_items_values == common_items_values)

    items_sum = sum(common_items_values)
    assert (test_items_sum == items_sum)


test_solution_2()


def solution_2(rugsacks):
    common_items = []
    for i in range(0, len(rugsacks), 3):
        common_items.append(find_common_items_2(rugsacks[i:i+3]))

    common_items_values = [get_item_value(item) for item in common_items]

    items_sum = sum(common_items_values)

    print(items_sum)


solution_2(rugsacks)
