def test_collection(m, utils, ut):

  class tests(ut.TestCase):

    def test1_array_map(self):
      # List
      self.assertEqual(m.map(lambda i: i + 1, [1, 2, 3]), [2, 3, 4])
      self.assertEqual(m.map(lambda i, j: i + j, [1, 2, 3], [1, 2, 3]), [2, 4, 6])

      # Tuple
      self.assertEqual(m.map(lambda i: i + 1, (1, 2, 3)), (2, 3, 4))
      # the class of the first sequence determines the class of the returned sequence
      self.assertEqual(m.map(lambda i, j: i + j, (1, 2, 3), [1, 2, 3]), (2, 4, 6))

      # Set
      self.assertEqual(m.map(lambda i: i + 1, {1, 2, 3}), {2, 3, 4})
      self.assertEqual(m.map(lambda i, j: i + j, {1, 2, 3}, (1, 2, 3)), {2, 4, 6})

      # dict_keys
      d = {"a": 1, "b": 1}
      self.assertEqual(m.map(lambda i: d[i], d.keys()), [1, 1])

      # strings
      # self.assertEqual(m.map(lambda i: 'a', 'bb'), ['a', 'a'])
      self.assertEqual(m.map(lambda i: 'a', 'bb'), 'aa')
      # self.assertEqual(m.map(lambda i, j: i + j, 'bb', 'cc'), ['bc', 'bc'])
      self.assertEqual(m.map(lambda i, j: i + j, 'bb', 'cc'), 'bcbc')
      
      
    def test1a_array_strictMap(self):
      self.assertEqual(m.strictMap(lambda i: i + 1, [1, 2, 3]), [2, 3, 4])
      self.assertEqual(m.strictMap(lambda i: i + 1, (1, 2, 3)), (2, 3, 4))
      self.assertEqual(m.strictMap(lambda i: i + 1, {1, 2, 3}), {2, 3, 4})

    def test2_array_zip(self):

      # zip list
      self.assertEqual(m.zip([1, 2, 3]), [[1], [2], [3]])
      self.assertEqual(m.zip([1, 2, 3], [1, 2, 3]), [[1, 1], [2, 2], [3, 3]])
      self.assertEqual(m.zip(*[[1, 2, 3], [1, 2, 3]]), [[1, 1], [2, 2], [3, 3]])

      # zip tupel
      self.assertEqual(m.zip((1, 2, 3)), ((1,), (2,), (3,)))
      self.assertEqual(m.zip((1, 2, 3), (1, 2, 3)), ((1, 1), (2, 2), (3, 3)))

      # set
      self.assertEqual(m.zip({1, 2, 3}, ["1", "2", "3"]), [{1, "1"}, {2, "2"}, {3, "3"}])

      # string
      self.assertEqual(m.zip('aaa', 'bbb'), 'ababab')
      
      
    def test3_array_concat(self):
      # list
      self.assertEqual(m.concat(), [])
      self.assertEqual(m.concat([1]), [1])
      self.assertEqual(m.concat([1], 1), [1, 1])
      self.assertEqual(m.concat(None, 1, 1), [None, 1, 1])
      self.assertEqual(m.concat([1,2,3], [1, 2, 3], [1, 2, 3]), [1, 2, 3, 1, 2, 3, 1, 2, 3])

      # tuple 
      self.assertEqual(m.concat((1), (3)), [1, 3])
      self.assertEqual(m.concat((1, 2), (3, 4)), (1, 2, 3, 4))
      
      # set
      self.assertEqual(m.concat({1, 2}, {3, 4}), {1, 2, 3, 4})

    def test3a_flatten(self):
      self.assertEqual(m.flatten([[1,2,3], [1, 2, 3], [1, 2, 3]]), [1, 2, 3, 1, 2, 3, 1, 2, 3])

      # the first element of the sequence determines the final type
      self.assertEqual(m.flatten([(1,2,3), [1, 2, 3], [1, 2, 3]]), (1, 2, 3, 1, 2, 3, 1, 2, 3))

      # sets contain only unique elements
      self.assertEqual(m.flatten([{1,2,3}, [4, 5, 6], [1, 2, 3]]), {1, 2, 3, 4, 5, 6})

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
      addOne = utils.curry(m.strictMap)(lambda i: i+1)
      self.assertEqual(addOne([1, 2, 3]), [2, 3, 4])

      addTwo = utils.compose(addOne, addOne)
      self.assertEqual(addTwo([1, 2, 3]), [3, 4, 5])

      cmap = utils.curry(m.map)(lambda i: i + 1)
      self.assertEqual(cmap([1, 2, 3]), [2, 3, 4])


    def test8_filter(self):
      # list
      self.assertEqual(m.filter(lambda i: i>2, [1, 2, 3]), [3])
      
      # tuples
      self.assertEqual(m.filter(lambda i: i>2, (1, 2, 3)), (3, ))
      self.assertEqual(m.filter(lambda i: i>1, (1, 2, 3)), (2, 3))

    def test8_forEach(self):
      # list
      newList = []
      self.assertEqual(m.forEach(lambda i: newList.append(i + 1), [1, 2, 3]) or newList, [2, 3, 4])

    def test9_flatten(self):
      # list
      self.assertEqual(m.flatten([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])
  return tests
