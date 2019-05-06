"""
FUNCTIONS:
1. Write a Python function to find the Max of three numbers.
"""
arg = (1, 5, 3)
expected = 5


def h1(t: tuple) -> int:
    return max(t)


assert h1(arg) == expected

"""
2. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""
arg = "1234abcd"
expected = "dcba4321"


def h2(s: str) -> str:
    return "".join(reversed(s))


assert h2(arg) == expected

"""
3. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""
arg = (8, 2, 3, 0, 7)
expected = 20


def h3(t: tuple) -> int:
    return sum(t)


assert h3(arg) == expected

"""
4. Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
"""
arg = 3
expected = 6


def h4(n: int) -> int:
    return n * h4(n-1) if n > 1 else n


assert h4(arg) == expected

"""
5. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""
arg = (8, 2, 3, -1, 7)
expected = -336


def h5(t: tuple) -> int:
    from operator import mul
    from functools import reduce
    return reduce(mul, t)


assert h5(arg) == expected

"""
6. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""
arg = 'The quick Brow Fox'
expected = "No. of Upper case characters : 3\nNo. of Lower case Characters : 12"


def h6(s: str) -> str:
    upper = sum(1 for letter in s if letter.isupper())
    lower = sum(1 for letter in s if letter.islower())
    return f"No. of Upper case characters : {upper}\nNo. of Lower case Characters : {lower}"


assert h6(arg) == expected

"""
7. Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
arg = [1, 2, 3, 3, 3, 3, 4, 5]
expected = [1, 2, 3, 4, 5]


def h7(l: list) -> list:
    return list(set(l))


assert h7(arg) == expected

"""
8. Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
"""
arg = 5
arg2 = 6
expected = True
expected2 = False


def h8(n: int) -> bool:
    assert n > 1
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


assert h8(arg) == expected
assert h8(arg2) == expected2

"""
9. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.
"""
arg = "This is some string"
expected = "<b><i><u>This is some string</u></i></b>"


def decorate(a):
    def decorator(f):
        def wrapper(s):
            return f"<{a}>{f(s)}</{a}>"
        return wrapper
    return decorator


@decorate('b')
@decorate('i')
@decorate('u')
def h9(s: str) -> str:
    return s


assert h9(arg) == expected

"""
10. Write a Python program to execute a string containing Python code.
"""


def h10(s: str) -> int:
    return exec(s)


"""
11. Write a Python program to access a function inside a function.
"""
arg = 1
expected = 2


def h11():
    def function(b: int) -> int:
        return b + 1
    return function


f = h11()

assert f(arg) == expected

"""
12. Write a Python program to detect the number of local variables declared in a function.
"""
expected = 3


def h12():
    a = 5
    b = 10
    c = 11
    return len(locals())


assert h12() == expected

"""
13. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""
arg = [1, 2, 3, 4, 5, 6, 7, 8, 9]
expected = [2, 4, 6, 8]


def h13(l: list) -> list:
    return list(filter(lambda x: x % 2 == 0, l))


assert h13(arg) == expected

"""
14. Write a Python function to check whether a number is perfect or not.
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

Answer: repeated h22 from homework 2
"""

"""
15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

Answer: repeated h21 from homework 2
"""

"""
MODULES:
Write Python module example with proper structure

Answer: This file is a Python module
"""
