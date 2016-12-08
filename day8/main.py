def print_screen(screen):
    for row in screen:
        print(row)
    print('\n')

def get_instruction_type(instruction):
    return instruction.split(' ')[0]

def rect(instruction, screen):
    dimensions = instruction.split(' ')[1]
    width = int(dimensions.split('x')[0])
    height = int(dimensions.split('x')[1])
    for row_index in range(0, height):
        for column_index in range(0, width):
            screen[row_index][column_index] = 1

def rotate_list(l, amount):
    n = len(l) - amount
    return l[n:] + l[:n]

def rotate(instruction, screen):
    instruction_split = instruction.split(' ')
    rotation_type = instruction_split[1]
    rotation_index = int(instruction_split[2].split('=')[1])
    rotation_amount = int(instruction_split[4])

    if rotation_type == 'row':
        current_row_status = list(screen[rotation_index])
        new_row = rotate_list(current_row_status, rotation_amount)
        screen[rotation_index] = new_row
    else:
        current_column_status = list([row[rotation_index] for row in screen])
        new_column = rotate_list(current_column_status, rotation_amount)
        for row_index in range(0, len(screen)):
            screen[row_index][rotation_index] = new_column[row_index]

def get_message(screen):
    for col_index in range(0, len(screen[0]), 5):
        for row_index in range(0, len(screen)):
            row = ''
            for value in screen[row_index][col_index:col_index+5]:
                if value:
                    row += '.'
                else:
                    row += ' '
            print(row)
        print('\n')


def main():
    input_file = open('input.txt', 'r') 
    instructions = []
    for line in input_file:
        instructions.append(line.rstrip())

    screen = []
    for i in range(0, 6):
        screen.append([0] * 50)

    for instruction in instructions:
        i_type = get_instruction_type(instruction)
        if i_type == 'rect':
            rect(instruction, screen)
        else:
            rotate(instruction, screen) 

    on_leds = 0
    for row in screen:
        for column in row:
            if column:
                on_leds += 1
    print(on_leds)
    get_message(screen)

if __name__ == '__main__':
    main()
