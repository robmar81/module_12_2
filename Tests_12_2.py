import runner_and_tournament as rat
import unittest
import inspect


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.rnr1 = rat.Runner('Усэйн', 10)
        self.rnr2 = rat.Runner('Андрей', 9)
        self.rnr3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({key: str(value) for key, value in cls.all_results[test].items()})

    def testUsainNik(self):
        tournament = rat.Tournament(90, self.rnr1, self.rnr3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def testAndreyNik(self):
        tournament = rat.Tournament(90, self.rnr2, self.rnr3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def testUsainAndreyNik(self):
        tournament = rat.Tournament(90, self.rnr1, self.rnr2, self.rnr3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == "__main__":
    unittest.main()
