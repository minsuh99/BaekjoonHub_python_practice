T = int(input())

for test_case in range(1, T + 1):
    A = input().strip()
    north = 'N' in A
    south = 'S' in A
    east = 'E' in A
    west = 'W' in A

    if north != south or east != west:
        print("No")
    else:
        print("Yes")
