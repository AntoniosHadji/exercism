import timeit

setup = 'from saddle_points import saddle_points'
cmd = 'saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'

print(timeit.timeit(cmd, setup=setup, number=1000000))


# original timing commit [:f587b86]
# 4.6083211319637485
# 4.579655827023089
# 4.576831965998281
# 4.633353625016753
# 4.324691342015285
# 4.491804242017679
# 4.489276387961581
