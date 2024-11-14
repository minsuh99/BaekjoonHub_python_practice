sleep = int(input())
wake = int(input())

if sleep >= 20 and sleep <= 23:
    wake += 24
print(wake - sleep)