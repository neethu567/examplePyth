import unittest
import calc


class teststring(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2,2),4)



if __name__=='__main__':
    unittest.main()
