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

def fissBuss(number):
    if isDivisibleByFifteen(number):
        return 'fissbuss'
    if isDivisibleByThree(number):
        return 'fiss'
    if isDivisibleByFive(number):
        return 'buss'
    else:
        return number


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

    def testSayFiss(self):
        self.assertEqual('fiss', fissBuss(3))

    def testSayBuss(self):
        self.assertEqual('buss', fissBuss(5))

    def testSayFissBuss(self):
        self.assertEqual('fissbuss', fissBuss(15))

    def testSayNumber(self):
        self.assertEqual(1, fissBuss(1))





def main():
    unittest.main()

if __name__ == '__main__':
    main()
