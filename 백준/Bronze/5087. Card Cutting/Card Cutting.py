import sys

while True:
    input_list = sys.stdin.readline().strip()
    if input_list == '#':
        break
    card_list = " ".join([i for i in input_list.split()])
    card_list = card_list.replace('A', '1')
    card_list = [int(i) for i in card_list.split()[:-1]]

    cheryl = 0
    tania = 0

    for num in card_list:
        if num % 2 == 0:
            tania += 1
        else:
            cheryl += 1

    if cheryl == tania:
        print("Draw")
    elif cheryl > tania:
        print("Cheryl")
    else:
        print("Tania")