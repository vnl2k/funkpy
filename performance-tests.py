import cProfile, pstats, io
import functools as ft
from functional import array as _

def profile_this(func, *args):
  pr = cProfile.Profile()
  pr.enable()
  func(*args)
  pr.disable()
  pstats.Stats(pr).strip_dirs().sort_stats('tottime').print_stats()

pr = cProfile.Profile()

profile_this(_.concat, [], range(1,100000,1))


# # Test 2
# pr = cProfile.Profile()
# pr.enable()
# _.concat(_.map(lambda i: i+1, range(1,100000,1)), range(1,100000,1))
# pr.disable()
# pstats.Stats(pr).strip_dirs().sort_stats('tottime').print_stats()

# pr = cProfile.Profile()
# pr.enable()
# func = lambda i: i + 1
# [func(i) for i in range(1, 10000, 1)]
# pr.disable()
# pstats.Stats(pr).strip_dirs().sort_stats('tottime').print_stats()



# s = io.StringIO()
# sortby = 'ncalls'
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())