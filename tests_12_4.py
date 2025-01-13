import logging
from runner_1 import Runner
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    def test_walk(self):
        runner = Runner('Rick')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Thomas')
        for j in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Joy")
        runner2 = Runner("Newt")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding=UTF-8, format='%(levelname)s | %(message)s')
    unittest.main()

