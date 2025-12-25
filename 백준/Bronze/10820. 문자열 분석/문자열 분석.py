import sys
input = sys.stdin.readlines
my_list = input()

for sentence in my_list:
    lower, upper, digit, space = 0, 0, 0, 0
    for s in sentence:
        if s == " ":
            space += 1
        elif s.isdigit():
            digit += 1
        elif s.isalpha():
            if s.isupper():
                upper += 1
            else:
                lower += 1
        elif s == "\n":
            break
    print(lower, upper, digit, space)