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

  reversedTrns = transducers.copy()
  reversedTrns.reverse()

  def f(shared_step: Step):
    l = list(map(lambda t: t(shared_step), reversedTrns))

  return f

def __into__():
  return None

class exports:

  map = __map__
  
  filter = __filter__

  compose = __compose__

  into = __into__

