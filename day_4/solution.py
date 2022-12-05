def has_common_range(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    elif range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    else:
        return False

def has_overlap(range1, range2):
    if range1[1] < range2[0]:
        return False
    elif range2[1] < range1[0]:
        return False
    else:
        return True

def find_common_ranges_in_pairs(pairs, comperator=has_common_range):
    num_common_ranges = 0
    for pair in pairs:
        range1, range2 = pair
        if comperator(range1, range2):
            num_common_ranges += 1
    return num_common_ranges

def test_solution():
    # Test data
    test_pairs = [  [(2,4), (6,8)], 
                    [(2,3), (4,5)], 
                    [(5,7), (7,9)],  
                    [(2,8), (3,7)], 
                    [(6,6), (4,6)],
                    [(2,6), (4,8)]    ]

    num_common_ranges = find_common_ranges_in_pairs(test_pairs) 
    num_overlaps = find_common_ranges_in_pairs(test_pairs, comperator=has_overlap)
    assert(num_common_ranges == 2)
    assert(num_overlaps == 4)
test_solution()

def get_pairs():
    with open("input.txt", "r") as f:
        pairs = f.read().splitlines()
    pairs = [[tuple( map(int, elf.split('-')) ) for elf in pair.split(',')] for pair in pairs]
    return pairs
pairs = get_pairs()

def solution_1():
    print(find_common_ranges_in_pairs(pairs))
solution_1()

def solution_2():
    print(find_common_ranges_in_pairs(pairs, comperator=has_overlap))
solution_2()