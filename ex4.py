#Write a program print the  Fibonacci series  till 100

n = 100

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

for i in range(n):
    print(fibonacci(i))

