"""
Profiling

Define function execution of which took a time e.g. 1 min.

Write profiling approaches using:

1. import time

2. import cProfile

3. from line_profiler import LineProfiler
"""


def function():
    for i in range(10**8):
        i += 1


def profile_with_time():
    import time

    start = time.time()
    function()
    end = time.time()

    print("Function profiling with time: {}".format(end - start))


def profile_with_cProfile():
    import cProfile

    cProfile.run('function()')


"""
How to run line_profiler
https://stackoverflow.com/questions/23885147/how-do-i-use-line-profiler-from-robert-kern
"""
from line_profiler import profile

@profile
def profile_with_line_profiler():
    function()


profile_with_time()
profile_with_cProfile()
profile_with_line_profiler()
