codes = {
    '000000': 'A',
    '001111': 'B',
    '010011': 'C',
    '011100': 'D',
    '100110': 'E',
    '101001': 'F',
    '110101': 'G',
    '111010': 'H'
}


n = int(input())
letters = input()
output = ''

for i in range(n):
    check_letter = letters[i * 6 : (i + 1) * 6]
    if check_letter in codes.keys():
        output += codes[check_letter]
    else:
        candidate = ''
        for code in codes.keys():
            error = sum([1 for j in range(len(code)) if check_letter[j] != code[j]])
            if error < 2:
                candidate += codes[code]
        
        if len(candidate) == 0:
            output = i + 1
            break
        else:
            output += candidate

print(output)