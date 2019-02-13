import numpy as np
from DeepLearning.Transformations import *


class NeuralNetwork(object):
    def __init__(self, inputs, hidden, output, lr=0.01, adaptive=False, decay=0.5):
        self.weights_ih = np.matrix(np.random.rand(hidden, inputs))
        self.weights_ho = np.matrix(np.random.rand(output, hidden))
        self.bias_ih = np.random.rand(hidden, 1)
        self.bias_ho = np.random.rand(output, 1)
        self.lr = lr
        self.decay = decay
        self.adaptive = adaptive

    def train(self, value_in, guess, epoch=0, activation_function=sigmoid, adaptive_function=timebased,
              input_space=[0, 1], output_space=[0, 1]):

        input_v = np.matrix(value_in).transpose()

        if self.adaptive:
            self.lr = adaptive_function(epoch, self.lr, self.decay)
            print(self.lr)

        # from input to hidden
        mat_ih = self.weights_ih * input_v
        mat_h = mat_ih + self.bias_ih
        mat_h_sigmoid = activation_function(mat_h)

        # from hidden to output
        mat_ho = self.weights_ho * mat_h_sigmoid
        mat_o = (mat_ho + self.bias_ho)
        output_v = activation_function(mat_o)

        # linear transformation
        [m, b] = linear_trans(input_space, output_space)
        output_linear = m * output_v + b
        guess_linear = (np.matrix(guess) - b) / m

        # calculate error
        guess_m = np.matrix(guess_linear).transpose()
        error = guess_m - output_v
        error_hidden = (self.weights_ho.transpose() * error)

        # backpropagation output to hidden
        d_sig_o = activation_function(output_v, derivate=True)
        gradient_ho = np.multiply(self.lr * error, d_sig_o)
        delta_w_ho = gradient_ho * mat_h_sigmoid.transpose()
        self.weights_ho += delta_w_ho

        delta_b_ho = np.multiply(self.lr * error, gradient_ho)
        self.bias_ho += delta_b_ho

        # backpropagation hidden to input
        d_sig_h = activation_function(mat_h_sigmoid, derivate=True)
        hidden_gradient = np.multiply(self.lr * error_hidden, d_sig_h)
        delta_w_ih = hidden_gradient * input_v.transpose()
        self.weights_ih += delta_w_ih
        delta_b_ih = np.multiply(self.lr * error_hidden, hidden_gradient)
        self.bias_ih += delta_b_ih

        return output_linear

    def predict(self, value_in, activation_function=sigmoid, input_space=[0, 1], output_space=[0, 1]):
        input_v = np.matrix(value_in).transpose()

        # from input to hidden
        mat_ih = self.weights_ih * input_v
        mat_h = mat_ih + self.bias_ih
        mat_h_sigmoid = activation_function(mat_h)

        # from hidden to output
        mat_ho = self.weights_ho * mat_h_sigmoid
        mat_o = (mat_ho + self.bias_ho)
        output_v = activation_function(mat_o)

        # linear transformation
        [m, b] = linear_trans(input_space, output_space)
        output_linear = m * output_v + b

        return output_linear