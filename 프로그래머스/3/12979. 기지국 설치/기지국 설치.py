def solution(n, stations, w):
    answer = 0
    cur_idx = 0
    RANGE = 2 * w + 1
    for station in stations:
        left = max(0, station - 1 - w)
        right = min(n - 1, station - 1 + w)
        if cur_idx < left:
            no_elec = left - cur_idx
            answer += no_elec // RANGE if no_elec % RANGE == 0 else no_elec // RANGE + 1
        cur_idx = right + 1
    if cur_idx < n:
        no_elec = n - cur_idx
        answer += no_elec // RANGE if no_elec % RANGE == 0 else no_elec // RANGE + 1
    return answer