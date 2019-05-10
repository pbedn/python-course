import time
import datetime

"""
I. Datetime

1. Write a Python program to find the date of the first Monday of a given week.
Sample Year and week : 2015, 50
Expected Output : Mon Dec 14 00:00:00 2015
"""
arg = "2015 50"
expected = "Mon Dec 14 00:00:00 2015"


def datetime_1(s: str) -> str:
    date = datetime.datetime.strptime(s + " 1", "%Y %W %w")
    return date.strftime("%a %b %d %H:%M:%S %Y")


assert datetime_1(arg) == expected

"""
2. Write a Python program to select all the Sundays of a specified year.
"""
arg = 2016
expected = 53


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def datetime_2(year: int) -> int:
    sundays = []
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year + 1, 1, 1)
    for single_date in date_range(start_date, end_date):
        if single_date.isoweekday() == 6:
            sundays.append(single_date)
    # print(sundays)
    return len(sundays)


assert datetime_2(arg) == expected

"""
3. Write a Python program to add year(s) with a given date and display the new date.

Sample Data : (addYears is the user defined function name)
print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))
"""
arg = ((datetime.date(2015, 1, 1), -1),
       (datetime.date(2015, 1, 1), 0),
       (datetime.date(2015, 1, 1), 2),
       (datetime.date(2000, 2, 29), 1))
expected = (datetime.date(2014, 1, 1),
            datetime.date(2015, 1, 1),
            datetime.date(2017, 1, 1),
            datetime.date(2001, 3, 1))


def datetime_3(d: datetime.date, years: int) -> datetime.date:
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))


for i, test_input in enumerate(arg):
    assert datetime_3(*test_input) == expected[i]

"""
4. Write a Python script to display the various Date Time formats -
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
"""


def datetime_4() -> tuple:
    now = datetime.datetime.now()
    return (
        now.strftime("%Y-%M-%D %H:%M"),
        now.strftime("%Y"),
        now.strftime("%B"),
        now.strftime("%W"),
        now.strftime("%w"),
        now.strftime("%j"),
        now.strftime("%d"),
        now.strftime("%A"),
    )


"""
5. Write a Python program to convert a date to the timestamp.
"""
arg = datetime.date(2019, 1, 1)
expected = 1546297200.0


def datetime_5(d: datetime.date):
    return time.mktime(d.timetuple())


assert datetime_5(arg) == expected

"""
6. Write a Python program to convert a string date to the timestamp.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
7. Write a Python program to calculate a number of days between two dates.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
8. Write a Python program to calculate no of days between two datetimes.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
9. Write a Python program to display the date and time in a human-friendly string.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
10. Write a Python program to convert a date to Unix timestamp.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
11. Write a Python program to calculate two date difference in seconds
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
12. Write a Python program to subtract five days from current date.
Sample Date :
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
13. Write a Python program to convert unix timestamp string to readable date.
Sample Unix timestamp string : 1284105682
Expected Output : 2010-09-10 13:31:22
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
14. Write a Python program to print yesterday, today, tomorrow.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
15. Write a Python program to convert the date to datetime (midnight of the date) in Python.
Sample Output : 2015-06-22 00:00:00
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
16. Write a Python program to print next 5 days starting from today.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
17. Write a Python program to determine whether a given year is a leap year.
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
18. Write a Python program to convert a string to datetime.
Sample String : Jan 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
19. Write a Python program to get the current time in Python.
Sample Format :  13:19:49.078205
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
20. Write a Python program to add 5 seconds with the current time.
Sample Data :
13:28:32.953088
13:28:37.953088
"""
arg = "2019-01-01"
expected = 1546297260.0


def datetime_6(d: str):
    return time.mktime(time.strptime(d, "%Y-%M-%d"))


assert datetime_6(arg) == expected

"""
II. I/O
1. Write a Python program to write a list to a file.
"""


def io_1():
    with open('file', 'w') as fin:
        fin.write("{}".format([1, 2]))


"""
2. Write a Python program to copy the contents of a file to another file .
"""


def io_2():
    from shutil import copy
    copy('file', 'file2')


"""
3. Write a Python program to combine each line from first file
   with the corresponding line in second file.
"""


def io_3():
    with open('file', 'r') as file1:
        with open('file2', 'r') as file2:
            for line1, line2 in zip(file1, file2):
                if line1 == line2:
                    continue


"""
4. Write a Python program to read a random line from a file.
"""


def io_4():
    from random import choice
    return choice(open("file").readlines())


"""
5. Write a Python program to read an entire text file.
"""


def io_5():
    with open("file", 'r') as fin:
        fin.read()


"""
6. Write a Python program to read first n lines of a file.
"""


def io_6(n):
    with open("file", 'r') as fin:
        for _ in range(n):
            fin.readlines()


"""
7. Write a Python program to append text to a file and display the text.
"""


def io_7():
    text = "some text"
    with open("file", 'a') as fout:
        fout.write("\n{}".format(text))
    # print(text)


"""
8. Write a Python program to read last n lines of a file (strict)
"""


def io_8(lines):
    """Algorithm from
    https://stackoverflow.com/questions/136168/get-last-n-lines-of-a-file-with-python-similar-to-tail
    """
    BLOCK_SIZE = 1024

    with open("file", 'r') as fin:
        total_lines_wanted = lines

        fin.seek(0, 2)
        block_end_byte = fin.tell()
        lines_to_go = total_lines_wanted
        block_number = -1
        blocks = []  # blocks of size BLOCK_SIZE, in reverse order starting
        # from the end of the file
        while lines_to_go > 0 and block_end_byte > 0:
            if block_end_byte - BLOCK_SIZE > 0:
                # read the last block we haven't yet read
                fin.seek(block_number * BLOCK_SIZE, 2)
                blocks.append(fin.read(BLOCK_SIZE))
            else:
                # file too small, start from begining
                fin.seek(0, 0)
                # only read what was not read
                blocks.append(fin.read(block_end_byte))
            lines_found = blocks[-1].count('\n')
            lines_to_go -= lines_found
            block_end_byte -= BLOCK_SIZE
            block_number -= 1
        all_read_text = ''.join(reversed(blocks))
        return '\n'.join(all_read_text.splitlines()[-total_lines_wanted:])


"""
9. Write a Python program to read a file line by line and store it into a list.
"""


def io_9():
    lst = []
    with open("file", 'r') as fin:
        for line in fin:
            lst.append(line)
    return lst


"""
10. Write a Python program to read a file line by line store it into a variable.
"""


def io_10():
    with open("file", 'r') as fin:
        for line in fin:
            variable = line
    return variable


"""
11. Write a Python program to read a file line by line store it into an array.
"""


def io_11():
    lst = []
    with open("file", 'r') as fin:
        for line in fin:
            lst.append(line)
    return lst


"""
12. Write a python program to find the longest word.
"""


def io_12():
    biggest = ''
    with open("file", 'r') as fin:
        for line in fin:
            for word in line.split():
                if len(word) > len(biggest):
                    biggest = word
    return biggest


"""
13. Write a Python program to count the number of lines in a text file.
"""


def io_13():
    with open("file", 'r') as fin:
        return len(fin.readlines())


"""
14. Write a Python program to count the frequency of words in a file.
"""


def io_14():
    from collections import Counter
    with open("file", 'r') as fin:
        return Counter(fin.read().split())


"""
15. Write a Python program to get the file size of a plain file.
"""


def io_15():
    from os import stat
    return stat('file').st_size


"""
16. Write a Python program to assess if a file is closed or not.
"""


def io_16():
    with open("file", 'r') as fin:
        return "File is closed" if fin.closed else "File is open"


"""
17. Write a Python program to remove newline characters from a file.
"""


def io_17():
    with open("file", 'r') as fin:
        with open('file2', 'w') as fout:
            for line in fin:
                line = line.replace('\n', '')
                fout.write(line)


"""
III. Exceptions
"""

"""
1. Please raise a RuntimeError exception.
Hints: Use raise() to raise an exception.
"""


def exceptions_1():
    raise RuntimeError()


"""
2. Write a function to compute 5/0 and use try/except to catch the exceptions.
Hints: Use try/except to catch exceptions.
"""


def exceptions_2():
    try:
        return 5 / 0
    except ZeroDivisionError:
        pass


"""
3. Define a custom exception class which takes a string message as attribute.
Hints:
To define a custom exception, we need to define a class inherited from Exception.
"""


class CustomException(Exception):
    pass
