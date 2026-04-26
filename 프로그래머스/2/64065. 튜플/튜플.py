def solution(s):
    answer = []
    seen = set()

    my_list = s[2:-2].split("},{")
    my_list = [list(map(int, x.split(","))) for x in my_list]
    my_list.sort(key=len)

    for group in my_list:
        for num in group:
            if num not in seen:
                answer.append(num)
                seen.add(num)

    return answer