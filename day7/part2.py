import re

input_file = open('input.txt', 'r') 
ip_addresses = []
for line in input_file:
    ip_addresses.append(line.rstrip())

def in_supernet(aba, ip):
    # There are 3 regexes here (beacuse I don't know how to do all 3 in one)
    # 1) Will match 0-* a-z/A-Z characters, then our aba match followed by 0-* a-z/A-Z characters then an open bracket e.g. yhjsabalop[
    # 2) Will match ] then 0-* a-z/A-Z then our match then 0-* a-z/A-Z then [ e.g. ]dopabaerq[
    # 1) Will match ] then 0-* a-z/A-Z characters, then our aba match followed by 0-* a-z/A-Z characters e.g. ]gyrabaors
    # These three regexes cover all possibilities of the aba match being in the supernet sequence
    return re.search(r'[a-zA-Z]*' + aba + '[a-zA-Z]*[\[]', ip) or re.search(r'[\]][a-zA-Z]*' + aba + '[a-zA-Z]*[\[]', ip) or re.search(r'[\]][a-zA-Z]*' + aba + '[a-zA-Z]*', ip)

def in_hypernet(bab, ip):
    return re.findall(r'[\[][a-zA-Z]*' + bab + '[a-zA-Z]*[\]]', ip)

valid_ips = []

for ip in ip_addresses:
    valid = False
    # Check if there are any ABA matches
    abas = [''.join(match) for match in re.findall(r'(?=(\w)(\w)(\1))', ip)]    
    matches_index = 0
    while not valid and matches_index < len(abas):
        match = abas[matches_index]
        bab = match[1] + match[0] + match[1]
        if in_supernet(match, ip) and in_hypernet(bab, ip):
            valid_ips.append(ip)
            valid = True
        matches_index += 1
print(len(valid_ips))
