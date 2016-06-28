import random

user_input_choice = input("식사? 뒷풀이?(식사/뒷풀이)")
if user_input_choice == "식사":
    food = []
    while True:
        rest_name = input("식당 이름을 입력해 주세요: ")
        food_name = input("음식 종류를 입력해 주세요: ")
        list_new = {rest_name: food_name}
        food.append(list_new)
        keep_going = input("계속 입력하시겠습니까?(y/n)")
        if keep_going == "y":
            user_input_choice =="식사"
        else:
            break

    try:
        user_input_rand = input("식당 랜덤뽑기를 하시겠습니까?(y/n)")
        while user_input_rand == "y":
            print(food)
            rand_food = random.choice(food)
            print("식당: {}".format(rand_food))
            food.remove(rand_food)
            user_input_rand = input("계속 진행하시겠습니까?(y/n)")
            if user_input_rand == "y":
                continue
            else:
                break
    except IndexError:
        print("더 이상 뽑을 식당이 없습니다!\n바이바이! 맛있게 드세요")


if user_input_choice == "뒷풀이":
    drink = []
    while True:
        pub_name = input("술집 이름을 입력해 주세요: ")
        drink_name = input("주종을 입력해 주세요: ")
        list_new = {pub_name: drink_name}
        drink.append(list_new)
        keep_going = input("계속 입력하시겠습니까?(y/n)")
        if keep_going == "y":
            user_input_choice =="식사"
        else:
            break
    try:

        user_input_rand = input("술집 랜덤뽑기를 하시겠습니까?(y/n)")
        while user_input_rand == "y":
            print(drink)
            rand_drink = random.choice(drink)
            print("술집: {}".format(rand_drink))
            drink.remove(rand_drink)
            user_input_rand = input("계속 진행하시겠습니까?(y/n)")
            if user_input_rand == "y":
                continue
            else:
                break
    except IndexError:
        print("더 이상 뽑을 술집이 없습니다!\n적당히 마셔요!바이바이!")
