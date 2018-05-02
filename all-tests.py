import unittest as ut

from functional import collection as _
from functional import monads as M

# tests
from tests.monads import test_monads
from tests.collection import test_collection

# tests for functional.array
ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_collection(_, ut)))

# tests for functional.monads
ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_monads(M, ut)))
