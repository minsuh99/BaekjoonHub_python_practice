def solution(A, B):
    A.sort()
    B.sort()

    a_idx, b_idx = 0, 0
    score = 0

    while a_idx < len(A) and b_idx < len(B):
        if B[b_idx] > A[a_idx]:
            score += 1
            a_idx += 1
            b_idx += 1
        else:
            b_idx += 1

    return score