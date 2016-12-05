def is_triangle(triangle_sides):
    return ( ((triangle_sides[0] + triangle_sides[1]) > triangle_sides[2]) and  ((triangle_sides[1] + triangle_sides[2]) > triangle_sides[0]) and ((triangle_sides[0] + triangle_sides[2]) > triangle_sides[1]))

input_file = open('input.txt', 'r')
triangle_specs = []
# Read the input into the triangle_specs list
for line in input_file:
    triangle_specs.append([int(i) for i in line.split()])

count = 0
for triangle in triangle_specs:
    if is_triangle(triangle):
        count += 1
print(count)

