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

    def test4_pickRegex(self):
      self.assertEqual(m.pickRegex(["a*"], {"aaa": 1, "bbb": 2, "ccc": 3}), {"aaa": 1})
      self.assertEqual(m.pickRegex(["aa*"], {"aaa": 1, "bbb": 2, "ccc": 3}), {"aaa": 1})
      self.assertEqual(m.pickRegex(["a*", "b*"], {"aaa": 1, "bbb": 2, "ccc": 3}), {"aaa": 1, "bbb": 2})

    def test5_get(self):
      self.assertEqual(m.get({"a": 1, "b": 2, "c": 3}, "a"), 1)
      self.assertEqual(m.get({"a": 1, "b": 2, "c": 3}, "f"), None)

    def test6_getValues(self):
      self.assertEqual(m.getValues({"a": 1, "b": 2, "c": 3}, ["a"]), [1])
      self.assertEqual(m.getValues({"a": 1, "b": 2, "c": 3}, ["a", "f"]), [1, None])

    def test7_update(self):
      self.assertEqual(m.update({"a": 1, "b": 2, "c": 3}, {"a": 100}), {"a": 100, "b": 2, "c": 3})

  return tests
