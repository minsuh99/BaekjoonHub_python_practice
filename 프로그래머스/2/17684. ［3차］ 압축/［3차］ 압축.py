def solution(msg):
    answer = []
    index_dict = {chr(ord("A") + i - 1): i for i in range(1, 27)}
    idx = 27

    start = 0

    while start < len(msg):
        end = start + 1

        while end <= len(msg) and msg[start:end] in index_dict:
            end += 1

        w = msg[start:end-1]
        answer.append(index_dict[w])

        if end <= len(msg):
            index_dict[msg[start:end]] = idx
            idx += 1

        start = end - 1

    return answer