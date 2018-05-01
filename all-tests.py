import unittest as ut

from functional import array as _
from functional import monads as M

# tests
from tests.monads import test_monads
from tests.array import test_array

# tests for functional.array
ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_array(_, ut)))

# tests for functional.monads
ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_monads(M, ut)))
