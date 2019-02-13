import numpy as np


def sigmoid(x, derivate=False):
    if derivate:
        return np.multiply(x, ((1 - x)))
    else:
        return 1 / (1 + np.exp(-x))


def tanh(x, derivate=False):
    if derivate:
        sig = sigmoid(2 * x)
        return 8 * sigmoid(2 * sig, True)
    return 2 * sigmoid(2 * x) + 1


def linear_trans(space1, space2):
    m = (space2[0] - space2[1]) / (space1[0] - space1[1])
    b = space2[0] - space1[0] * m
    return [m, b]


def timebased(epoch, lr, decay):
    lr *= 1 / (1 + decay * epoch)
    return lr
