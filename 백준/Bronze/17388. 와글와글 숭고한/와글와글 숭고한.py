s, k, h = map(int, input().split())

if s+k+h >= 100:
    print("OK")
else:
    minimum = min(min(s, k),h)
    if minimum == s:
        print("Soongsil")
    elif minimum == k:
        print("Korea")
    elif minimum == h:
        print("Hanyang")