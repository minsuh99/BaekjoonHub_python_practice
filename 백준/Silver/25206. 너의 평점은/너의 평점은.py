degree = []
score = []

def grade2score(grade):
    match grade:
        case 'A+':
            return 4.5
        case 'A0':
            return 4.0
        case 'B+':
            return 3.5
        case 'B0':
            return 3.0
        case 'C+':
            return 2.5
        case 'C0':
            return 2.0
        case 'D+':
            return 1.5
        case 'D0':
            return 1.0
        case 'F':
            return 0.0

for _ in range(20):
    _, d, g = map(str, input().split())
    if g != 'P':
        degree.append(float(d))
        score.append(grade2score(g))

res = [degree[i] * score[i] for i in range(len(degree))]
print(sum(res)/sum(degree))