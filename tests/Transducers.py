from functools import reduce

def test_transducers(trns, ut):

  shortList = [1, 2, 3]

  class tests(ut.TestCase):

    def test0_Map(self):

      addOne = trns.map(lambda i: i + 1)(lambda a, i: i)
      self.assertEqual(addOne(0, 1), 2)

      addOneAndSum = trns.map(lambda i: i + 1)(lambda a, i: a + i)
      self.assertEqual(reduce(addOneAndSum, shortList, 0), 9)

    def test1_Filter(self):

      filterOne = trns.filter(lambda i: i > 1)(lambda a, i: a.append(i) or a)
      self.assertEqual(filterOne([], 1), [])
      self.assertEqual(filterOne([], 2), [2])

    def test2a_compose(self):
      addOne = trns.map(lambda i: i + 1)
      addTwo = trns.map(lambda i: i + 2)
      pipe = trns.compose(addOne, addTwo)(lambda agg, i: agg.append(i) or agg)

      self.assertEqual(reduce(pipe, [1, 2, 3], []), [4, 5, 6])

    def test2b_compose(self):
      addOne = trns.map(lambda i: i + 1)
      filterTwo = trns.filter(lambda i: i > 2)

      pipe1 = trns.compose(addOne, filterTwo)(lambda agg, i: agg.append(i) or agg)
      self.assertEqual(reduce(pipe1, [1, 2, 3], []), [3, 4])

      pipe2 = trns.compose(filterTwo, addOne)(lambda agg, i: agg.append(i) or agg)
      self.assertEqual(reduce(pipe2, [1, 2, 3], []), [4])
      self.assertEqual(trns.into(pipe2, [1, 2, 3], []), [4])

  return tests