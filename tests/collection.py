def test_collection(m, ut):

  class tests(ut.TestCase):

    def test1_array_map(self):
      self.assertEqual(m.map(lambda i: i + 1, [1, 2, 3]), [2, 3, 4])
      self.assertEqual(m.map(lambda i, j: i + j, [1, 2, 3], [1, 2, 3]), [2, 4, 6])

    def test1a_array_strictMap(self):
      self.assertEqual(m.strictMap(lambda i: i + 1, [1, 2, 3]), [2, 3, 4])

    def test2_array_zip(self):
      self.assertEqual(m.zip([1, 2, 3]), [[1], [2], [3]])
      self.assertEqual(m.zip([1, 2, 3], [1, 2, 3]), [[1, 1], [2, 2], [3, 3]])

    def test2a_array_zip(self):
      self.assertEqual(m.zip(*[[1, 2, 3], [1, 2, 3]]), [[1, 1], [2, 2], [3, 3]])

    def test3_array_concat(self):
      self.assertEqual(m.concat(), [])
      self.assertEqual(m.concat([1]), [1])
      self.assertEqual(m.concat([1], 1), [1, 1])
      self.assertEqual(m.concat(None, 1, 1), [1, 1])
      self.assertEqual(m.concat([1,2,3], [1, 2, 3], [1, 2, 3]), [1, 2, 3, 1, 2, 3, 1, 2, 3])

    # def test3a_array_strict_concat(self):
    #   self.assertEqual(m.strict_concat(), [])
    #   self.assertEqual(m.strict_concat([1]), [1])

    def test4_array_push(self):
      self.assertEqual(m.push([1], 2, 3, [1, 2, 3]), [1, 2, 3, [1, 2, 3]])

    def test5_array_reduce(self):
      # sum 
      self.assertEqual(m.reduce(lambda agg, i: agg+i, [1, 2, 3], 0), 6)

      # reduce to dictionary
      self.assertEqual(m.reduce(lambda agg, i: agg.update({i: i}) or agg, [1, 2, 3], {}), {1: 1, 2: 2, 3: 3})

    def test6_isSomething(self):
      self.assertEqual(m.isIterable([1]), True)
      self.assertEqual(m.isSubscriptable([1]), True)
      self.assertEqual(m.isList([1]), True)

      self.assertEqual(m.isSubscriptable(map(str, [1])), False)
      self.assertEqual(m.isList(map(str, [1])), False)
      self.assertEqual(m.isIterable(map(str, [1])), True)

    def test7_curry_compose(self):
      addOne = m.curry(m.strictMap)(lambda i: i+1)
      self.assertEqual(addOne([1, 2, 3]), [2, 3, 4])

      addTwo = m.compose(addOne, addOne)
      self.assertEqual(addTwo([1, 2, 3]), [3, 4, 5])

  return tests
