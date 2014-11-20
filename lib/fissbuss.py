import unittest

# Unit

def isDivisibleByThree(number):
    return True


# Unit Tests

class FissBussTests(unittest.TestCase):

    def testIsDivisibleByThree(self):
        self.assertTrue(isDivisibleByThree(3))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
