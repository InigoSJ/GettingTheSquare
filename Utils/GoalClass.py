import pygame
import random

cWidth = 600
cHeight = 600


class goal(object):
    def __init__(self, multi_player=False, position_list=[]):
        self.dim = 15
        self.points = 10
        self.count = 0
        self.multi = multi_player
        if self.multi:
            self.pos_list = position_list
            self.pos = self.pos_list[self.count]
        else:
            self.pos = [random.uniform(int(cWidth / 10), cWidth - int(cWidth / 10)),
                        random.uniform(int(cHeight / 10), cHeight - int(cHeight / 10))]

    def collision(self, player, surface):
        self.Rect = pygame.draw.rect(surface, (0, 0, 255), (self.pos[0], self.pos[1], self.dim, self.dim))

        if self.Rect.colliderect(player.Rect):
            self.count += 1
            if self.multi:
                self.pos = self.pos_list[self.count]
            else:
                self.pos = [random.uniform(30, cWidth - 30), random.uniform(30, cHeight - 30)]
            player.score += 10
