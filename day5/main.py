import md5


puzzle_input = 'ffykfhsq'
iterator = -1
password = [None]*8
current_index = 0
while password[7] == None:
    iterator += 1
    m = md5.new('%s%d' % (puzzle_input, iterator))
    hexdigest = m.hexdigest()
    if hexdigest[0:5] == '00000':
        password[current_index] = hexdigest[5]
        current_index += 1
print(''.join(password))
