# # 2
# def hide_numbers(s):
#     make_list = list(s)
#     for i in range(len(make_list)-4):
#         make_list[i] = "*"
#     make_str = "".join(make_list)
#
#     return make_str
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + hide_numbers('01033334444'));
#
#
# import re
#
# def hide_numbers(s):
#     p = re.compile(r'\d(?=\d{4})')
#     return p.sub("*", s, count = 0)
#
# # 평균구하기
# def average(list):
#     a = 0
#     for i in list:
#         a = i + a
#     div = a / len(list)
#     return div
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# list = [5,3,4]
# print("평균값 : {}".format(average(list)));

# def range_sum(begin, end):
#     make_list = list(range(begin,end+1))
#     return sum(make_list)

# # 짝수와 홀수
# def evenOrOdd(num):
#     if num%2 == 0:
#         s = "Even"
#     else:
#         s = "Odd"
#     return s
#
# def rm_small(mylist):
#     mylist.remove(min(mylist))
#     return mylist
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# my_list = [4, 3, 2, 1]
# print("결과 {} ".format(rm_small(my_list)))
#
# areas = [i*i for i in range(1,11) if i&2 == 0]
# a = [(x,y) for x in range(15) for y in range(15)]
# print(a)
# print(areas)
#
# def sum_digit(number):
#     str_number = str(number)
#     make_list = list(str_number)
#     return sum(make_list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : {}".format(sum_digit(123)));


