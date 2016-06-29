# 1
def average(a,b):
    return (a + b)/2

# 2

def max_min(*args):
    return max(*args), min(*args)

# 3
def triangle_area(width, height):
    return width * height / 2
# 4
def range_sum(begin, end):
    a = 0
    for i in range(begin, end + 1):
        a = i + a
    return a

# 5
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

# 6
a = Point()
a.setx(3)
a.sety(4)
a.get()
a.move(3,4)