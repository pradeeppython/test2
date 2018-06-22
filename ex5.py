# Write a program find a given number is prime or not


def prime_num(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
            else:
                return True             
print(prime_num(78))
