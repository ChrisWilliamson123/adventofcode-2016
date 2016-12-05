def next_key(current_key, direction):
    # print(direction)
    # print(current_key)
    if direction == 'L' or direction == 'R':
        index_to_change = 1
    else:
        index_to_change = 0

    if direction == 'L' or direction == 'U':
        multiplier = -1
    else:
        multiplier = 1
    # print(current_key[index_to_change] + multiplier)
    if current_key[index_to_change] + multiplier > 2 or current_key[index_to_change] + multiplier < 0:
        return current_key
    else:
        current_key[index_to_change] += multiplier
        return current_key

input_file = open('input.txt', 'r')
key_presses = []
# Read the input into the key_presses list
for line in input_file:
    key_presses.append(list(line)[0:-1])

# Set up the keypad
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Start at 5
current_button = [1, 1]

for button_path in key_presses:
    for movement in button_path:
        current_button = next_key(current_button, movement)
    print(current_button)
