science_score = []
society_score = []

for _ in range(4):
    science_score.append(int(input()))
for _ in range(2):
    society_score.append(int(input()))

science_score.sort()
society_score.sort()

print(sum(science_score[1:]) + society_score[-1])