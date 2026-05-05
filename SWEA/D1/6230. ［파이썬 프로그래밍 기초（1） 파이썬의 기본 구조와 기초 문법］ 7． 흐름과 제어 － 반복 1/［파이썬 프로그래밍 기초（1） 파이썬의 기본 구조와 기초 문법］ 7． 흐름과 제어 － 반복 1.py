score = [88, 30, 61, 55, 95]

for i in range(5):
    flag = "합격" if score[i] >= 60 else "불합격"
    print(f"{i + 1}번 학생은 {score[i]}점으로 {flag}입니다.")