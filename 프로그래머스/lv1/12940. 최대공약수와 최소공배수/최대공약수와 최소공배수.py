def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solution(n, m):
    G = gcd(n, m) if n > m else gcd(m, n)
    answer = [G, n * m // G]
    return answer