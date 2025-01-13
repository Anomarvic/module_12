import unittest
import tests_12_1
import tests_12_2

testsST = unittest.TestSuite()

testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testsST)

