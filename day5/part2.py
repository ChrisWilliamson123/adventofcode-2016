import md5

puzzle_input = 'ffykfhsq'
iterator = -1
password = [None]*8

while None in password:
    iterator += 1
    m = md5.new('%s%d' % (puzzle_input, iterator))
    hexdigest = m.hexdigest()
    if hexdigest[0:5] == '00000':
        try:
            index = int(hexdigest[5])
            if password[index] == None:
                password[index] = hexdigest[6]
        except:
            continue
print(password)
