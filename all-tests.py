import unittest as ut

from pyfunk import Collection as _
from pyfunk import Monads as M
from pyfunk import Object

# tests
from tests.Monads import test_monads
from tests.Collection import test_collection
from tests.Object import test_item_functions

ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_collection(_, ut)))

ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_monads(M, ut)))

ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_item_functions(Object, ut)))
