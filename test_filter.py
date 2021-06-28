import unittest
import filter


class TestFilter(unittest.TestCase):
    def setUp(self):
        self.sample_data_unformated = [
            "1426828011 9",
            "1426828028 350",
            "1426828037 25",
            "1426828056 231",
            "1426828058 109",
            "1426828066 111",
        ]

        self.sample_data_formated = [
            ("1426828011", 9),
            ("1426828028", 350),
            ("1426828037", 25),
            ("1426828056", 231),
            ("1426828058", 109),
            ("1426828066", 111),
        ]

        self.sample_highest_id = ["1426828028"]
        self.sample_three_highest_ids = ["1426828028", "1426828056", "1426828066"]
        self.sample_five_highest_ids = [
            "1426828028",
            "1426828056",
            "1426828066",
            "1426828037",
            "1426828058",
        ]
        self.sample_all_ids = [
            "1426828028",
            "1426828056",
            "1426828066",
            "1426828058",
            "1426828037",
            "1426828011",
        ]

        self.n_output = 3

    def tearDown(self):
        # currently no specific teardown required
        pass

    def test_read_file(self):
        path_to_test_file = "./data.txt"
        data_read_from_file = filter.read_file(path_to_test_file)
        self.assertIsInstance(data_read_from_file, list)
        self.assertEqual(data_read_from_file, self.sample_data_unformated)

    def test_format_dataset(self):
        data_formated = filter.format_dataset(self.sample_data_unformated)
        self.assertEqual(data_formated, self.sample_data_formated)

    def test_max_loop(self):
        three_highest_ids = filter.max_loop(self.sample_data_formated, self.n_output)
        self.assertCountEqual(three_highest_ids, self.sample_three_highest_ids)

    def test_min_loop(self):
        three_highest_ids = filter.min_loop(self.sample_data_formated, self.n_output, 6)
        self.assertCountEqual(three_highest_ids, self.sample_three_highest_ids)

    def test_main(self):
        calling_max_loop = filter.main(1)
        calling_min_loop = filter.main(5)
        calling_sort = filter.main(3)
        returning_all_ids = filter.main(6)

        self.assertEqual(calling_max_loop, self.sample_highest_id)
        self.assertCountEqual(calling_min_loop, self.sample_five_highest_ids)
        self.assertCountEqual(calling_sort, self.sample_three_highest_ids)
        self.assertCountEqual(returning_all_ids, self.sample_all_ids)
        self.assertRaises(ValueError, filter.main, 7)


if __name__ == "__main__":
    unittest.main()
