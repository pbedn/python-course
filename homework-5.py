"""
# CLASS

1. Write a Python class to convert an integer to a roman numeral.
"""
arg = 29
expected = "XXIX"


class ConvertIntToRoman:
    """
    Algorithm from
    https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
    """
    INTS = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    NUMS = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
            'V', 'IV', 'I')

    def __init__(self, number):
        assert 0 < number < 4000
        self.number = number

    def run(self):
        result = []
        for i, val in enumerate(self.INTS):
            count = self.number // val
            result.append(self.NUMS[i] * count)
            self.number -= val * count
            if self.number == 0:
                break
        return "".join(result)


assert ConvertIntToRoman(arg).run() == expected


"""
2. Write a Python class to convert a roman numeral to an integer.
"""
arg = "XXIX"
expected = 29


class ConvertRomanToInt:
    """
    Algorithm from
    https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
    """
    ROMAN_DICT = {'M': 1000,
                  'D': 500,
                  'C': 100,
                  'L': 50,
                  'X': 10,
                  'V': 5,
                  'I': 1}

    def __init__(self, roman):
        self.roman = roman

    def run(self):
        int_sum = 0
        for i in range(len(self.roman)):
            try:
                value = self.ROMAN_DICT[self.roman[i]]
                if i + 1 < len(self.roman) and self.ROMAN_DICT[self.roman[i+1]] > value:
                    int_sum -= value
                else:
                    int_sum += value
            except KeyError:
                raise ValueError("Input: {}, is not a valid Roman numeral".format(self.roman))

        assert ConvertIntToRoman(int_sum).run() == self.roman

        return int_sum


assert ConvertRomanToInt(arg).run() == expected


"""
3. Write a Python class to find validity of a string of parentheses,
'(', ')', '{', '}', '[' and ']. These brackets must be close in the correct
order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{"
are invalid.
"""
args = (
    ("()[]{}", True),
    ("(()((())()))", True),
    ("({[)]", False)
)


class FindValidity:
    LEFT = ['(', '[', '{']
    RIGHT = [')', ']', '}']

    def __init__(self, symbol):
        self.symbol = symbol

    def run(self):
        stack = []
        balanced = True

        for s in self.symbol:
            if s in self.LEFT:
                stack.append(s)
            else:
                if not stack:
                    balanced = False
                else:
                    stack.pop()

        if balanced and not stack:
            return True
        return False


for test_input, expected in args:
    assert FindValidity(test_input).run() is expected


"""
4. Write a Python class to get all possible unique subsets from a set of
distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
"""
arg = [4, 5, 6]
expected = [[], [4], [5], [6], [4, 5], [4, 6], [5, 6], [4, 5, 6]]


class GetUniqueSubsets:
    def __init__(self, arg):
        self.arg = arg

    def run(self):
        from itertools import combinations

        res = list()
        for i in range(len(self.arg) + 1):
            for e in combinations(self.arg, i):
                res.append(list(e))
        return res


assert GetUniqueSubsets(arg).run() == expected


"""
5. Write a Python class to find a pair of elements (indices of the two numbers)
from a given array whose sum equals a specific target number.
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 2, 3
"""
arg = ([10, 20, 10, 40, 50, 60, 70], 50)
expected = (2, 3)


class FindPairOfElements:
    def __init__(self, arg):
        self.lst = arg[0]
        self.target = arg[1]

    def run(self):
        res = tuple()
        for i, a in enumerate(self.lst):
            if a == self.target:
                continue
            for j in range(1, len(self.lst)):
                b = self.lst[j]
                if a + b == self.target and i < j:
                    res = (i, j)
        return res


assert FindPairOfElements(arg).run() == expected


"""
6. Write a Python class to find the three elements that sum to zero from a set
of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""
arg = [-25, -10, -7, -3, 2, 4, 8, 10]
expected = [[-10, 2, 8], [-7, -3, 10]]


class FindThreeElements:
    def __init__(self, arg):
        self.arg = arg
        self.length = len(self.arg)

    def run(self):
        res = list()
        for i in range(0, self.length - 2):
            for j in range(i + 1, self.length - 1):
                for k in range(j + 1, self.length):
                    if self.arg[i] + self.arg[j] + self.arg[k] == 0:
                        res.append([self.arg[i], self.arg[j], self.arg[k]])
        return res


assert FindThreeElements(arg).run() == expected


"""
7. Write a Python class to implement pow(x, n).
"""
arg = (2, 3)
expected = 8


class Power:

    def run(self, x, n):
        if n == 0:
            return 1
        elif int(n % 2) == 0:
            return (self.run(x, int(n / 2)) *
                    self.run(x, int(n / 2)))
        else:
            return (x * self.run(x, int(n / 2)) *
                    self.run(x, int(n / 2)))


assert Power().run(*arg) == expected


"""
8. Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'
"""
arg = 'hello .py'
expected = '.py hello'


class ReverseString:
    def __init__(self, arg):
        self.arg = arg

    def run(self):
        return " ".join(list(reversed(self.arg.split(' '))))


assert ReverseString(arg).run() == expected


"""
9. Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in
upper case.
"""


class UserString:
    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input(">>> ")

    def print_string(self):
        print(self.s.upper())


"""
10. Write a Python class named Rectangle constructed by a length and width and
a method which will compute the area of a rectangle.
"""
arg = (10, 10)
expected = 100


class Rectangle:
    def __init__(self, arg):
        self.arg = arg

    def area(self):
        return self.arg[0] * self.arg[1]


assert Rectangle(arg).area() == expected


"""
11. Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle.
"""
arg = 1
area = 3.14159
perimeter = 6.28319

from math import pi, isclose


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * pi * self.radius


assert isclose(Circle(arg).area(), area, rel_tol=True) is True
assert isclose(Circle(arg).perimeter(), perimeter, rel_tol=True) is True
