seq = input()
ball = [1, 0, 0]

for s in seq:
    if s == "A":
        ball[0], ball[1] = ball[1], ball[0]
    elif s == "B":
        ball[1], ball[2] = ball[2], ball[1]
    elif s == "C":
        ball[0], ball[2] = ball[2], ball[0]

print(ball.index(1) + 1)