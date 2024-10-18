first = input()
second = input()
third = input()

my_list = [first, second, third]
res = 0

for word in my_list:
    if word.isdigit():
        res = int(word) + 3 - my_list.index(word)
        break

if res % 3 == 0:
    if res % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if res % 5 == 0:
        print("Buzz")
    else:
        print(res)