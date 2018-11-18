import timeit
import random



setup = 'from saddle_points import saddle_points'
cmd = 'saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'

print('original')
print(timeit.timeit(cmd, setup=setup))

setup = 'from saddle_points import saddle_points_v2'
cmd = 'saddle_points_v2([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'

print('v2')
print(timeit.timeit(cmd, setup=setup))

setup = 'from saddle_points import saddle_points_v3'
cmd = 'saddle_points_v3([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'

print('v3')
print(timeit.timeit(cmd, setup=setup))

# run original first
# original
# 4.171279536967631
# v2
# 4.895349195052404

# run v2 first
# v2
# 5.160853045003023
# original
# 4.217024507001042

matrix = str([[random.randint(1, 10) for _ in range(10)]
              for _ in range(10)])
setup = f'matrix={matrix}'
cmd = '''[[matrix[j][i] for j in range(len(matrix))]
for i in range(len(matrix[0]))]'''
print('matrix transpose')
print(timeit.timeit(cmd, setup=setup))
cmd = '[list(col) for col in zip(*matrix)]'
print('matrix transpose with zip')
print(timeit.timeit(cmd, setup=setup))


m = '''
[[9, 8, 7, 6, 8, 8, 1, 1, 1, 1],
 [5, 3, 2, 0, 8, 8, 1, 1, 1, 1],
 [5, 3, 2, 0, 8, 8, 1, 1, 1, 1],
 [6, 6, 7, 7, 7, 7, 1, 1, 1, 1],
 [6, 6, 7, 7, 8, 8, 1, 1, 1, 1],
 [6, 6, 7, 7, 8, 8, 1, 1, 1, 1],
 [6, 6, 7, 7, 8, 8, 1, 1, 1, 1],
 [6, 6, 7, 7, 8, 8, 1, 1, 1, 1],
 [6, 6, 7, 7, 8, 8, 1, 1, 1, 1],
 [6, 6, 7, 7, 8, 8, 1, 1, 1, 1],
])'''

setup = 'from saddle_points import saddle_points'
cmd = 'saddle_points('
cmd += m
print('10x10 matrix')
print(timeit.timeit(cmd, setup=setup))

setup = 'from saddle_points import saddle_points_v2'
cmd = 'saddle_points_v2('
cmd += m
print('10x10 matrix v2')
print(timeit.timeit(cmd, setup=setup))

setup = 'from saddle_points import saddle_points_v3'
cmd = 'saddle_points_v3('
cmd += m
print('10x10 matrix v3')
print(timeit.timeit(cmd, setup=setup))

# original
# 4.350348759035114
# v2
# 5.087190779973753
# v3
# 7.133009254001081
# 10x10 matrix
# 38.508683688996825
# 10x10 matrix v2
# 47.48531726497458
# 10x10 matrix v3
# 72.56647891900502

# v2
# 4.989308018004522
# original
# 4.278400840994436
# large matrix
# 37.96387248602696
# large matrix v2
# 46.24808180198306


# original
# 3.69518995285
# v2
# 4.98324584961
# large matrix
# 34.2091879845
# large matrix v2
# 44.9098410606


# 5 hours not completed
# m = str([[random.randint(1, 100) for _ in range(100)] for _ in range(100)])
# setup = 'from saddle_points import saddle_points'
# cmd = 'saddle_points('
# cmd += m
# cmd += ')'
# print('100x100 matrix')
# print(timeit.timeit(cmd, setup=setup))

# setup = 'from saddle_points import saddle_points_v2'
# cmd = 'saddle_points_v2('
# cmd += m
# cmd += ')'
# print('100x100 matrix v2')
# print(timeit.timeit(cmd, setup=setup))
