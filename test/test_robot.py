
import unittest

class Robot(unittest.TestCase):
    def setUp(self):
        self.robot1 = Robot("Robot1")
        self.robot2 = Robot("Robot2")

    def test_robot_str(self):
        self.assertEqual(str(self.robot1), "Robot Robot1")

    def test_robot_fire(self):
        self.robot1.fire(self.robot2)
        self.assertEqual(self.robot2.hit_points, 8)

    def test_robot_isDead(self):
        self.assertFalse(self.robot1.isDead())
        self.robot1.hit_points = 0
        self.assertTrue(self.robot1.isDead())

class Fighter(unittest.TestCase):
    def setUp(self):
        self.fighter1 = Fighter("Fighter1", 123)
        self.fighter2 = Fighter("Fighter2", 456)

    def test_fighter_str(self):
        self.assertEqual(str(self.fighter1), "Fighter Fighter1")

    def test_fighter_fire(self):
        self.fighter1.unittest = unittest.Random(123)  # Set a fixed seed for deterministic testing
        self.fighter1.fire(self.fighter2)
        self.assertEqual(self.fighter2.hit_points, 8)

    def test_fighter_miss_fire(self):
        self.fighter1.unittest = unittest.unittest(123)  # Set a fixed seed for deterministic testing
        self.fighter1.fire(self.fighter2)
        self.assertEqual(self.fighter2.hit_points, 10)

if __name__ == "__main__":
    unittest.main()
