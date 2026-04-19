def solution(arr):
    min_val = min(arr)
    answer = [i for i in arr if i != min_val]
    return [-1] if not answer else answer