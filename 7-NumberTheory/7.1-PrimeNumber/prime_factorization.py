import math

def prime_factorization(x):
    c = x

    # print the number of 2s that divides c
    while c % 2 == 0:
        print(2)
        c //= 2

    # check for odd factors from 3 upwards
    i = 3
    sqrt_of_c = math.sqrt(c)
    while i <= sqrt_of_c + 1:
        if c % i == 0:
            print(i)
            c //= i
            sqrt_of_c = math.sqrt(c) # only update if c changes
        else:
            i += 2

    # if c is still greater than 1, it must be prime
    if c > 1:
        print(c)

prime_factorization(214748364)
prime_factorization(2147483647)
