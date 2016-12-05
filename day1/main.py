input_file = open('input.txt', 'r')
directions = []
# Read the input into the directions list
for line in input_file:
    for direction in line.split(', '):
        directions.append(direction)

# Set up initial coords and direction stuff
co_ords = [0, 0]
all_visited = []
compass_directions = ['N', 'E', 'S', 'W']
current_direction = 0
visited_twice = []

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

    # Loop through all the movements we need to do
    for i in range(1, int(blocks_to_walk)+1):
        # Update our position
        co_ords[co_ord_to_change] += multiplier
        # If this position has been visited, add to visited_twice list
        if co_ords in all_visited:
            visited_twice.append(list(co_ords))
        # Add our coord to out visited list
        all_visited.append(list(co_ords))

print('Final co-ords: ' + str(co_ords))
# Get the Manhattan distance
print('Minimum distance: ' + str(abs(co_ords[0]) + abs(co_ords[1])))
# Distance from the first point that has been visited twice
print(abs(visited_twice[0][0]) + abs(visited_twice[0][1]))
