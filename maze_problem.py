import random
import pygame
import actions


class MazeProblem:
    def __init__(self, starting_position=None):
        self._initialised_screen = False
        self._screen = None
        self._goal_x = 15
        self._goal_y = 15

        self._maze_definition = [
            # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
            [0,  0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 2
            [0,  0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 3
            [0,  0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 4
            [0,  0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0,  0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
            [0,  0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
            [0,  0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
            [0,  0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 17
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 18
            [0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # 19
        ]

        if starting_position:
            self._x = starting_position[0]
            self._y = starting_position[1]
        else:
            # We'll pick a random x and y until we hit a 0
            self._x = random.randint(0, 19)
            self._y = random.randint(0, 19)
            while self._maze_definition[self._y][self._x] != 0 or (self._x == self._goal_x and self._y == self._goal_y):
                self._x = random.randint(0, 19)
                self._y = random.randint(0, 19)

    def get_maze_definition(self):
        return self._maze_definition

    def get_possible_actions(self):
        # We return a list of possible actions here
        possible_actions = []
        if 0 < self._y <= 19 and self._maze_definition[self._y - 1][self._x] == 0:
            possible_actions.append(actions.NORTH)
        if 19 > self._y >= 0 and self._maze_definition[self._y + 1][self._x] == 0:
            possible_actions.append(actions.SOUTH)
        if 0 <= self._x < 19 and self._maze_definition[self._y][self._x + 1] == 0:
            possible_actions.append(actions.EAST)
        if 19 >= self._x > 0 and self._maze_definition[self._y][self._x - 1] == 0:
            possible_actions.append(actions.WEST)

        return possible_actions

    def get_state(self):
        return self._x, self._y

    def get_goal(self):
        return self._goal_x, self._goal_y

    def take_action(self, action):
        if action == actions.NORTH:
            if self._y <= 0:
                raise RuntimeError('Tried to move off edge')
            if self._maze_definition[self._y - 1][self._x] != 0:
                raise RuntimeError('Tried to move to non-zero spot')
            self._y -= 1
        elif action == actions.SOUTH:
            if self._y >= 19:
                raise RuntimeError('Tried to move off edge')
            if self._maze_definition[self._y + 1][self._x] != 0:
                raise RuntimeError('Tried to move to non-zero spot')
            self._y += 1
        elif action == actions.EAST:
            if self._x >= 19:
                raise RuntimeError('Tried to move off edge')
            if self._maze_definition[self._y][self._x + 1] != 0:
                raise RuntimeError('Tried to move to non-zero spot')
            self._x += 1
        elif action == actions.WEST:
            if self._x <= 0:
                raise RuntimeError('Tried to move off edge')
            if self._maze_definition[self._y][self._x - 1] != 0:
                raise RuntimeError('Tried to move to non-zero spot')
            self._x -= 1
        else:
            raise RuntimeError('Unknown action')

        if self._x == self._goal_x and self._y == self._goal_y:
            return 100, (self._x, self._y)

        return 0, (self._x, self._y)
