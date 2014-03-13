from neuralnetwork import NeuralNetwork
from seekers.base import Seeker


class NeuralNet(Seeker):

    def __init__(self, model):
        super(NeuralNet, self).__init__()
        self._model = model
        self.net = NeuralNetwork()

    def __str__(self):
        return "Neural Network"

    def next(self):
        'seeks the next coordinate in the space and returns it'
        return self._model.space.randomize()

    @property
    def current(self):
        'return current coordinates'
        return self._model.space.current()

    @current.setter
    def current(self, value):
        'recieve new coordinates and reset to them'
        self._model._space._current = value
        self.reset()

