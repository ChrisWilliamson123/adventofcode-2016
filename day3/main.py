def is_triangle(triangle_sides):
    return ( ((triangle_sides[0] + triangle_sides[1]) > triangle_sides[2]) and  ((triangle_sides[1] + triangle_sides[2]) > triangle_sides[0]) and ((triangle_sides[0] + triangle_sides[2]) > triangle_sides[1]))

input_file = open('input.txt', 'r')
def read_part_one(input_file):
    triangle_specs = []
    # Read the input into the triangle_specs list
    for line in input_file:
        triangle_specs.append([int(i) for i in line.split()])
    return triangle_specs

def read_part_two(input_file):
    rows = []
    for line in input_file:
        rows.append(line.split())
    columns = []
    for i in range(0, 3):
        columns.append([])
        for row in rows:
            columns[i].append(row[i])
    triangle_specs = []
    for col in range(0, len(columns)):
        for i in range(0, len(columns[col]), 3):
            triangle_specs.append([int(i) for i in columns[col][i:i+3]])
    print(triangle_specs)
    return triangle_specs

triangle_specs = read_part_two(input_file)
count = 0
for triangle in triangle_specs:
    if is_triangle(triangle):
        count += 1
print(count)
