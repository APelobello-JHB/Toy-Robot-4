import unittest
from io import StringIO
import sys
from test_base import captured_io, run_unittests
from unittest.mock import patch
import robot
from world import obstacles as obstacles


class MyTests(unittest.TestCase):
    def test_is_position_blocked(self):
            obstacles.random.randint: lambda a, b: 10
            obstacles.get_obstacles()

            self.assertEqual(obstacles.is_position_blocked(10, 10), False)
            self.assertEqual(obstacles.is_position_blocked(20, 20), False)


    def test_is_position_blocked_within_4_spaces(self):
            obstacles.random.randint: lambda a, b: 20
            obstacles.get_obstacles()

            self.assertEqual(obstacles.is_position_blocked(12, 10), False)
            self.assertEqual(obstacles.is_position_blocked(11, 12), False)
            self.assertEqual(obstacles.is_position_blocked(16, 20), False)
            self.assertEqual(obstacles.is_position_blocked(14, 14), False)
    

    def test_is_path_blocked(self):
            obstacles.random.randint: lambda a, b: 50
            obstacles.get_obstacles()

            self.assertEqual(obstacles.is_position_blocked(12, 10), False)
            self.assertEqual(obstacles.is_position_blocked(20, 40), False)


if __name__ == '__main__':
    unittest.main()