N = int(input())

for i in range(N):
    word_list = input().split()
    temp = " ".join(word_list[::-1])
    print(f"Case #{i+1}: {temp}")