# Write a program find a factorial of a given number

def my_fact(n):
    if n <= 1:
        return 1
    else:
        return n * my_fact(n-1)
print(my_fact(-1))
