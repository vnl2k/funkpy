import functools as ft

def test_transducers(trns, ut):

  shortList = [1, 2, 3]

  class tests(ut.TestCase):

    def test0_Map(self):

      addOne = trns.map(lambda i: i + 1)(lambda a, i: i)
      self.assertEqual(addOne(0, 1), 2)

      addOneAndSum = trns.map(lambda i: i + 1)(lambda a, i: a + i)
      self.assertEqual(ft.reduce(addOneAndSum, shortList, 0), 9)

    def test1_Filter(self):

      filterOne = trns.filter(lambda i: i > 1)(lambda a, i: a.append(i) or a)
      self.assertEqual(filterOne([], 1), [])
      self.assertEqual(filterOne([], 2), [2])

  return tests