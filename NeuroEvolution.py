import pygame
import random

from Utils.OtherFunctions import *
from Utils.PlayerClass import *
from Utils.GoalClass import *

cWidth = 600
cHeight = 600
TPlayers = 20

circlepos = []
MAX_GEN = 50
MAX_TIME = 10
MUTATION = 0.1

gen = 1
p1 = []

for i in range(TPlayers):
    p1.append(player(lr=0.01))

while gen <= MAX_GEN:
    for i in range(20 * MAX_TIME):
        circlepos += [[random.uniform(0, cWidth), random.uniform(0, cHeight - 10)]]
    pygame.init()
    win = pygame.display.set_mode((cWidth, cHeight))

    on = True
    circle = []
    maxscore = 0
    current = pygame.time.get_ticks()
    index = 0

    for i in range(TPlayers):
        circle.append(goal(multi_player=True, position_list=circlepos))

    while on:
        message_display('Generation {}'.format(gen), 20, 70, 35, win)
        now = pygame.time.get_ticks()
        clock = (now - current) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
                gen = MAX_GEN + 1
        if clock <= MAX_TIME:
            for i in range(TPlayers):
                p1[i].movement(win, circle[i], clock)
                circle[i].collision(p1[i], win)
            for play in p1:
                if play.score > maxscore:
                    maxscore = play.score
                    index = p1.index(play)
                    layers = play.hidden_layers

            message_display(str(clock), 30, (cWidth / 2), (cHeight / 2), win)

            pygame.display.update()
            win.fill((0, 0, 0))

        elif clock <= MAX_TIME + 0.5:
            win.fill((0, 0, 0))

            pygame.display.update()
        else:

            players_by_fitness = []
            next_gen = []
            sum_score = 0
            for gamer in p1:
                sum_score += gamer.score
                for i in range(1 + gamer.score // (10 * gen)):
                    players_by_fitness.append(gamer)
            chosen = random.sample(players_by_fitness, int(TPlayers))

            for gamer in chosen:
                gamer.score = 0
                gamer.pos = [cWidth / 2, cHeight / 2]
                next_gen.append(gamer)
                mutated = mutate(gamer, MUTATION)
                next_gen.append(mutated)

            p1 = next_gen
            gen += 1
            on = False

pygame.quit()
