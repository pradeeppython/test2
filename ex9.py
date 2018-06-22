#Write a program find a given number is Armstrong or not?

def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum+digit**3
        temp = temp // 10
    if num == sum:
        print(num," is an armstrong number")
    else:
        print(num,"is not an armstrong number")

num = int(input("enter a number:"))
a = is_armstrong(num)
