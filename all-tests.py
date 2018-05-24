import unittest as ut

from funkpy import Collection as _
from funkpy import Monads as M
from funkpy import Object

# tests
from tests.Monads import test_monads
from tests.Collection import test_collection
from tests.Object import test_item_functions

ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_collection(_, ut)))

ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_monads(M, ut)))

ut.TextTestRunner(verbosity=2).run(ut.TestLoader().loadTestsFromTestCase(test_item_functions(Object, ut)))
