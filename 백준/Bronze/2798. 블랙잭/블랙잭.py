from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
card = [int(i) for i in input().split()]
print(max([sum(i) for i in list(combinations(card, 3)) if sum(i) <= M]))