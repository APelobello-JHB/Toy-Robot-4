import unittest
from io import StringIO
import sys
from test_base import captured_io, run_unittests
from unittest.mock import patch
import robot
import world.obstacles as obstacles
import world.text.world as world


class MyTests(unittest.TestCase):
    def test_get_robot_name(self):
        with captured_io(StringIO("Jules\n")):
            self.assertEqual(robot.get_robot_name(), 'Jules')


    def test_do_help(self):
        with captured_io(StringIO("help")):
            self.assertEqual(robot.do_help(), (True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""))


    def test_get_command(self):
        with captured_io(StringIO("forward 10")): 
            self.assertEqual(robot.get_command("Jules"), "forward 10")


    def test_split_command_input(self): 
        with captured_io(StringIO("forward 10")):
            self.assertEqual(robot.get_command("forward 10"), "forward 10")

    
    def test_valid_command_do_replay(self):
        with captured_io(StringIO("replay")):
            self.assertEqual(robot.valid_command("replay"), True)
    

    
if __name__ == '__main__':
    unittest.main()

