import pygame as pg
from random import randint
from math import sqrt

SCALE = 25


class Vector:
    pass
class Vector:
    def __init__(self, color, origin, dimensions):
        self.color = color
        self.origin = origin
        self.dimensions = dimensions
        self._calc_end()

    def _calc_end(self):
        ox, oy = self.origin
        dx, dy = self.dimensions
        self.end = ox + (dx * SCALE), oy - (dy * SCALE)
    
    def copy(self) -> Vector:
        return Vector(self.color, self.origin, self.dimensions)

    def draw(self, surface):
        pg.draw.line(surface, self.color, self.origin, self.end, 3)

    def center_on(self, other: Vector):
        self.origin = other.end
        self._calc_end()

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions
        self._calc_end()
    
    def set_origin(self, origin):
        self.origin = origin
        self._calc_end()

    def normalize(self):
        x, y = self.dimensions
        mag = sqrt(x**2 + y**2)
        self.set_dimensions((x / mag, y / mag))

    def proyect_on(self, other: Vector):
        sx, sy = self.dimensions
        ox, oy = other.dimensions
        dot = sx * ox + sy * oy
        try:
            temp_name = dot / (ox ** 2 + oy ** 2)
        except ZeroDivisionError:
            temp_name = 0
        self.dimensions = ox * temp_name, oy * temp_name
        self._calc_end()
    


class Plane:
    def __init__(self, center, size):
        self.rect = pg.Rect((0, 0), (size * SCALE, size * SCALE))
        self.rect.center = center

        self.randomize()
        self.vec_B.proyect_on(self.vec_A)

    def draw(self, surface):
        pg.draw.rect(surface, (20, 20, 20), self.rect)
        self.vec_A.draw(surface)
        self.vec_B.draw(surface)
        if self.result.dimensions != (0, 0):
            self.result.draw(surface)

    def randomize(self):
        self.vec_A = Vector(
            pg.Color('red'),
            self.rect.center,
            (
                randint(-5, 5),
                randint(-5, 5)
            )
        )
        self.vec_B = Vector(
            pg.Color('green'),
            self.rect.center,
            (
                randint(-5, 5),
                randint(-5, 5)
            )
        )
        self.result = Vector(pg.Color('blue'), self.rect.center, (0, 0))

    def normalize_a(self):
        self.vec_B.set_origin(self.rect.center)
        self.vec_A.normalize()
        self.result.set_dimensions((0, 0))
    
    def normalize_b(self):
        self.vec_B.set_origin(self.rect.center)
        self.vec_B.normalize()
        self.result.set_dimensions((0, 0))

    def add(self):
        self.vec_B.center_on(self.vec_A)
        vax, vay = self.vec_A.dimensions
        vbx, vby = self.vec_B.dimensions
        self.result.set_dimensions((vax + vbx, vay + vby))
    
    def sub(self):
        vax, vay = self.vec_A.dimensions
        vbx, vby = self.vec_B.dimensions
        self.vec_B.set_dimensions((-vbx, -vby))
        self.vec_B.center_on(self.vec_A)
        self.result.set_dimensions((vax - vbx, vay - vby))

    def proyect(self):
        self.vec_B.set_origin(self.vec_A.origin)
        self.vec_B.proyect_on(self.vec_A)
        self.result.set_dimensions((0, 0))


class App:
    running = True

    def __init__(self):
        pg.init()

        self.window = pg.display.set_mode((800, 600))
        self.plane = Plane(self.window.get_rect().center, 21)

    def __del__(self):
        pg.quit()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.running = False
                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:
                            self.running = False
                        case pg.K_1:
                            self.plane.randomize()
                        case pg.K_2:
                            self.plane.normalize_a()
                        case pg.K_3:
                            self.plane.normalize_b()
                        case pg.K_4:
                            self.plane.add()
                        case pg.K_5:
                            self.plane.sub()
                        case pg.K_6:
                            self.plane.proyect()

    def draw(self):
        self.plane.draw(self.window)
        pg.display.flip()


if __name__ == '__main__':
    App().run()