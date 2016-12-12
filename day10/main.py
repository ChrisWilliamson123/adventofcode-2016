input_text = open('input.txt', 'r')
bot_instructions = []
for line in input_text:
  bot_instructions.append(line)

def parse_input(instructions):
  