for i in range(3, 0, -1):
    temp = input()
    if temp.isdigit():
        check_num = int(temp) + i

        if check_num % 3 == 0:
            if check_num % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        else:
            if check_num % 5 == 0:
                print("Buzz")
            else:
                print(check_num)
        
        break