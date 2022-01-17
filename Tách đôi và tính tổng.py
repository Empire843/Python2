number = input()
while True:
    num1 = number[:len(number) // 2]
    num2 = number[len(number) // 2:]
    number = str(int(num1)+int(num2))
    print(number)
    if len(number) == 1:
        break

