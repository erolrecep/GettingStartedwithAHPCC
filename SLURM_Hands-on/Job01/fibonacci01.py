#!/usr/bin python3

def fibonacci(number):
    if number == 0:
        return 0
    elif number < 3:
        return number
    else:
        fib1 = 1
        fib2 = 1
        total = 0
        for x in range(3, number + 1):
            total = fib1 + fib2
            fib1, fib2 = fib2, total
        return total

def main():
    print(fibonacci(5))

if __name__ == '__main__':
    main()
