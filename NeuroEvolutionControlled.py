import pygame
import random
import math

from Utils.OtherFunctions import *
from Utils.PlayerClass import *
from Utils.GoalClass import *

cWidth = 600
cHeight = 600
TPlayers = 100
TPlayers += TPlayers % 2  # guarantee there's an odd number of players

circlepos = []
MAX_GEN = 50
MAX_TIME = 10
MUTATION = 0.1

gen = 1
p1 = []

for i in range(TPlayers):
    p1.append(player())

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
            message_display(str(gen), 100, (cWidth / 2), (cHeight / 2), win)
            pygame.display.update()
            fitness_list = []
            for gamer in p1:
                fitness = gamer.score * 100
                fitness_list.append([fitness, gamer])
                gamer.score = 0
            fitness_list = sorted(fitness_list, key=lambda x: x[0], reverse=True)
            sorted_players = [p[1] for p in fitness_list]
            half_players = int(TPlayers / 2)
            next_gen = []
            next_gen.append(sorted_players[0])  # best
            next_gen += random.sample(sorted_players[1:half_players], math.floor(TPlayers * 0.4 - 1))  # good
            next_gen += random.sample(sorted_players[half_players + 1:], half_players - len(next_gen))  # lucky
            p1 = next_gen
            mutated = []
            for p in p1:
                p.score = 0
                p.pos = [cWidth / 2, cHeight / 2]
                mutated += [mutate(p, MUTATION)]
            p1 += mutated
            gen += 1
            on = False

pygame.quit()
