T = int(input())
for _ in range(T):
    n, word = input().split()
    for letter in word:
        print(letter*int(n), end="")
    print()