from unittest import TestCase
import runner


class CalkTest(TestCase):
    def test_walk(self):
        runner_1 = runner.Runner('Maxim')
        for n in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runner.Runner('Oleg')
        for n in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = runner.Runner('Olga')
        runner_4 = runner.Runner('Petr')
        for n in range(10):
            runner_3.walk()
            runner_4.walk()
        d_1 = runner_3.distance
        d_2 = runner_4.distance
        for n in range(10):
            runner_3.run()
            runner_4.run()
        d_3 = runner_3.distance
        d_4 = runner_4.distance
        self.assertNotEqual(d_1, d_3)
        self.assertNotEqual(d_2, d_4)

if __name__ == "__main__":
    unittest.main
