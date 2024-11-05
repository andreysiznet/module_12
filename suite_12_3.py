import unittest
import test_12_3
runnerTEST = unittest.TestSuite()
runnerTEST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runnerTEST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTEST)
