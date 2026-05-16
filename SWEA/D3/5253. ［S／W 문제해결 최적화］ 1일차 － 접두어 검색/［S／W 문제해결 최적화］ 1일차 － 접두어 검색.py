T = int(input())

for test_case in range(1, T + 1):
    res = 0
    N, M = map(int, input().split())
    
    word_A = []
    word_B = []
    for _ in range(N):
        word_A.append(input())
    
    for _ in range(M):
        word_B.append(input())
    
    
    for b in word_B:
        for a in word_A:
            if a.startswith(b):
                res += 1
                break
    
    print(f"#{test_case} {res}")