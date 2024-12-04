n = int(input())

earth = 0
aboriginal = 0
another = 0
for _ in range(n):
    response = input()
    blue = 'blue' in response
    black = 'black' in response
    white = 'white' in response
    gold = 'gold' in response
    if blue and black:
        earth += 1
    elif white and gold:
        aboriginal += 1
    else:
        another += 1
print(earth / n * 100)
print(aboriginal / n * 100)
print(another / n * 100)