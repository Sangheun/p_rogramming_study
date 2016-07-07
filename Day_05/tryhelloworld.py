# # #
# # #
# # # selected = None
# # # while selected not in ['가위', '바위', '보']:
# # #     selected = input('가위, 바위, 보 중에 선택하세요.')
# # #
# # # print('선택된 값은 :', selected)
# # #
# #
# # patterns = ['가위', '보', '보']
# # for pattern in patterns:
# #     print(pattern)
# #
# # for i in range(len(patterns)):
# #     print(patterns[i])
# #
# # length = len(patterns)
# # i=0
# # while i < length:
# #     print(patterns[i])
# #     i = i + 1


# list = [1,2,3,5,7,2,5,237,55]
# # for val in list:
# #     if val % 3 == 0:
# #         print(val)
# #         break
# #break가 포함된 상위 블럭의 반복문이 종료됨.

# # for i in range(10):
# #     if i%2 != 0:
# #         print(i)
# #         print(i)
# #         print(i)
# #         print(i)
# #

# school = {'1반':[172,185,198,177,165,199], '2반':[166,177,167,180,191]}
# try:
#     for class_number, students in school.items():
#         # for student in students:
#         #     if student>190:
#         #         print(class_number,'190을 넘는 학생이 있습니다.')
#         #         break
#         for student in students:
#             if student > 190:
#                 print(class_number, '반에 190을 넘는 학생이 있습니다.')
#                 raise StopIteration
# except StopIteration:
#     print('정상종료')


# class Car():
#     '''자동차'''
#     def run(self):
#         print("{}가 달립니다.".format(self.name))



# taxi = Car()
# taxi.name = "택시"
# # taxi.run()

# class Human():

#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight

#     def __str__(self):
#         return "{} (몸무게 {}kg)".format(self.name, self.weight)

#     def eat(self):
#         self.weight += 0.1
#         print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))

#     def walk(self):
#         self.weight -= 0.1
#         print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

# # 아래에서 person을 이름과 몸무게를 가지는 Human클래스의 인스턴스로 만들어보세요.
# person = Human("사람", 50.5)
# person.eat()
# person.eat()
# person.walk()

# class Car():

#     def run(self):
#         print("차가 달립니다.")

# # 아래에서 Car를 상속받는 Truck이라는 클래스를 만들고, load라는 메소드를 만들어 보세요.
# # load메소드에서는 "짐을 실었습니다."라고 출력하면 됩니다.

# class Truck(Car):
#     def load(self):
#         print("짐을 실었습니다.")


class Car():

    def run(self):
        print("차가 달립니다.")


class Truck(Car):

    def load(self):
        print("짐을 실었습니다.")
    # 이 아래에서 run 메소드를 오버라이드 하세요.
    def run(self):
        print("트럭이 달립니다.")

truck = Truck()
truck.run()
