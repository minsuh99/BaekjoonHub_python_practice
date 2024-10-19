word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alphabet in croatia:
    while word.find(alphabet) > -1:
        idx = word.find(alphabet)
        word = word.replace(alphabet, '*')

print(len(word))