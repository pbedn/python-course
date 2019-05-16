"""
1. Write a Python program to create an Enum object and display a member name
and value.
Sample data :
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
Expected Output :
Member name: Albania
Member value: 355
"""
from enum import Enum


class SampleEnum(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


def h1():
    return SampleEnum


"""
2. Write a Python program to iterate over an enum class and display individual
member and their value.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
"""


def h2():
    for c in SampleEnum:
        yield c.name, c.value


"""
3. Write a Python program to display all the member name of an enum class
ordered by their values.
Expected Output:
Country Name ordered by Country Code:
Afghanistan
Algeria
Angola
Albania
Andorra
Antarctica
"""


def h3():
    pass


"""
4. Write a Python program to get all values from an enum class.
Expected output:
[93, 355, 213, 376, 244, 672]
"""


def h4():
    pass


"""
5. Write a Python program to count the most common words in a dictionary.
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
"""


def h5():
    pass


"""
6. Write a Python program to find the class wise roll number from a tuple-of-tuples.
Expected Output:
defaultdict(, {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]})
"""


def h6():
    pass


"""
7. Write a Python program to count the number of students of individual class.
Sample data:
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)
Expected Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})
"""


def h7():
    pass


"""
8.Write a Python program to get the unique enumeration values.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
"""


def h8():
    pass


"""
9. Write a Python program to create an instance of an OrderedDict using a given
dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.
Expected Output:
Angola 244
Andorra 376
Algeria 213
Afghanistan 93
Albania 355
In reverse order:
Albania 355
Afghanistan 93
Algeria 213
Andorra 376
Angola 244
"""


def h9():
    pass


"""
10. Write a Python program to group a sequence of key-value pairs into a
dictionary of lists.
Expected output:
[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]
"""


def h10():
    pass


"""
11. Write a Python program to compare two unordered lists (not sets).
Expected Output: False
"""


def h11():
    pass


"""
12. Write a Python program to create an array contains six integers. Also print all the members of the array.
Expected Output:
10
20
30
40
50
"""


def h12():
    pass


"""
13. Write a Python program to get the array size of types unsigned integer and float.
Expected Output:
4
4
"""


def h13():
    pass


"""
14. Write a Python program to get an array buffer information.
Expected Output:
Array buffer start address in memory and number of elements.
(25855056, 2)
"""


def h14():
    pass


"""
15. Write a Python program to get the length of an array.
Expected Output:
Length of the array is:
5
"""


def h15():
    pass


"""
16. Write a Python program to convert an array to an ordinary list with the same items.
Expected Output:
Original array:
array('b', [1, 2, 3, 4])
Array to list:
[1, 2, 3, 4]
"""


def h16():
    pass


"""
17. Write a Python program to convert an array to an array of machine values and return the bytes representation.
Expected Output:
Original array:
A1: array('i', [1, 2, 3, 4, 5, 6])
Array of bytes: b'010000000200000003000000040000000500000006000000'
"""


def h17():
    pass


"""
18. Write a Python program to read a string and interpreting the string as an array of machine values.
Expected Output:
array1: array('i', [7, 8, 9, 10])
Bytes: b'0700000008000000090000000a000000'
array2: array('i', [7, 8, 9, 10])
"""


def h18():
    pass


"""
19. Write a Python program to push three items into the heap and print the items from the heap.
Expected Output:
('V', 1)
('V', 2)
('V', 3)
"""


def h19():
    pass


"""
20. Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap.
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2)
----------------------
The smallest item in the heap:
('V', 1)
----------------------
Pop the smallest item in the heap:
('V', 2)
('V', 3)
"""


def h20():
    pass


"""
21. Write a Python program to push an item on the heap, then pop and return the smallest item from the heap.
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2)
----------------------
Using heappushpop push item on the heap and return the smallest item.
('V', 2)
('V', 3)
('V', 6)
"""


def h21():
    pass


"""
22. Write a Python program to create a heapsort, pushing all values onto a heap
and then popping off the smallest values one at a time.
Expected Output:
[10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
"""


def h22():
    pass


"""
23. Write a Python program to get the two largest and three smallest items
from a dataset.
Expected Output:
[100, 90]
[10, 20, 20]
"""


def h23():
    pass


"""
24. Write a Python program to locate the left insertion point for a
specified value in sorted order.
Expected Output:
4
2
"""


def h24():
    pass


"""
25. Write a Python program to locate the right insertion point for a
specified value in sorted order.
Expected Output:
3
2
"""


def h25():
    pass


"""
26. Write a Python program to insert items into a list in sorted order.
Expected Output:
Original List:
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
Sorted List:
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
"""


def h26():
    pass


"""
27. a Python program to create a queue and display all the members and size
of the queue.
Expected Output:
Members of the queue:
0 1 2 3
Size of the queue:
4
"""


def h27():
    pass


"""
28. Write a Python program to find whether a queue is empty or not.
Expected Output:
True
False
"""


def h28():
    pass


"""
29. Write a Python program to create a FIFO queue.
Expected Output:
0 1 2 3
"""


def h29():
    pass


"""
30. Write a Python program to create a LIFO queue.
Expected Output:
3 2 1 0
"""


def h30():
    pass
