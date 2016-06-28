import random

user_input_choice = input("식사 ? 뒷풀이?")
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
    print(food)
    user_input_rand = input("식당 랜덤뽑기를 하시겠습니까?(y/n)")

    try:
        while user_input_rand == "y":
            rand_food = random.choice(food)
            print(rand_food)
            food.remove(rand_food)
            user_input_rand = input("랜덤뽑기를 하시겠습니까?")
    except IndexError:
        print('더 이상 뽑을 식당이 없어요!')

elif user_input_choice == "뒷풀이":
    drink = []
    while True:
        pub_name = input("술집 이름을 입력해"
                          " 주세요: ")
        drink_name = input("주종을 입력해 주세요: ")
        if pub_name != "End":
            list_new = {pub_name: drink_name}
            drink.append(list_new)
        else:
            break
    print(drink)
    user_input_rand = input("랜덤뽑기를 하시겠습니까?")

    try:
        while user_input_rand == "y":
            rand_drink = random.choice(drink)
            print(rand_drink)
            drink.remove(rand_drink)
            user_input_rand = input("랜덤뽑기를 하시겠습니까?")
    except IndexError:
        print("더 이상 선택할 술집이 없어요!")

import random

user_input_choice = input("식사 ? 뒷풀이?")
if user_input_choice == "식사":
    food = []
    while True:
        rest_name = input("식당 이름을 입력해 주세요: ")
        food_name = input("음식 종류를 입력해 주세요: ")
        if food_name != "End":
            list_new = {rest_name: food_name}
            food.append(list_new)
        else:
            break
    user_input_rand = input("랜덤뽑기를 하시겠습니까?")

    try:
        while user_input_rand == "y":
            print(food)
            if food != []:
                rand_food = random.choice(food)
                print(rand_food)
                food.remove(rand_food)
                # user_input_rand = input("랜덤뽑기를 하시겠습니까?")
            else:
                print("랜덤 뽑기를 종료합니다.")
                break
    except IndexError:
        print('더 이상 뽑을 식당이 없어요!')

elif user_input_choice == "뒷풀이":
    drink = []
    while True:
        pub_name = input("술집 이름을 입력해"
                          " 주세요: ")
        drink_name = input("주종을 입력해 주세요: ")
        if pub_name != "End":
            list_new = {pub_name: drink_name}
            drink.append(list_new)
        else:
            break
    print(drink)
    user_input_rand = input("랜덤뽑기를 하시겠습니까?")

    try:
        while user_input_rand == "y":
            rand_drink = random.choice(drink)
            print(rand_drink)
            drink.remove(rand_drink)
            user_input_rand = input("랜덤뽑기를 하시겠습니까?")
    except IndexError:
        print("더 이상 선택할 술집이 없어요!")

