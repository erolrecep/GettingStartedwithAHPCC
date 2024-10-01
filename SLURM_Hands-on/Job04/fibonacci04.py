#!/usr/bin python3

def fibonacci(number):
    if number == 0:
        return [0]
    elif number == 1:
        return [0, 1]
    elif number == 2:
        return [0, 1, 1]
    else:
        fib1 = 1
        fib2 = 1
        total = 0
        sequence = [0, 1, 1]
        for x in range(3, number + 1):
            total = fib1 + fib2
            sequence.append(total)
            fib1, fib2 = fib2, total
        return sequence

def main():
    with open("../output/fibonacci_sequence_100.txt", "w") as f:
        for x in fibonacci(100):
            f.write(str(x) + "\n")

if __name__ == '__main__':
    main()
