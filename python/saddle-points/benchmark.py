import timeit

setup = 'from saddle_points import saddle_points'
cmd = 'saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'

print(timeit.timeit(cmd, setup=setup, number=1000000))


# original timing commit [:f587b86]
# 4.6083211319637485
# 4.579655827023089
