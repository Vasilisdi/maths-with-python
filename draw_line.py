from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def printthem(self):
        print(F"  ({self.x} , {self.y}) ")


class Line:
    def __init__(self, point_A=None, point_B=None): #cate the =None term indicates that if is none / leave vacant
        if point_A is None:
            self.point_A = Point(0, 0)
        else:
            self.point_A = point_A
        if point_B is None:
            self.point_B = Point(0, 0)
        else:
            self.point_B = point_B

    def length(self):
        return sqrt((self.point_A.x - self.point_B.x)**2 + (self.point_A.y - self.point_B.y)**2)

    def printthemm(self):
        self.point_A.printthem()
        self.point_B.printthem()


pa = Point(1, 1)
pb = Point(2, 2)
line = Line(pa, pb)
line.printthemm()
print(line.length())

line = Line()
line.printthemm()
print(int(line.length()))