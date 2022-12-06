def get_signal():
    with open("input.txt", "r") as f:
        signal = f.read()
    return signal


def is_start_of_packet_marker(marker):

    return len(marker) == len(set(marker))


def find_start_of_packet_marker(signal, num_unique=4):
    marker = signal[0:num_unique]

    for i in range(num_unique, len(signal)):
        if is_start_of_packet_marker(marker):
            return i
        new_char = signal[i]
        marker = marker[1:] + new_char


def test_solution():
    test_signals = ["bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg",
                    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
    test_start_of_packet_marker = [5, 6, 10, 11]

    start_of_packet_marker = []

    for test_signal in test_signals:
        start_of_packet_marker.append(find_start_of_packet_marker(test_signal))

    assert (start_of_packet_marker == test_start_of_packet_marker)


test_solution()


def solutions():
    signal = get_signal()

    first_solution = find_start_of_packet_marker(signal)
    second_solution = find_start_of_packet_marker(signal, 14)

    print("First solution:", first_solution)
    print("Second solution:", second_solution)


solutions()
