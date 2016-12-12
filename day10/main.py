def parse_input(bot_instructions):
    value_assignments = []
    give_assignments = []
    for instruction in bot_instructions:
        instruction_split = instruction.split(' ')
        if instruction_split[0] == 'value':
            value_assignments.append((int(instruction_split[1]), int(instruction_split[-1])))
        else:
            give_assignments.append([
                int(instruction_split[1]),
                instruction_split[5],
                int(instruction_split[6]),
                instruction_split[-2],
                int(instruction_split[-1])
            ])
    return (value_assignments, [x for x in give_assignments if x is not None])

def set_high_low(bot, value, bots):
    if value >= bots[bot]['high']:
        bots[bot]['low'] = int(bots[bot]['high'])
        bots[bot]['high'] = value
    else:
        bots[bot]['low'] = value

def send_to_output(output, value, outputs):
    outputs[output] = value

def perform_trades(give_assignments, bots, outputs):
    
    incomplete = []
    for trade in give_assignments:
        giver = bots[trade[0]]
        if giver['low'] != 0 and giver['high'] != 0:
            low_receiver = trade[2]
            high_receiver = trade[4]
            if trade[1] == 'output':
                send_to_output(low_receiver, giver['low'], outputs)
            else:
                set_high_low(low_receiver, giver['low'], bots)
            if trade[3] == 'output':
                send_to_output(high_receiver, giver['high'], outputs)
            else:
                set_high_low(high_receiver, giver['high'], bots)
        else:
            incomplete.append(trade)
    give_assignments = incomplete
    return give_assignments

def main():
    input_text = open('input.txt', 'r')
    bot_instructions = []
    for line in input_text:
      bot_instructions.append(line.rstrip())

    bots = [{'high': 0, 'low': 0} for i in range(0, 250)]
    outputs = [0 for i in range(0, 25)]
    # Parse the input to separate initial value assignments and trade assignments
    value_assignments, give_assignments = parse_input(bot_instructions)

    for value in value_assignments:
        set_high_low(value[1], value[0], bots)

    while len(give_assignments) != 0:
        give_assignments = perform_trades(give_assignments, bots, outputs)

    bots = [x for x in bots if x['high'] != 0]
    for index in range(0, len(bots)):
        bot = bots[index]
        if bot['high'] == 61 and bot['low'] == 17:
            print(index)
    outputs = [x for x in outputs if x != 0]
    print(outputs[0] * outputs[1] * outputs[2])

if __name__ == '__main__':
    main()
