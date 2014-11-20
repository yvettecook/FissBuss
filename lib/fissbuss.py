import unittest

# Unit

def isDivisibleByThree(number):
    return number % 3 == 0

def isDivisibleByFive(number):
    return number % 5 == 0


# Unit Tests

class FissBussTests(unittest.TestCase):

    def testIsDivisibleByThree(self):
        self.assertTrue(isDivisibleByThree(3))

    def testIsNotDivisibleByThree(self):
        self.assertFalse(isDivisibleByThree(1))

    def testIsDivisibleByFive(self):
        self.assertTrue(isDivisibleByFive(5))

    def testIsNotDivisibleByFive(self):
        self.assertFalse(isDivisibleByFive(1))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
