def solution(sequence):
    answer = 0
    
    arr1 = [num * ((-1) ** i) for i, num in enumerate(sequence)]
    arr2 = [num * ((-1) ** (i + 1)) for i, num in enumerate(sequence)]
    
    dp1 = [0 for _ in range(len(sequence))]
    dp2 = [0 for _ in range(len(sequence))]
    
    dp1[0] = arr1[0]
    dp2[0] = arr2[0]
    
    for i in range(1, len(sequence)):
        dp1[i] = max(arr1[i], dp1[i - 1] + arr1[i])
        dp2[i] = max(arr2[i], dp2[i - 1] + arr2[i])

    answer = max(max(dp1), max(dp2))
    return answer