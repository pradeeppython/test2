# Write a program find given number is perfect or not

def perfect_number(n):
    total = 0
    for ele in range(1, n):
        if n % ele == 0:
            total = total + ele
    return total == n

n = int(input("enter a number: "))
print(perfect_number(n))
