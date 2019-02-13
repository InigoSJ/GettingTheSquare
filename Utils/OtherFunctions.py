import pygame
import numpy as np


def sign(x):
    if x < 0:
        return -1
    else:
        return 1


def right_move(obj1, obj2):
    x_dif = obj2.pos[0] - obj1.pos[0]
    y_dif = obj2.pos[1] - obj1.pos[1]  # canvas is inverted
    if abs(x_dif) > abs(y_dif):
        x_sign = sign(x_dif)
        move = [x_sign, x_sign * y_dif / x_dif]
    else:
        y_sign = sign(y_dif)
        move = [y_sign * x_dif / y_dif, y_sign]
    return move


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 255, 0))
    return textSurface, textSurface.get_rect()


def message_display(text, size, posx, posy, window):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (posx, posy)
    window.blit(TextSurf, TextRect)


def mutate(player_obj, mutation_rate):
    new_p = player_obj
    new_p.brain.weights_ho += np.random.uniform(-mutation_rate, mutation_rate, new_p.brain.weights_ho.shape)
    new_p.brain.weights_ih += np.random.uniform(-mutation_rate, mutation_rate, new_p.brain.weights_ih.shape)
    new_p.brain.bias_ho += np.random.uniform(-mutation_rate, mutation_rate, new_p.brain.bias_ho.shape)
    new_p.brain.bias_ih += np.random.uniform(-mutation_rate, mutation_rate, new_p.brain.bias_ih.shape)
    return new_p
