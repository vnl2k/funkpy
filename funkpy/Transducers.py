from functools import reduce
from typing import Callable, TypeVar, Union #, Generic

T = TypeVar('T') # generic type

class Accumulator:
  __slots__ = ['val']

  @staticmethod
  def of(value: T = None):
    return Accumulator(value)

  def __init__(self, value: T = None):
    self.val = value

  def getValue(self):
    return self.val



A = TypeVar(Accumulator)

# the step returns either an accumuklator A or transformed value T
Step = TypeVar(Callable[[A, T], Union[A, T]])

Reducer = TypeVar(Callable[[A, T], A])

def __map__(map_func: Callable[[T], T]) -> Callable[[Step], Reducer]:
  def f(step: Step) -> Reducer:
    return lambda a, i: step(a, map_func(i))

  return f

def __filter__(predicate_func) -> Callable[[Step], Reducer]:
  def f(step: Step) -> Reducer:
    return lambda a, i: step(a, i) if predicate_func(i) else a

  return f

def __compose__(*transducers):

  reversedTrns = list(transducers)
  reversedTrns.reverse()

  def f(shared_step: Step):
    return reduce(lambda step, t: t(step), reversedTrns, shared_step)

  return f

def __into__(r: Reducer, input, acc: A):
  return reduce(r, input, acc)

class exports:

  map = __map__

  filter = __filter__

  compose = __compose__

  into = __into__

