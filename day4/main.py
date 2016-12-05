import collections

# This function splits the initial encrypted room name into it's parts
def split_name(name):
    letters = ''.join(name.split('-')[0:-1])
    sectorID = name.split('-')[-1].split('[')[0]
    checksum = name.split('[')[1][0:-1]
    return [letters, sectorID, checksum]

# This function will return True if the room is real
def is_real_room(letters, checksum):
    # This gets a list of the letters in the string and their respective counts
    letters_with_counts = collections.Counter(letters).most_common()
    # This sorts the letters list we have, firstly on most frequent, then on alphabetical order
    # We then get the first 5, as that's how long the checksum is
    letters_in_order = sorted(letters_with_counts, key=lambda entry: (-entry[1], entry[0]))[0:5]
    # Loop through the letters
    for i in range(0, len(letters_in_order)):
        # Compare the letters with the respective letter in the checksum
        # If it doesn't match, return False
        if most_common_letters[i][0] != checksum[i]:
            return False
    return True

input_file = open('input.txt', 'r')
encrypted_names = []
# Read the input into the encrypted_names list
for line in input_file:
    encrypted_names.append(line.rstrip())

sectorID_sum = 0
for name in encrypted_names:
    split = split_name(name)
    letters = split[0]
    sectorID = split[1]
    checksum = list(split[2])
    if is_real_room(letters, checksum):
        sectorID_sum += int(sectorID)
print(sectorID_sum)
