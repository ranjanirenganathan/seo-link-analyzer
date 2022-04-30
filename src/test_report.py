import unittest
import report


class Test(unittest.TestCase):
    def test_remove_none_values(self):
        self.assertEqual({}, report.remove_none_values({"1": None}))
        self.assertEqual({"1": "1"}, report.remove_none_values({"1": "1", "2": None}))
        self.assertEqual({}, report.remove_none_values({}))
        self.assertEqual({"1": "1"}, report.remove_none_values({"1": "1"}))

    def test_sort_pages(self):
        self.assertEqual([("0", 45), ("1", 35), ("2", 25), ("3", 0)],
                         report.sort_pages({"3": 0, "1": 35, "2": 25, "0": 45}),
                         )
        self.assertEqual([("0", 3), ("1", 2), ("2", 1), ("3", 0)],
                         report.sort_pages({"3": 0, "1": 2, "2": 1, "0": 3}),
                         )
        self.assertEqual([], report.sort_pages({}), )


if __name__ == "__main__":
    unittest.main()
