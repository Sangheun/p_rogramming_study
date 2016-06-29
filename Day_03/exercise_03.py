# # # def sum_many(*args):
# # #     sum = 0
# # #     for i in args:
# # #         sum = sum + i
# # #     return sum
# # #
# # # result = sum_many(1,2,3)
# # # print(result)
# # #
# # # result = sum_many(1,2,3,4,5,6,7)
# # # print(result)
# # #
# # # def sum_mul(choice, *args):
# # #     if choice == "sum":
# # #         result=0
# # #         for i in args:
# # #             result = result + i
# # #     elif choice == "mul":
# # #         result = 1
# # #         for i in args:
# # #             result = result * i
# # #     return result
# # #
# # # result = sum_mul("sum", 1,2,3,4,5)
# # # print(result)
# # #
# # # result = sum_mul("mul", 1,2,3,4,5)
# # # print(result)
# # #
# # #
# # # def sum_and_mul(a,b):
# # #     return a + b, a*b
# # #
# # # sum, mul = sum_and_mul(3,4)
# # # print(sum)
# # # print(mul)
# #
# # a = list(range(3,6))
# # print(a)
# #
# # args = [2,6]
# # a = list(range(*args))
# # print(a)
#
# import random
# # random.seed(10)
# def makeRandoms(count):
#     ns = []
#     for _ in range(count):
#         ns.append(random.randrange(10))
#     return ns
#
# a = makeRandoms(10)
# print(a)
#
# def max_min(*args):
#     return max(*args), min(*args)
#
# b = max_min(a)
# print(b)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class Point:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        result = self.x + self.dx, self.y + self.dy
        return result

a = Point()
a.setx(3)
a.sety(4)
a.get()
a.move(3,4)
