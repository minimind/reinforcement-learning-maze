import sys
import actions


class QValueStore:
    def __init__(self):
        self._state_to_actions = {}

    def get_q_value(self, state, action):
        if state in self._state_to_actions:
            if action in self._state_to_actions[state]:
                return self._state_to_actions[state][action]
        return 0

    def get_best_action(self, state):
        best_action = actions.UNKNOWN_ACTION
        if state in self._state_to_actions:
            max_value = sys.float_info.min
            for action in self._state_to_actions[state]:
                if self._state_to_actions[state][action] > max_value:
                    max_value = self._state_to_actions[state][action]
                    best_action = action

        return best_action

    def store_value(self, state, action, value):
        if state not in self._state_to_actions:
            self._state_to_actions[state] = {}

        self._state_to_actions[state][action] = value
