import unittest
import test_problem

class TestUnitCode(unittest.TestCase):
    def test_check(self):
        result = test_problem.checknumber(5)
        self.assertEqual(result,True)

    def test_check_operator(self):
        result = test_problem.checkoperator("+")
        self.assertEqual(result,True)

    def test_solver(self):
        result = test_problem.solver("5-6")
        self.assertEqual(result,-1)

if __name__ == '__main__':
    unittest.main()
