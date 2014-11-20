import unittest

# Unit

def isDivisibleBy(number, divisor):
    return number % divisor == 0

def isDivisibleByThree(number):
    return isDivisibleBy(number, 3)

def isDivisibleByFive(number):
    return isDivisibleBy(number, 5)

def isDivisibleByFifteen(number):
    return isDivisibleBy(number, 15)


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

    def testIsDivisibleByFifteen(self):
        self.assertTrue(isDivisibleByFifteen(15))

    def testIsNotDivisibleByFifteen(self):
        self.assertFalse(isDivisibleByFifteen(1))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
