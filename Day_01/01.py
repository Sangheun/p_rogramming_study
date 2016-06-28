import random


random_num = random.randrange(1,20)
input_num = int(input("enter a number"))

def count_num(num1, num2):
    while num1 != num2:
        if num1 > num2:
            print("num1이 더 큽니다.")
        elif num1 < num2:
            print("num2가 더 큽니다.")
        else:
            print("똑같네요.")
            break


# input("Well, {}, I am thinking of a number between 1 and 20. Take a Guess.".format(input_name))

