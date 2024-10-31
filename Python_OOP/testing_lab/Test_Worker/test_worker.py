from Python_OOP.testing_lab.Test_Worker.worker import Worker


from unittest import TestCase, main


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Test", #arrange
                             1000,
                             100)

    def test_innit_of_worker(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_the_work_exception_when_the_worker_has_zero_or_less_energy(self):
        self.worker.energy = 0  #arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))
        self.assertEqual(0, self.worker.money)
        self.assertEqual(0, self.worker.energy)

        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))
        self.assertEqual(0, self.worker.money)
        self.assertEqual(-1, self.worker.energy)

    def test_the_work_when_the_worker_has_more_than_zero_energy(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_the_rest_increase_energy(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_the_get_info_returning_a_string(self):
        expected_string = f'{self.worker.name} has saved {self.worker.money} money.'

        self.assertEqual(expected_string, self.worker.get_info())


if __name__ == "__main__":
    main()