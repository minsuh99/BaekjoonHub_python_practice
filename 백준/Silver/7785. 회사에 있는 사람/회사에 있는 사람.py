n = int(input())
people = set()
for _ in range(n):
    name, record = input().split()
    if record == "enter":
        people.add(name)
    elif record == "leave":
        people.remove(name)

for name in sorted(list(people), reverse=True):
    print(name)