import random

#랜덤 넘버 생성
random_num = random.randrange(1,21)
print(random_num)

#이름 입력
input_name = input("Hello! What is your name?")

print("Well, %s, I am thinking of a number between 1 and 20." % input_name)

#숫자 입력받기
input_num = input("Enter a number!!")

#입력값 숫자로 전환
input_num = int(input_num)

count_num = 1 #시작은 1이니까
while random_num != input_num: #random_num과 input_num이 다르면
    count_num = count_num + 1
    if input_num > random_num:
        print("Your guess is too high.")
        input_num = int(input("Enter a number!!"))
    elif input_num < random_num:
        print("Your guess is too low.")
        input_num = int(input("Enter a number!!"))

if random_num == input_num: #random_num과 input_num이 같으면
    print("Good job, %s! You guessed my number in %d guesses!" % (input_name, count_num))

print(input_num)