def solution(a, b):
    answer = ''
    day_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    cur_weekday = 5
    cur_day = 0
    for i in range(a - 1):
        cur_day += day_of_month[i]
    cur_day += b - 1
    answer = weekday[(cur_weekday + cur_day) % 7]
    print(cur_day)
    return answer