"""
### LIST

1. Write a Python program to check if all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""
a = [{}, {}, {}]
b = [{1, 2}, {}, {}]


def h1(lst):
    return not any(e for e in lst)


assert h1(a) is True
assert h1(b) is False

"""
2. Write a Python program to remove duplicates from a list of lists. Go to the
editor
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
"""

lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
expected = [[10, 20], [30, 56, 25], [33], [40]]


def h2_a(lst):
    """Does not preserve order"""
    new = []
    for e in lst:
        if e not in new:
            new.append(e)
    return sorted(new)


assert h2_a(lst) == expected


"""
3. Write a Python program to find the list in a list of lists whose sum of
elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
"""

lst = [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]
expected = [10, 11, 12]


def h3(lst):
    return max([(l, sum(l)) for l in lst], key=lambda x: x[1])[0]


assert h3(lst) == expected

"""
4. Write a Python program to compute the similarity between two lists.
Sample data: ["red", "orange", "green", "blue", "white"],
["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
"""

a, b = ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
expected1 = ['white', 'orange', 'red']
expected2 = ['black', 'yellow']
expected = (set(expected1), set(expected2))


def h4(a, b):
    return set(a) - set(b), set(b) - set(a)


assert h4(a, b) == expected

"""
5. Write a Python program to change the position of every n-th value with the (n+1)
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
"""

lst = [0, 1, 2, 3, 4, 5]
expected = [1, 0, 3, 2, 5, 4]


def h5(lst):
    for i, _ in enumerate(lst):
        if i % 2 == 0:
            lst[i+1], lst[i] = lst[i], lst[i+1]
    return lst


assert h5(lst) == expected

"""
6. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
expected = [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


def h6(lst):
    return sorted(lst, key=lambda x: x[1])


assert h6(lst) == expected

"""
7. Write a Python program to count the number of strings where the string length
 is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

lst = ['abc', 'xyz', 'aba', '1221']
expected = 2


def h7(lst):
    return sum(1 for e in lst if len(e) >= 2 and e[0] == e[-1])


assert h7(lst) == expected

"""
### TUPLE

8. Write a Python program to print a tuple with string formatting.
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)
"""

t = (100, 200, 300)
expected = "This is a tuple (100, 200, 300)"


def h8(t):
    return f"This is a tuple {t}"


assert h8(t) == expected


"""
9. Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
expected = [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


def h9(lst):
    return [t[:-1] + (100,) for t in lst]


assert h9(lst) == expected

"""
10. Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""

lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
expected = [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']


def h10(lst):
    return [e for e in lst if e]


assert h10(lst) == expected

"""
11. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""

lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
expected = [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


def h11(lst):
    return sorted(lst, key=lambda x: x[1], reverse=True)


assert h11(lst) == expected

"""
### SET

12. Write a Python program to create a shallow copy of sets.

Note : Shallow copy is a bit-wise copy of an object. A new object is created
that has an exact copy of the values in the original object.
"""

s = {1, 2, 3}
expected = {1, 2, 3}


def h12(s):
    return s.copy()


assert id(h12(s)) != expected

"""
13. Write a Python program to remove an item from a set if it is present in the set.
"""

s = {1, 2, 3}
s2 = {1, 2}
item = 3
expected = {1, 2}


def h13(s, item):
    s.discard(item)
    return s


assert h13(s, item) == expected
assert h13(s2, item) == expected


"""
### DICT

14. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
       {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
expected = {'S005', 'S002', 'S007', 'S001', 'S009'}


def h14(lst):
    return {v for d in lst for v in d.values()}


assert h14(lst) == expected

"""
15. Write a Python program to create and display all combinations of letters,
 selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""
dct = {'1': ['a', 'b'], '2': ['c', 'd']}
dct2 = {'1': ['a', 'b'], '2': ['c', 'd', 'e'], '3': ['g']}
expected = ['ac', 'ad', 'bc', 'bd']
expected2 = ['acg', 'adg', 'aeg', 'bcg', 'bdg', 'beg']


def h15(dct):
    from itertools import product
    return [''.join(c) for c in product(*dct.values())]


assert h15(dct) == expected
assert h15(dct2) == expected2

"""
16. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""

s = 'w3resource'
expected = {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


def h16(s):
    from collections import Counter
    return Counter(s)


assert h16(s) == expected

"""
17. Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
"""

dct = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
expected = ["item4 55", "item1 45.5", "item3 41.3"]


def h17(dct):
    highest = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    return [f"{k} {v}" for k, v in highest[:3]]


assert h17(dct) == expected

"""
18. Write a Python program to create a dictionary from two lists without losing
duplicate values.
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}}
"""

lst1, lst2 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
expected = {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}}


def h18(lst1, lst2):
    return dict(zip(lst1, [{e,} for e in lst2]))


assert h18(lst1, lst2) == expected

"""
19. Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
"""

dct1, dct2 = {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
expected = "key1: 1 is present in both x and y"


def h19(dct1, dct2):
    for k, v in dct1.items():
        for kk, vv in dct2.items():
            if k == kk and v == vv:
                res_k, res_v = k, v
    return f"{res_k}: {res_v} is present in both x and y"


assert h19(dct1, dct2) == expected


"""
### FUNC

20. Write a Python function to sum all the numbers in a list.
Sample List : [8, 2, 3, 0, 7]
Expected Output : 20
"""

lst = [8, 2, 3, 0, 7]
expected = 20


def h20(lst):
    return sum(lst)


assert h20(lst) == expected


"""
21.Write a Python program that accepts a hyphen-separated sequence of words as
input and prints the words in a hyphen-separated sequence after sorting them
alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
"""

s = "green-red-yellow-black-white"
expected = "black-green-red-white-yellow"


def h21(s):
    return "-".join(sorted(s.split("-")))


assert h21(s) == expected


"""
22. Write a Python function to check whether a number is perfect or not.
According to Wikipedia : In number theory, a perfect number is a positive integer
 that is equal to the sum of its proper positive divisors, that is, the sum of
 its positive divisors excluding the number itself (also known as its aliquot sum).
 Equivalently, a perfect number is a number that is half the sum of all of its positive
 divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper
positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to
half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next
perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect
numbers 496 and 8128.
"""

lst = list(range(1, 10000))
expected = [6, 28, 496, 8128]


def h22(lst):
    perfect = []
    for i in lst:
        divisors = []
        for j in range(1, i):
            if i % j == 0:
                divisors.append(j)
        if sum(divisors) == i and (sum(divisors) + i) / 2 == i:
            perfect.append(i)
    return perfect


assert h22(lst) == expected


"""
23. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
Click me to see the sample solution
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
expected = [2, 4, 6, 8]


def h23(lst):
    return [i for i in lst if i % 2 == 0]


assert h23(lst) == expected
