def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True


def solution(numbers):
    answer = set()
    visited = [False for _ in range(len(numbers))]
    
    def dfs(num_list):
        nonlocal answer
        
        if num_list:
            check_num = int("".join(num_list))
            if is_prime(check_num):
                answer.add(check_num)
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(num_list + [numbers[i]])
                visited[i] = False
    
    
    dfs([])

    return len(answer)