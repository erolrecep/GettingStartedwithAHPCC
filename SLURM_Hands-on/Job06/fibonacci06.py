#!/usr/bin python3


# import required libraries
import matplotlib.pyplot as plt


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
    result = fibonacci(100)
    # print(fibonacci(12))

    # Plot the fibonacci sequence
    plt.plot(result)
    plt.grid(True)
    plt.title("Fibonacci Sequence up to 100")
    plt.xlabel("Sequence")
    plt.ylabel("Fibonacci values")
    plt.savefig("../output/fibonacci_sequence100.png")
    plt.show()

    # Plot the ratio between two consecutive values of the sequence
    ratio = [result[idx] / result[idx+1]  for idx in range(len(result)-1)]
    plt.plot(ratio)
    plt.grid(True)
    plt.title("The Ratio between Fibonacci Values up to 100")
    plt.xlabel("Sequence")
    plt.ylabel("Fibonacci ratio")
    plt.savefig("../output/fibonacci_ratio100.png")
    plt.show()


if __name__ == '__main__':
    main()
