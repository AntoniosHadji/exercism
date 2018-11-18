import cProfile
import io
import pstats
import random
from saddle_points import saddle_points
from saddle_points import saddle_points_v2

m = [[random.randint(1, 10) for _ in range(10)] for _ in range(10)]

pr = cProfile.Profile()
pr.enable()
# ... do something ...
saddle_points(m)
pr.disable()

s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

pr = cProfile.Profile()
pr.enable()
# ... do something ...
saddle_points_v2(m)
pr.disable()

s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
