def solution(numbers):
    my_list = sorted([str(i) for i in numbers], key = lambda x: x * 4, reverse=True)

    return "".join(my_list) if my_list[0] != "0" else "0"