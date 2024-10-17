def happiness(s, m, l):
    if 1*s+2*m+3*l >= 10:
        return "happy"
    elif 1*s+2*m+3*l < 10:
        return "sad"
    
s = int(input())
m = int(input())
l = int(input())

print(happiness(s, m, l))