import pygame

from Utils.OtherFunctions import *
from Utils.PlayerClass import *
from Utils.GoalClass import *

cWidth = 600
cHeight = 600

pygame.init()
win = pygame.display.set_mode((cWidth, cHeight))

on = True
p1 = player()
circle = goal()

while on:

    now = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                p1.is_training = False  # Press P to Predict
            if event.key == pygame.K_t:
                p1.is_training = True  # Press T to Train

    p1.movement(win, circle, now)
    circle.collision(p1, win)

    message_display(str(p1.score), 20, (100), (50), win)
    message_display(str(now / 1000), 20, (500), (50), win)

    pygame.display.update()
    win.fill((0, 0, 0))

pygame.quit()
