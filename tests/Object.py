def test_item_functions(m, ut):

  class tests(ut.TestCase):

    def test1_apply(self):
      self.assertEqual(m.apply(lambda i: i+1, 1), 2)
      self.assertEqual(m.apply(lambda d: d.update({"a": 1}) or d, {}), {"a": 1})

    def test2_isGood(self):
      self.assertEqual(m.isGood(lambda i: 1 == 1, 1), True)
      self.assertEqual(m.isGood(lambda d: len(d.keys()) == 2, {"a": 1}), False)

    def test3_pick(self):
      self.assertEqual(m.pick(["a", "b"], {"a": 1, "b": 2, "c": 3}), {"a": 1, "b": 2})
  return tests
