import re


def is_inside_brackets(full_ip, four_chars):
    return re.search(r'[\[][a-zA-Z]*' + four_chars + r'[a-zA-Z]*[\]]', full_ip)

def all_chars_same(four_chars):
    return four_chars == len(four_chars) * four_chars[0]

input_file = open('input.txt', 'r') 
ip_addresses = []
for line in input_file:
    ip_addresses.append(line.rstrip())

valid_ips = []
for ip in ip_addresses:
    # Find a character sequence such as 'abba'
    search_result = [''.join(result) + ''.join(result)[::-1] for result in re.findall(r'(.)(.)\2\1', ip)]
    if len(search_result):
        valid = True
        # Can have more than one result from the regex, so loop through them
        for result in search_result:
            if is_inside_brackets(ip, result) or all_chars_same(result):
                valid = False
        if valid:
            valid_ips.append([ip, result])
print(len(valid_ips))
