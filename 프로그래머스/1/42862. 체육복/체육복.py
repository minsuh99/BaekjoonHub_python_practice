def solution(n, lost, reserve):
    overlap = set(lost) & set(reserve)
    lost = set(lost) - overlap
    reserve = set(reserve) - overlap

    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)