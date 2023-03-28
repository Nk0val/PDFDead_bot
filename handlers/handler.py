# Base class of all handlers

import abc


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        self.bot = bot

    @abc.abstractmethod
    def handle(self):
        pass
