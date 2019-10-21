import timeit


def test(setup, cmd):
    repeat = 3
    precision = 3
    t = timeit.Timer(stmt=cmd, setup=setup)
    number, _ = t.autorange()
    r = t.repeat(repeat, number)
    best = min(r)
    units = {"usec": 1, "msec": 1e3, "sec": 1e6}
    print(f"{number:>7} loops,", end=" ")
    usec = best * 1e6 / number
    scales = [(scale, unit) for unit, scale in units.items()]
    scales.sort(reverse=True)
    # after break scale, time_unit retain values
    for scale, time_unit in scales:
        if usec >= scale:
            break

    print(
        f"best of {repeat}: {usec/scale:{precision+1}.{precision}g} {time_unit} per loop for {cmd}"
    )


setup = "import grains"
cmd = "grains.total(64)"
test(setup, cmd)

setup = "import bitshift"
cmd = "bitshift.total(64)"
test(setup, cmd)

setup = "import exponent"
cmd = "exponent.total(64)"
test(setup, cmd)

setup = "import pow"
cmd = "pow.total(64)"
test(setup, cmd)
