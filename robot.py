class Robot:
    def __init__(self, name):
        self.name = name
        self.hit_points = 10

    def __str__(self):
        return "Robot " + self.name

    def fire(self, target_robot):
        target_robot.hit_points -= 2
        print("Robot", self.name, "was hit by Robot", target_robot.name + "!")

    def isDead(self):
        return self.hit_points <= 0


class Arena:
    def fight(self, robot1, robot2):
        while not robot1.isDead() and not robot2.isDead():
            robot1.fire(robot2)
            if not robot2.isDead():
                robot2.fire(robot1)

        if robot1.isDead():
            return robot2
        else:
            return robot1


# Test fight between D2R2 and Data
d2r2 = Robot("D2R2")
data = Robot("Data")

arena = Arena()
winner = arena.fight(d2r2, data)

print("The winner is", winner)

# EXERCISE 2

import unittest

class Fighter(Robot):
    def __init__(self, name, seed):
        super().__init__(name)
        self.seed = seed
        self.random = random.Random(seed)

    def __str__(self):
        return "Fighter " + self.name

    def fire(self, target_robot):
        if self.random.choice([True, False]):
            target_robot.hit_points -= 2
            print("Fighter", self.name, "hits Robot", target_robot.name + "!")
        else:
            print("Fighter", self.name, "misses the shot!")

# test 
            
            import unittest;

class TestRobot(unittest.TestCase):
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

class TestFighter(unittest.TestCase):
    def setUp(self):
        self.fighter1 = Fighter("Fighter1", 123)
        self.fighter2 = Fighter("Fighter2", 456)

    def test_fighter_str(self):
        self.assertEqual(str(self.fighter1), "Fighter Fighter1")

    def test_fighter_fire(self):
        self.fighter1.random = unittest.Random(123)  # Set a fixed seed for deterministic testing
        self.fighter1.fire(self.fighter2)
        self.assertEqual(self.fighter2.hit_points, 8)

    def test_fighter_miss_fire(self):
        self.fighter1.random = unittest.Random(123)  # Set a fixed seed for deterministic testing
        self.fighter1.fire(self.fighter2)
        self.assertEqual(self.fighter2.hit_points, 10)

if __name__ == "__main__":
    unittest.main()
