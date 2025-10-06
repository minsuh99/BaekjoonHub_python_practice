from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        if city.lower() in cache:
            answer += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:
            answer += 5
            if cache and len(cache) == cacheSize:
                cache.popleft()
            cache.append(city.lower())

    return answer