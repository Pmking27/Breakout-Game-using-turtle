from math import sin, cos
import turtle

counter = 0


def rotate(x, y, r):
    s, c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c


class Cube:
    EDGES = (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5,
                                                     6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)
    VERTICES = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
                (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]

    def __init__(self, xpos, ypos, axes, color, ball):
        self.xpos = xpos
        self.ypos = ypos
        self.counter = counter
        self.axes = axes
        self.c = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.c)
        self.ball = ball
        self.fall = False

    def draw(self):

        for edge in self.EDGES:
            points = []

            for vertex in edge:
                x, y, z = self.VERTICES[vertex]

                if self.axes == '3' and self.fall == True:
                    # Only this one to rotate around y
                    x, z = rotate(x, z, self.counter)
                    y, z = rotate(y, z, self.counter)  # Only this for x
                    x, y = rotate(x, y, self.counter)  # This for z

                elif self.axes == 'x':
                    y, z = rotate(y, z, self.counter)  # Only this for x
                elif self.axes == 'y':
                    x, z = rotate(x, z, self.counter)
                elif self.axes == 'z':
                    x, y = rotate(x, y, self.counter)

                # Perspective formula
                z += 5
                if z != 0:
                    f = 100/(z)

                sx, sy = x*f, y*f
                points.append(sx)
                points.append(sy)

            self.t.up()
            self.t.goto(points[0]+self.xpos, points[1]+self.ypos)
            self.t.down()
            self.t.goto(points[2]+self.xpos, points[3]+self.ypos)
            self.t.up()
