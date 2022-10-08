from ctypes import _NamedFuncPointer
import unittest
import Calc


class testCalc(unittest.TestCase):

    def test_add(self):
        result = Calc.add(10, 5)
        self.assertEqual(Calc.add(10, 5), 15)
        self.assertEqual(Calc.add(-1, 1), 0)
        self.assertEqual(Calc.add(-1, -1), -2)

    def test_subtract(self):
        result = Calc.add(10, 5)
        self.assertEqual(Calc.add(10, 5), 5)
        self.assertEqual(Calc.add(-1, 1), -2)
        self.assertEqual(Calc.add(-1, -1), 0)

    def test_multiply(self):
        result = Calc.add(10, 5)
        self.assertEqual(Calc.add(10, 5), 50)
        self.assertEqual(Calc.add(-1, 1), -1)
        self.assertEqual(Calc.add(-1, -1), 1)

    def test_divide(self):
        result = Calc.add(10, 5)
        self.assertEqual(Calc.add(10, 5), 2)
        self.assertEqual(Calc.add(-1, 1), -1)
        self.assertEqual(Calc.add(-1, -1), 1)
        self.assertEqual(Calc.add(5, 2), 2.5)

        with self.assertRaises(ValueError):            Calc.divide(10, 0)
if __name__ == '__main__':
    unittest.main()