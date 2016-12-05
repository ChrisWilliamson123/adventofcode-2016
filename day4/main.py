import collections

# This function splits the initial encrypted room name into it's parts
def split_name(name):
    letters = ''.join(name.split('-')[0:-1])
    sectorID = name.split('-')[-1].split('[')[0]
    checksum = name.split('[')[1][0:-1]
    return [letters, sectorID, checksum]

def shift_cipher(string, shift_amount):
    # Mod with 26 to get the actual shift amount
    shift_amount %= 26
    # Initialise a string which will hold our final shifted string
    new_string = ''
    # Loop through each character
    for character in string:
        upper = character.upper()
        # If the shift loops round to the start of the alphabet, get the correct character
        if ord(upper) + shift_amount > 90:
            new_char = chr(64 + ((ord(upper) + shift_amount) - 90))
        else:
            # Add the shift amount like normal
            new_char = chr(ord(upper) + shift_amount)
        new_string += new_char
    return new_string

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
        if letters_in_order[i][0] != checksum[i]:
            return False
    return True

input_file = open('input.txt', 'r')
encrypted_names = []
# Read the input into the encrypted_names list
for line in input_file:
    encrypted_names.append(line.rstrip())

sectorID_sum = 0
north_pole_room_ID = 0
for name in encrypted_names:
    split = split_name(name)
    letters = split[0]
    sectorID = int(split[1])
    checksum = list(split[2])
    if is_real_room(letters, checksum):
        sectorID_sum += sectorID
        if shift_cipher(letters, sectorID) == 'NORTHPOLEOBJECTSTORAGE':
            north_pole_room_ID = sectorID

print('Sum of sector IDs: ' + str(sectorID_sum))
print('North pole object storage sector ID: ' + str(north_pole_room_ID))

