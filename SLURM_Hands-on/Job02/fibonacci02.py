#!/usr/bin python3

def fibonacci(number):
    # if number == 0:
    #     print("0")
    #     return 0
    # elif number == 1:
    #     print("0 1")
    #     return number
    # elif number == 2:
    #     print("0 1 1")
    #     return number
    if number < 3:
        print(" ".join([str(x) for x in range(0, number+1)]))
    else:
        fib1 = 1
        fib2 = 1
        total = 0
        print("0 1 1", end=" ")
        for x in range(3, number + 1):
            total = fib1 + fib2
            print(total, end=" ")
            fib1, fib2 = fib2, total
        print()

def main():
    fibonacci(3)

if __name__ == '__main__':
    main()
