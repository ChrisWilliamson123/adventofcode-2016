import collections


input_file = open('input.txt', 'r')
messages = []
# Read the input into the messages list
for line in input_file:
    messages.append(line)

# Create a list to hold the messages by column first (so we'll have a 8x624 list)
by_column = []
for col_index in range(0, len(messages[0])-1):
    new_entry = []
    for row_index in range(0, len(messages)):
        new_entry.append(messages[row_index][col_index])
    by_column.append(new_entry)

error_corrected = ''
# Get the most common letter in each column and build up the final string
for column in by_column:
    # This gets a list of the letters in the string and their respective counts
    letters_with_counts = collections.Counter(column).most_common(1)
    error_corrected += letters_with_counts[0][0]
print(error_corrected)
