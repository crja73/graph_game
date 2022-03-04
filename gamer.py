from random import randint
from graph import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
fps = 20
update_period = round(100 / fps)


class GameObject:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

        if not hasattr(self, "update"):
            raise NotImplementedError("Нельзя создать такой объект")

        @property
        def x(self): return self._x

        @property
        def y(self): return self._x

        @property
        def width(self): return self._width

        @property
        def height(self): return self._height


class BlackHole(GameObject):
    def __init__(self, x_center, y_center, radius):
        GameObject.__init__(self, x_center, y_center, 1.5 * radius, 1.5 * radius)
        brushColor("black")
        self._image = circle(x_center, y_center, radius)

    def update(self):
        pass


class Pulsar(BlackHole):
    def __init__(self, x_center, y_center, radius):
        BlackHole.__init__(self, x_center, y_center, 1.5 * radius)
        changeFillColor(self._image, 'brown')

    def update(self):
        self.__changeRadius(randint(5, 20))

    def __changeRadius(self, new_radius):
        self._width = 2 * new_radius
        self._height = 2 * new_radius

        changeCoords(self._image,
                     [(self._x - new_radius, self._y - new_radius),
                      (self._x + new_radius, self._y + new_radius)])


windowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
canvasSize(SCREEN_WIDTH, SCREEN_HEIGHT)

all_objects = []

NUMBER_OF_BLACKHOLES = 10
for i in range(NUMBER_OF_BLACKHOLES):
    all_objects.append(BlackHole(randint(0, SCREEN_WIDTH),
                                 randint(0, SCREEN_HEIGHT),
                                 randint(10, 20)))
NUMBER_OF_PULSARS = 6000
pulsars = []
for i in range(NUMBER_OF_PULSARS):
    all_objects.append(Pulsar(randint(0, SCREEN_WIDTH),
                              randint(0, SCREEN_HEIGHT),
                              randint(10, 20)))


def update():
    for obj in all_objects:
        obj.update()


onTimer(update, update_period)

run()
