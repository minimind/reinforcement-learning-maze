import random
import time
import actions
from maze_problem import MazeProblem
from q_value_store import QValueStore
from draw_maze import draw_maze

MAX_NO_OF_TRIALS = 10000
MAX_TRIAL_LENGTH = 1000
DISPLAY_EVERY = 1
RHO = 0.05  # Chance a random action is taken
ALPHA = 0.1  # Learning rate
GAMMA = 0.3  # Discount rate

store = QValueStore()


def q_learning_step(maze_problem, alpha, gamma, rho):
    pass


def main():
    q_value_store = QValueStore()
    no_of_trials = 0
    running = True
    while running and no_of_trials < MAX_NO_OF_TRIALS:
        print(f'trial {no_of_trials}')
        maze_problem = MazeProblem()

        counter = 0
        while running and counter < MAX_TRIAL_LENGTH:
            if (no_of_trials % DISPLAY_EVERY) == 0:
                running = draw_maze(maze_problem)

            state = maze_problem.get_state()
            best_possible_action = q_value_store.get_best_action(state)
            if best_possible_action == actions.UNKNOWN_ACTION \
                    or random.random() < RHO \
                    or q_value_store.get_q_value(state, best_possible_action) == 0:
                best_possible_action = random.choice(maze_problem.get_possible_actions())
            reward, new_state = maze_problem.take_action(best_possible_action)
            q = q_value_store.get_q_value(state, best_possible_action)
            max_q = q_value_store.get_q_value(new_state, q_value_store.get_best_action(new_state))
            q = (1 - ALPHA) * q + ALPHA * (reward + max_q)
            q_value_store.store_value(state, best_possible_action, q)

            time.sleep(0.01)
            counter += 1

            if reward == 100:
                counter = MAX_TRIAL_LENGTH

        no_of_trials += 1


main()
