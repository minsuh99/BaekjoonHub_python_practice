import sys

vowel = ['a', 'e', 'i', 'o', 'u', 'y']
while True:
    word = sys.stdin.readline().strip().lower()
    
    if word == 'quit!':
        break
    else:
        if len(word) > 4 and word.endswith('or') and word[-3] not in vowel:
            word = word[:-2] + 'our'
    print(word)
