# Prime numbers

def isPrimeNumber(n):
    flag = False
    if n > 1:
        for i in range(2, n):
            if(n % i) == 0:
                flag = True
                break
    return flag


if __name__ == '__main__':

    result = isPrimeNumber(19)

    if result:
        print('Not a prime number')
    else:
        print('It is a prime number')