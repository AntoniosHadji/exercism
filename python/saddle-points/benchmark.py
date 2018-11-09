import timeit


print(timeit.timeit('from saddle_points import saddle_points;saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])', number=1000000))
