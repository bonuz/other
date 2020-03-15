def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


print("Insert a number for collatz sequience")
try:
    num = int(input())

    while num != 1:
        num = collatz(num)
        print(str(num))

except ValueError:
    print("Must be an integer value")

    


