import unittest
from tack1 import File
import os
class TestFile(unittest.TestCase):

    def test_file_open(self):
        with File('myfile.txt', 'w') as file:
            self.assertFalse(file.closed,'File open error')

    def test_file_close(self):
        with File('myfile.txt', 'w') as file:
            self.assertTrue(os.path.exists('myfile.txt'))

    def test_counter(self):
        with File('myfile.txt', 'r') as file:
            file.read()
        with File('myfile.txt', 'r') as file:
            file.read()
        self.assertEqual(File.COUNTER,2,'Counter error!')


if __name__ == '__main__':
    unittest.main()