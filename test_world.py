import unittest
from io import StringIO
import sys
from test_base import captured_io, run_unittests
from unittest.mock import patch
import robot
import world.text.world as world


class MyTests(unittest.TestCase):
    def test_do_forward(self):
        robot_name = "Jules"
        steps = 5
        self.assertEqual(world.do_forward(robot_name, steps), (True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'))

    
    def test_do_back(self):
        robot_name = "Jules"
        steps = 5
        self.assertEqual(world.do_back(robot_name, steps), (True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'))


    def test_do_right_turn(self):
        robot_name = "Jules"
        self.assertEqual(world.do_right_turn(robot_name), (True, ' > '+robot_name+' turned right.'))
    

    def test_do_left_turn(self):
        robot_name = "Jules"
        self.assertEqual(world.do_left_turn(robot_name), (True, ' > '+robot_name+' turned left.'))


if __name__ == '__main__':
    unittest.main()