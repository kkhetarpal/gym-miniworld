import numpy as np
import math
from ..miniworld import MiniWorldEnv, Room
from ..entity import Box

class OneRoom(MiniWorldEnv):
    """
    Environment in which the goal is to go to a red box
    placed randomly in one big room.
    """

    def __init__(self, size=10,change_goal=None, **kwargs):
        assert size >= 2
        self.size = size
        self.change_goal = change_goal

        super().__init__(
            max_episode_steps=180,
            **kwargs
        )

    def _gen_world(self):
        room = self.add_rect_room(
            min_x=0,
            max_x=self.size,
            min_z=0,
            max_z=self.size
        )

        if not self.change_goal:
            self.box = self.place_entity(Box(color='red'))
        else:
            self.box = self.place_entity(Box(color='blue'))
        self.place_agent()

    def step(self, action):
        obs, reward, done, info = super().step(action)

        if self.near(self.box):
            reward += self._reward()
            done = True

        return obs, reward, done, info
