def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_array = merge_sort(arr[:mid])
    high_array = merge_sort(arr[mid:])
    global res
    
    merged_arr = []
    
    low_idx = high_idx = 0
    
    while low_idx < len(low_array) and high_idx < len(high_array):
        if low_array[low_idx] <= high_array[high_idx]:
            merged_arr.append(low_array[low_idx])
            low_idx += 1
        else:
            merged_arr.append(high_array[high_idx])
            high_idx += 1
            res += len(low_array) - low_idx
    
    if low_array[low_idx:]:
        merged_arr += low_array[low_idx:]
    else:
        merged_arr += high_array[high_idx:]

    return merged_arr

N = int(input())
arr = list(map(int, input().split()))
res = 0
merge_sort(arr)
print(res)