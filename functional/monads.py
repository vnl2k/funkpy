class Monad:
  def __init__(self, value=None):
    self.val = value

  def __eq__(self, other):
    if isinstance(other, Monad):
      return self.val == other.val
    else:
      return self.val == other

  def __str__(self):
    return str(self.val)

  def flatMap(self, func):
    """ (F[A], A => F[B]) => F[B]

    Arguments:
      func {Function} -- A => F[B]

    Returns:
      F[B]
    """
    return func(self.val)
    


class Either(Monad):
  """[summary]
  
  [description]
  """

  @staticmethod
  def of(val):
    if isinstance(val, Exception) or val is None:
      return Either.Left(val)
    return Either([None, val])

  @staticmethod
  def pure(val):
    if isinstance(val, Exception) or val is None:
      return Either.Left(val)
    return Either([None, val])

  def map(self, f):
    if len(self.val) == 1:
      return self
    return self.of(f(self.val[1]))

  @staticmethod
  def Left(val):
    return Either([val])

  def either(self, left, right):
    if len(self.val) == 1:
      return left(self.val[0])
    else:
      return right(self.val[1])


class Option(Monad):

  def __init__(self, val=None):
    self.val = val

  Nothing = None
  """ Internal reference to empty element."""

  @staticmethod
  def of(val):
    """ Class constructor method.
    A => F[A]

    Arguments:
      val {A} -- any value type

    Returns:
      F[A] -- option of any value type
    """
    return Option(val)

  @staticmethod
  def pure(val):
    """ Same as Option.of method """
    return Option(val)

  def flatMap(self, func):
    """ (F[A], A => F[B]) => F[B]

    Arguments:
      func {Function} -- A => F[B]

    Returns:
      F[B]
    """
    return func(self.val)

  def map(self, func):
    """ (F[A], A => B) => F[B]

    Transforms the value inside the container

    Arguments:
      func {Function} -- Any function A => B

    Returns:
      F[B]
    """
    # return self if self.val == Option.Nothing else Option.of(func(self.val))
    return self if self.val == Option.Nothing else self.flatMap(lambda i: self.of(func(i)))

  def maybe(self, val2=None):
    """ Retuns eiher the value inside the container or val2"""
    return val2 if self.val == Option.Nothing else self.val
