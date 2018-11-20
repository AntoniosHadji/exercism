import timeit
import random


def test(setup, cmd, label):
    t = timeit.Timer(stmt=cmd, setup=setup)
    r = []
    r.append(t.autorange())
    r.append(t.autorange())
    r.append(t.autorange())
    r = sorted(r, key=lambda x: x[1])[0]
    print(f'{label}: {r[0]} loops, {r[1]/r[0]} seconds per loop')


def new_matrix(n):
    return str([[random.randint(1, n) for _ in range(n)] for _ in range(n)])


def run_test(n):
    print(f'matrix size: {n}')
    m = new_matrix(n)
    setup = 'from saddle_points import saddle_points'
    cmd = f'saddle_points({m})'
    label = 'v0'
    test(setup, cmd, label)

    setup = 'from first_attempts import saddle_points_v1'
    cmd = f'saddle_points_v1({m})'
    label = 'v1'
    test(setup, cmd, label)

    setup = 'from first_attempts import saddle_points_v2'
    cmd = f'saddle_points_v2({m})'
    label = 'v2'
    test(setup, cmd, label)


run_test(10)
run_test(50)
run_test(100)
run_test(200)
run_test(300)


# test zip vs list comprenhension

# matrix = str([[random.randint(1, 10) for _ in range(10)]
#               for _ in range(10)])
# setup = f'matrix={matrix}'
# cmd = '''[[matrix[j][i] for j in range(len(matrix))]
# for i in range(len(matrix[0]))]'''
# print('matrix transpose')
# print(timeit.timeit(cmd, setup=setup))
# cmd = '[list(col) for col in zip(*matrix)]'
# print('matrix transpose with zip')
# print(timeit.timeit(cmd, setup=setup))
