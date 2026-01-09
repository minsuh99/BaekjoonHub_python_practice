import sys
input = sys.stdin.readline

N = int(input())
rank_list = [1 for _ in range(N)]
people = []

for i in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))
    if i == 0:
        continue
    for j in range(i):
        if weight > people[j][0] and height > people[j][1]:
            rank_list[j] += 1
        elif weight < people[j][0] and height < people[j][1]:
            rank_list[i] += 1
        
print(*rank_list)