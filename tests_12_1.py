from runner_1 import Runner
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Rick')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Thomas')
        for j in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Joy")
        runner2 = Runner("Newt")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()