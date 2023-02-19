import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Creates a window
pygame.display.set_caption("Planet simulation")

WHITE = (255,255,255)

class Planet:
    AU = 149.6e6 * 1000 #distance earth to sun *1000 cuz km in m
    G = 6.67428e-11
    SCALE = 250 /  AU # 1AU = 100 px
    TIMESTEP = 3600*24 #day

    def __innit__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)#FPS cap
        #WIN.fill(WHITE)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main()