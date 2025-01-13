import unittest
import tests_12_3

testsST = unittest.TestSuite()

testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testsST)

