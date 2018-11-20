import timeit
import random


def test(setup, cmd):
    repeat = 3
    precision = 3
    t = timeit.Timer(stmt=cmd, setup=setup)
    number, _ = t.autorange()
    r = t.repeat(repeat, number)
    best = min(r)
    units = {"usec": 1, "msec": 1e3, "sec": 1e6}
    print(f"{number:>7} loops,", end=' ')
    usec = best * 1e6 / number
    scales = [(scale, unit) for unit, scale in units.items()]
    scales.sort(reverse=True)
    # after break scale, time_unit retain values
    for scale, time_unit in scales:
        if usec >= scale:
            break

    print(f"best of {repeat}: {usec/scale:{precision+1}.{precision}g} {time_unit} per loop")  # noqa

def new_matrix(n):
    return str([[random.randint(1, n) for _ in range(n)] for _ in range(n)])


def run_test():
    size = [10, 50, 100, 200, 300]
    labels = ['v0', 'v1']
    for label in labels:
        print(f'testing {label}')
        setup = f'from first_attempts import saddle_points_{label} as saddle_points'  # noqa
        for n in size:
            m = new_matrix(n)
            print(f'{n:>3}', end=' ')
            cmd = f'saddle_points({m})'
            test(setup, cmd)


run_test()

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
