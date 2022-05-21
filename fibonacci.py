# Fibonacci sequence

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 2) + Fibonacci(n - 1)


if __name__ == '__main__':
    number = 10
    print("The Fibonacci Sequence is:")
    for number in range(0, number):
        print(Fibonacci(number))