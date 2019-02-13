import pygame

from DeepLearning.NeuralNetwork import *
from Utils.OtherFunctions import *

cWidth = 600
cHeight = 600


class player(object):
    def __init__(self, hidden=10, adaptive=False, decay=0.5, lr=0.01):
        self.dim = 22
        self.pos = [cWidth / 2, cHeight / 2]
        self.score = 0
        self.speed = 1
        self.hidden_layers = hidden
        self.brain = NeuralNetwork(4, self.hidden_layers, 2, lr, adaptive, decay)
        self.color = (255, 0, 0)
        self.is_training = True

    def movement(self, surface, goal_o, time):
        self.Rect = pygame.draw.rect(surface, self.color, (self.pos[0], self.pos[1], self.dim, self.dim))

        r_move = right_move(self, goal_o)

        if self.is_training:
            guess = self.brain.train([self.pos[0], self.pos[1], goal_o.pos[0], goal_o.pos[1]], r_move,
                                     output_space=[-1, 1])
        else:
            guess = self.brain.predict([self.pos[0], self.pos[1], goal_o.pos[0], goal_o.pos[1]], output_space=[-1, 1])
            message_display('PREDICT', 20, (300), (300), surface)

        self.pos[0] += guess[0, 0] * self.speed
        self.pos[1] += guess[1, 0] * self.speed

        if self.pos[0] > cWidth - self.dim:
            self.pos[0] = cWidth - self.dim
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[1] <= 0:
            self.pos[1] = 0
        if self.pos[1] >= cHeight - self.dim:
            self.pos[1] = cHeight - self.dim