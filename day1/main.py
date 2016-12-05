input_file = open('input.txt', 'r')
directions = []
# Read the input into the directions list
for line in input_file:
    for direction in line.split(', '):
        directions.append(direction)

# Set up initial coords and direction stuff
co_ords = [0, 0]
compass_directions = ['N', 'E', 'S', 'W']
current_direction = 0

# For each direction
for direction in directions:
    # Get the direction to turn and the distance
    turn = direction[0]
    blocks_to_walk = direction[1:]

    # If we are turning right, increment our direction index
    if turn == 'R':
        current_direction += 1
        if current_direction == 4:
            current_direction = 0
    # If we are turning left, decrement our direction index
    else:
        current_direction -= 1
        if current_direction == -1:
            current_direction = 3

    # Select the correct co-ord index to change
    if current_direction == 0 or current_direction == 2:
        co_ord_to_change = 1
    else:
        co_ord_to_change = 0

    # Set the multiplier so that we either increase or decrease the co-ords
    multiplier = 1
    if current_direction > 1:
        multiplier = -1

    # Change the co-ord value
    co_ords[co_ord_to_change] += int(blocks_to_walk)*multiplier

print('Final co-ords: ' + str(co_ords))
# Get the Manhattan distance
print('Minimum distance: ' + str(abs(co_ords[0]) + abs(co_ords[1])))
