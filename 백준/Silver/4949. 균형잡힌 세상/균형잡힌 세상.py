import sys


while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    check_string = ""
    for s in sentence:
        if s not in '()[]':
            continue
        else:
            check_string += s
    for _ in range(len(check_string)):
        check_string = check_string.replace('()', '')
        check_string = check_string.replace('[]', '')

    if len(check_string) > 0:
        print("no")
    else:
        print("yes")

# 다시 생각해보기
