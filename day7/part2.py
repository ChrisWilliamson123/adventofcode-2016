import re

input_file = open('input.txt', 'r') 
ip_addresses = []
for line in input_file:
    ip_addresses.append(line.rstrip())

valid_ips = []

for ip in ip_addresses:
    valid = False
    # Check if there are any ABA matches
    abas = [''.join(match) for match in re.findall(r'(?=(\w)(\w)(\1))', ip)]
    if ip == 'igefoemugshofmibco[uhahihzaglmzdpzjvfp]tfbuuhoughgismec[inbtuzxnxekfkulodyk]fxykxfkfnjvswwc':
        print(abas)
    matches_index = 0
    while not valid and matches_index < len(abas):
        match = abas[matches_index]
        # igefoemugshofmibco[uhahihzaglmzdpzjvfp]tfbuuhoughgismec[inbtuzxnxekfkulodyk]fxykxfkfnjvswwc
        aba_in_supernet = re.search(r'[a-zA-Z]*' + match + '[a-zA-Z]*[\[]', ip) or re.search(r'[\]][a-zA-Z]*' + match + '[a-zA-Z]*[\[]', ip) or re.search(r'[\]][a-zA-Z]*' + match + '[a-zA-Z]*', ip)
        if ip == 'igefoemugshofmibco[uhahihzaglmzdpzjvfp]tfbuuhoughgismec[inbtuzxnxekfkulodyk]fxykxfkfnjvswwc' and match == 'fkf':
            print(aba_in_supernet)

        bab = match[1] + match[0] + match[1]
        bab_in_hypernet = re.findall(r'[\[][a-zA-Z]*' + bab + '[a-zA-Z]*[\]]', ip)

        if aba_in_supernet and bab_in_hypernet:
            valid_ips.append(ip)
            valid = True
            print(ip) 
            # print(match, bab)
        matches_index += 1
print(len(valid_ips))