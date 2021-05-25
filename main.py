import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))  # Set to (0, 0) for fullscreen
running = True
pendulums = []  # This list stores references to every Pendulum object that was created
number_of_pendulums = 5  # <------- The number of pendulums
speed_multiplier = 0.5  # <------- Change value to control the speed (0.5 good)


class Pendulum:
    def __init__(self, start=None, parent=None, length=None, angle=0, angular_velocity=0,
                 mass=1):  # mass parameter does absolutely nothing
        self.start = start
        self.parent = parent
        self.angle = angle
        self.angular_velocity = angular_velocity
        self.mass = mass
        self.length = length
        pendulums.append(self)


def draw_pendulums():  # This function draws every Pendulum object that was ever created
    for pendulum in pendulums:
        pendulum.angle += pendulum.angular_velocity
        if pendulum.parent != None:
            start = pendulum.parent.end
        else:
            start = pendulum.start
        pendulum.end = (start[0] + pendulum.length * math.sin(math.radians(pendulum.angle)),
                        start[1] + pendulum.length * math.cos(
                            math.radians(pendulum.angle)))  # Here we rotate the line by an angle
        pygame.draw.circle(screen, color=(5, 240, 9), center=pendulum.end, radius=4)
        pygame.draw.line(screen, (255, 255, 255), start, pendulum.end, width=3)


Pendulum(start=(screen.get_width() / 2, screen.get_height() / 2), length=random.randint(30, 100),
         angular_velocity=random.choice((0.1, 0.2, 0.3, 0.4, 0.5)))
for i in range(number_of_pendulums - 1):
    Pendulum(parent=pendulums[-1], length=random.randint(30, 70),
             angular_velocity=random.choice((0.1, 0.2, 0.3, 0.4, 0.5)) * random.choice((-1, 1)) * speed_multiplier)
tracer = pygame.Surface((screen.get_width(), screen.get_height()))  # This is the surface for drawing the tracer
n = 0
r = g = b = 112
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
    if n == 1:
        r += random.choice((-10, 0, 10))  # Here we change the color by a bit
        g += random.choice((-10, 0, 10))
        b += random.choice((-10, 0, 10))
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255
        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0
        pygame.draw.circle(tracer, color=(r, g, b), center=pendulums[-1].end,
                           radius=2)  # We draw a small circle at the end of the last item on the list on every iteration
    n = 1
    screen.blit(tracer, (0, 0))
    draw_pendulums()
    pygame.display.update()
