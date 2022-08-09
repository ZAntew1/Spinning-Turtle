import time
import pygame

pygame.init()

width = 1920
length = 1080

window = pygame.display.set_mode((width, length))
pygame.display.set_caption("Race")

UP = pygame.image.load("UP.png")
DOWN = pygame.image.load("DOWN.png")

LEFT = pygame.image.load("LEFT.png")
RIGHT = pygame.image.load("RIGHT.png")

LEFTDOWN = pygame.image.load("LEFTDOWN.png")
LEFTUP = pygame.image.load("LEFTUP.png")

RIGHTDOWN = pygame.image.load("RIGHTDOWN.png")
RIGHTUP = pygame.image.load("RIGHTUP.png")

wait = 0.1

place = (940, 520)
                            



Run = True

while Run == True:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
    
    window.fill((1, 145, 142))
    char1 = window.blit(UP, (place))
    pygame.display.update()
    time.sleep(wait)
    window.fill((1, 145, 142))
    char2 = window.blit(RIGHTUP, (place))
    pygame.display.update()
    time.sleep(wait)
    window.fill((1, 145, 142))
    char3 = window.blit(RIGHT, (place))
    pygame.display.update()
    time.sleep(wait)
    window.fill((1, 145, 142))
    char4 = window.blit(RIGHTDOWN, (place))
    pygame.display.update()
    time.sleep(wait)
    window.fill((1, 145, 142))
    char5 = window.blit(DOWN, (place))
    pygame.display.update()
    time.sleep(wait)
    window.fill((1, 145, 142))
    char6 = window.blit(LEFTDOWN, (place))
    pygame.display.update()
    time.sleep(wait)
    window.fill((1, 145, 142))
    char7 = window.blit(LEFT, (place))
    pygame.display.update()
    time.sleep(wait)
    window.fill((1, 145, 142))
    char8 = window.blit(LEFTUP, (place))
    pygame.display.update()
    time.sleep(wait)

