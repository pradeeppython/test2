#Write a program find the given number is perfect or not

def perfect_number(num):
    total = 0
    for i in range(1,num):
        if num % i == 0:
            total += i
    return total == num

print(perfect_number(28))
