import unittest
from q_value_store import QValueStore
from maze_problem import MazeProblem
import actions


class TestLearning(unittest.TestCase):
    def test_store(self):
        q_value_store = QValueStore()

        self.assertEqual(q_value_store.get_q_value((3, 0), actions.EAST), 0)
        self.assertEqual(q_value_store.get_best_action((2, 5)), actions.UNKNOWN_ACTION)

        q_value_store.store_value((3, 7), actions.EAST, 0.3)
        q_value_store.store_value((0, 2), actions.NORTH, 0.4)
        q_value_store.store_value((3, 7), actions.NORTH, 0.5)

        self.assertEqual(q_value_store.get_q_value((3, 7), actions.EAST), 0.3)
        self.assertEqual(q_value_store.get_q_value((3, 7), actions.SOUTH), 0)
        self.assertEqual(q_value_store.get_q_value((0, 2), actions.NORTH), 0.4)
        self.assertEqual(q_value_store.get_q_value((3, 7), actions.NORTH), 0.5)

        q_value_store.store_value((3, 7), actions.EAST, 0.6)
        self.assertEqual(q_value_store.get_q_value((3, 7), actions.EAST), 0.6)

        self.assertEqual(q_value_store.get_best_action((3, 7)), actions.EAST)
        q_value_store.store_value((3, 7), actions.NORTH, 0.7)
        q_value_store.store_value((3, 7), actions.SOUTH, 0.1)
        self.assertEqual(q_value_store.get_best_action((3, 7)), actions.NORTH)

    def test_initial_position(self):
        for i in range(10000):
            maze_problem = MazeProblem()
            self.assertEqual(maze_problem.get_maze_definition()[maze_problem._y][maze_problem._x], 0)

    def test_possible_actions(self):
        # Corners
        maze_problem = MazeProblem((0, 0))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.SOUTH, actions.EAST])

        maze_problem = MazeProblem((19, 0))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.SOUTH, actions.WEST])

        maze_problem = MazeProblem((0, 19))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.NORTH, actions.EAST])

        maze_problem = MazeProblem((19, 19))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.NORTH, actions.WEST])

        # Sides
        maze_problem = MazeProblem((10, 0))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.SOUTH, actions.EAST, actions.WEST])

        maze_problem = MazeProblem((19, 10))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.NORTH, actions.SOUTH, actions.WEST])

        maze_problem = MazeProblem((10, 19))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.NORTH, actions.EAST, actions.WEST])

        maze_problem = MazeProblem((0, 10))
        self.assertEqual(maze_problem.get_possible_actions(), [actions.NORTH, actions.SOUTH, actions.EAST])

        # Next to walls
        maze_problem = MazeProblem((2, 1))
        self.assertEqual(maze_problem.get_maze_definition()[2][2], 1)
        self.assertEqual(maze_problem.get_possible_actions(), [actions.NORTH, actions.EAST, actions.WEST])

        maze_problem = MazeProblem((2, 10))
        self.assertEqual(maze_problem.get_maze_definition()[9][2], 1)
        self.assertEqual(maze_problem.get_possible_actions(), [actions.SOUTH, actions.EAST, actions.WEST])

        maze_problem = MazeProblem((12, 6))
        self.assertEqual(maze_problem.get_maze_definition()[5][12], 1)
        self.assertEqual(maze_problem.get_possible_actions(), [actions.SOUTH, actions.EAST, actions.WEST])

    def test_take_action(self):
        with self.assertRaises(RuntimeError):
            maze_problem = MazeProblem((0, 0))
            maze_problem.take_action(actions.NORTH)

        with self.assertRaises(RuntimeError):
            maze_problem = MazeProblem((0, 0))
            maze_problem.take_action(actions.WEST)

        with self.assertRaises(RuntimeError):
            maze_problem = MazeProblem((19, 19))
            maze_problem.take_action(actions.SOUTH)

        with self.assertRaises(RuntimeError):
            maze_problem = MazeProblem((19, 19))
            maze_problem.take_action(actions.EAST)

        with self.assertRaises(RuntimeError):
            maze_problem = MazeProblem((3, 1))
            maze_problem.take_action(actions.SOUTH)

        maze_problem = MazeProblem((14, 4))
        maze_problem.take_action(actions.EAST)
        self.assertEqual(maze_problem.get_state(), (15, 4))
        maze_problem.take_action(actions.NORTH)
        self.assertEqual(maze_problem.get_state(), (15, 3))
        maze_problem.take_action(actions.WEST)
        self.assertEqual(maze_problem.get_state(), (14, 3))
        maze_problem.take_action(actions.SOUTH)
        self.assertEqual(maze_problem.get_state(), (14, 4))
