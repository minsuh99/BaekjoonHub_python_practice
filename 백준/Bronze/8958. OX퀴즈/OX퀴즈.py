T = int(input())

for _ in range(T):
    final = 0
    score = 1
    res = input()
    for ans in res:
        if ans == "O":
            final += score
            score += 1
        elif ans == 'X':
            score = 1
    print(final)