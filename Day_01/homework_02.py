import random
# random.seed(10)

#1~9를 범위로 하는 리스트 생성 함수.
def makeRandoms(count):
    ns = []
    for _ in range(count):
        ns.append(random.randrange(10))
    return ns

list1 = makeRandoms(10)
list2 = makeRandoms(10)

def sum10(num):
    for i in list1:
        for j in list2:
            if i + j == num:
                print(i, j, end=',')


print(list1)
print(list2)
sum10(10)