from runner import Runner
from runner import Tournament
import unittest


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result, test_name in cls.all_results.items():
            print(f'{result}:{test_name}')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_1_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.runner3)
        # чтобы выводились имена, а не ссылки на объекты конвертируем словарь в другой словарь
        all_results_with_names = {result: runner.name for (result, runner) in self.all_results.items()}
        print(all_results_with_names)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_2_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.runner3)
        # чтобы выводились имена, а не ссылки на объекты конвертируем словарь в другой словарь
        all_results_with_names = {result: runner.name for (result, runner) in self.all_results.items()}
        print(all_results_with_names)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_3_all(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())] == self.runner3)
        # чтобы выводились имена, а не ссылки на объекты конвертируем словарь в другой словарь
        all_results_with_names = {result: runner.name for (result, runner) in self.all_results.items()}
        print(all_results_with_names)

    if __name__ == '__main__':
        unittest.main()

