import unittest
import filter


class TestFilter(unittest.TestCase):
    def test_read_file(self):
        path_to_test_file = "./data.txt"
        self.assertIsInstance(filter.read_file(path_to_test_file), list)

    # def test_format_data_set(self):



if __name__ == "__main__":
    unittest.main()
