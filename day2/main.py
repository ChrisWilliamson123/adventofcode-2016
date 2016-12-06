def next_key(current_key, direction):
    if direction == 'L' or direction == 'R':
        index_to_change = 1
    else:
        index_to_change = 0

    if direction == 'L' or direction == 'U':
        multiplier = -1
    else:
        multiplier = 1
    
    next_key = list(current_key)
    if next_key[index_to_change] + multiplier < 0:
        return current_key
    next_key[index_to_change] += multiplier

    try:
        t = keypad[next_key[0]][next_key[1]]
        if keypad[next_key[0]][next_key[1]] == 0:
            return current_key
        return next_key
    except:
        return current_key

input_file = open('input.txt', 'r')
key_presses = []
# Read the input into the key_presses list
for line in input_file:
    key_presses.append(list(line.rstrip()))

# Set up the keypad
# Uncomment for part 1
# keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Uncomment for part 2
keypad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]

# Start at 5
current_button = [2, 0]

for button_path in key_presses:
    for movement in button_path:
        current_button = next_key(current_button, movement)
    print(keypad[current_button[0]][current_button[1]])
