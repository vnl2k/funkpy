def test_monads(m, ut):

  class tests(ut.TestCase):

    def test0_Functor(self):
      self.assertEqual(m.Functor.of(1), 1)
      self.assertEqual(m.Functor.of(1).map(lambda i: i+1), 2)

    def test1_either(self):
      self.assertEqual(m.Either.of(1).either(lambda i: i,lambda i: i), 1)

    
    def test2_either_Errorhandling(self):
      def f():
        try: 
          return 1/0
        # except ZeroDivisionError as ex:
        except Exception as ex:
          # return Exception(*ex.args)
          return ex
      self.assertEqual(m.Either.of(f()).either(lambda i: i,lambda i: i).args,('division by zero',))

   
    def test3_option(self):
      self.assertEqual(m.Option.of(1).maybe(0), 1)
      self.assertEqual(m.Option.of(None).maybe(0), 0)
      self.assertEqual(m.Option.of(10).map(lambda i: 1+i).maybe(None), 11)
      self.assertEqual(m.Option.of(10).maybe(), 10)

    def test4_monad_behavior(self):
      addOne = lambda i: m.Monad.of(i+1)
      self.assertEqual(m.Monad.of(1).flatMap(addOne) == m.Monad.of(2), True)
      self.assertEqual(m.Monad.of(1).flatMap(addOne).flatMap(addOne) == m.Monad.of(1).flatMap(lambda i: addOne(i).flatMap(addOne)), True)


    def test4a_option_behavior(self):
      addOne = lambda i: m.Option.of(i+1)
      self.assertEqual(m.Option.of(1).flatMap(addOne) == m.Option.of(2), True)
      self.assertEqual(m.Option.of(1).flatMap(addOne).flatMap(addOne) == m.Option.of(1).flatMap(lambda i: addOne(i).flatMap(addOne)), True)

  return tests