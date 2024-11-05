import tests_12_2
import unittest
from tests_12_1 import Runner

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 10


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = Runner("walk")
        for _ in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r = Runner("run")
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner("run_1")
        r2 = Runner("run_2")
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)
    def setUp(self):
        self.usain = tests_12_2.Runner('Усэйн', 10)
        self.andrew = tests_12_2.Runner('Андрей', 9)
        self.nick = tests_12_2.Runner('Ник', 3)
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_first(self):
        first_run = tests_12_2.Tournament(90, self.usain, self.nick)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_second(self):
        second_run = tests_12_2.Tournament(90, self.andrew, self.nick)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_third(self):
        third_run = tests_12_2.Tournament(90, self.andrew, self.usain, self.nick)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result
if __name__ == '__main__':
    unittest.main()

