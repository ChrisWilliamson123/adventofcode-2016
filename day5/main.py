import md5


puzzle_input = 'ffykfhsq'
iterator = -1
password = ''
while len(password) != 8:
    iterator += 1
    m = md5.new('%s%d' % (puzzle_input, iterator))
    hexdigest = m.hexdigest()
    if hexdigest[0:5] == '00000':
        password += hexdigest[5]
print(password)
