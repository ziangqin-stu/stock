"""
General Method:
1. use RL method, use data fragment as state, stock operation as action, simulated stock trade market as environment.
2.
"""


import torch


class BaseRLAgent:
    def __init__(self):
        self.nn = None

    def train(self, x):
        pass

    def forward(self, x):
        pass


class DQNAgent(BaseRLAgent):
    def train(self, x):
        pass


class PPOAgent(BaseRLAgent):
    def train(self, x):
        pass


class SACAgent(BaseRLAgent):
    def train(self, x):
        pass
