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
from enum import Enum, IntEnum


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


class SampleEnum2(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


def h3():
    for c in sorted(SampleEnum2):
        yield c.name


"""
4. Write a Python program to get all values from an enum class.
Expected output:
[93, 355, 213, 376, 244, 672]
"""


def h4():
    for c in SampleEnum:
        yield c.value


"""
5. Write a Python program to count the most common words in a dictionary.
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
"""


def h5(dct):
    from collections import Counter
    return Counter(dct).most_common(4)


"""
6. Write a Python program to find the class wise roll number from a tuple-of-tuples.
Expected Output:
defaultdict(, {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]})
"""


def h6(classes):
    from collections import defaultdict
    class_roll_number = defaultdict(list)

    for class_name, roll_id in classes:
        class_roll_number[class_name].append(roll_id)

    return class_roll_number


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


def h7(students):
    from collections import Counter
    return Counter(name for name, _ in students)


"""
8.Write a Python program to get the unique enumeration values.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
"""


class Countries(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213


def h8():
    for country in Countries:
        yield country.name, country.value


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


def h9(dct, reverse=False):
    from collections import OrderedDict
    new_dict = OrderedDict(dct.items())

    if reverse:
        print('In reverse order:')
        for key, value in reversed(new_dict.items()):
            yield key, value
    else:
        for key, value in new_dict.items():
            yield key, value


"""
10. Write a Python program to group a sequence of key-value pairs into a
dictionary of lists.
Expected output:
[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]
"""


def h10(dct):
    from collections import defaultdict
    d = defaultdict(list)
    for k, v in dct:
        d[k].append(v)
    return sorted(d.items())


"""
11. Write a Python program to compare two unordered lists (not sets).
Expected Output: False
"""


def h11(l1, l2):
    return l1 == l2


"""
12. Write a Python program to create an array contains six integers. Also print all the members of the array.
Expected Output:
10
20
30
40
50
"""


def h12(lst):
    from array import array
    my_array = array('i', lst)
    for i in my_array:
        yield i


"""
13. Write a Python program to get the array size of types unsigned integer and float.
Expected Output:
4
4
"""


def h13(a):
    sign = 'I'
    if isinstance(a[0], float) or isinstance(a[1], float):
        sign = 'f'
    from array import array
    arr = array(sign, a)
    return arr.itemsize


"""
14. Write a Python program to get an array buffer information.
Expected Output:
Array buffer start address in memory and number of elements.
(25855056, 2)
"""


def h14(lst):
    from array import array
    num_array = array('i', lst)
    return num_array.buffer_info()


"""
15. Write a Python program to get the length of an array.
Expected Output:
Length of the array is:
5
"""


def h15(lst):
    from array import array
    num_array = array('i', lst)
    return len(num_array)


"""
16. Write a Python program to convert an array to an ordinary list with the same items.
Expected Output:
Original array:
array('b', [1, 2, 3, 4])
Array to list:
[1, 2, 3, 4]
"""


def h16(lst):
    from array import array
    array_num = array('i', lst)
    num_list = array_num.tolist()
    return num_list


"""
17. Write a Python program to convert an array to an array of machine values and return the bytes representation.
Expected Output:
Original array:
A1: array('i', [1, 2, 3, 4, 5, 6])
Array of bytes: b'010000000200000003000000040000000500000006000000'
"""


def h17(lst):
    import binascii
    from array import array
    x = array('i', lst)
    b = binascii.hexlify(x.tobytes())
    return b


"""
18. Write a Python program to read a string and interpreting the string as an array of machine values.
Expected Output:
array1: array('i', [7, 8, 9, 10])
Bytes: b'0700000008000000090000000a000000'
array2: array('i', [7, 8, 9, 10])
"""


def h18(lst):
    res = []
    from array import array
    import binascii
    array1 = array('i', lst)
    res.append('array1: {}'.format(array1))
    as_bytes = array1.tobytes()
    res.append('Bytes: {}'.format(binascii.hexlify(as_bytes)))
    array2 = array('i')
    array2.frombytes(as_bytes)
    res.append('array2: {}'.format(array2))
    return res


"""
19. Write a Python program to push three items into the heap and print the items from the heap.
Expected Output:
('V', 1)
('V', 2)
('V', 3)
"""


def h19(elements):
    import heapq
    heap = []
    for e in reversed(elements):
        heapq.heappush(heap, e)
    return heap


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


def h20(elements):
    import heapq
    heap = []
    for e in reversed(elements):
        heapq.heappush(heap, e)
    heapq.heappop(heap)
    return heap


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


def h21(elements):
    import heapq
    heap = []
    for e in reversed(elements):
        heapq.heappush(heap, e)
    heapq.heappushpop(heap, ('V', 6))
    return heap


"""
22. Write a Python program to create a heapsort, pushing all values onto a heap
and then popping off the smallest values one at a time.
Expected Output:
[10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
"""


def h22(h):
    import heapq
    heap = []
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for _ in range(len(heap))]


"""
23. Write a Python program to get the two largest and three smallest items
from a dataset.
Expected Output:
[100, 90]
[10, 20, 20]
"""


def h23(h):
    import heapq
    return heapq.nlargest(2, h), heapq.nsmallest(3, h)


"""
24. Write a Python program to locate the left insertion point for a
specified value in sorted order.
Expected Output:
4
2
"""


def h24(a, x):
    import bisect
    i = bisect.bisect_right(a, x)
    return i


"""
25. Write a Python program to locate the right insertion point for a
specified value in sorted order.
Expected Output:
3
2
"""


def h25(a, x):
    import bisect
    i = bisect.bisect_right(a, x)
    return i


"""
26. Write a Python program to insert items into a list in sorted order.
Expected Output:
Original List:
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
Sorted List:
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
"""


def h26(lst):
    import bisect
    sorted_list = []
    for i in lst:
        bisect.insort(sorted_list, i)
    return sorted_list


"""
27. Write a Python program to create a queue and display all the members and size
of the queue.
Expected Output:
Members of the queue:
0 1 2 3
Size of the queue:
4
"""


def h27(n):
    res = []
    import queue
    q = queue.Queue()
    for x in range(n):
        q.put(x)
    y = z = q.qsize()

    for n in list(q.queue):
        res.append(n)
    return res, q.qsize()


"""
28. Write a Python program to find whether a queue is empty or not.
Expected Output:
True
False
"""


def h28(n):
    import queue
    p = queue.Queue()
    q = queue.Queue()
    for x in range(n):
        q.put(x)
    return p.empty(), q.empty()


"""
29. Write a Python program to create a FIFO queue.
Expected Output:
0 1 2 3
"""


def h29(n):
    import queue
    res = []
    q = queue.Queue()
    for x in range(n):
        q.put(str(x))
    while not q.empty():
        res.append(q.get())
    return res


"""
30. Write a Python program to create a LIFO queue.
Expected Output:
3 2 1 0
"""


def h30(n):
    import queue
    res = []
    q = queue.LifoQueue()
    for x in range(n):
        q.put(str(x))
    while not q.empty():
        res.append(q.get())
    return res
