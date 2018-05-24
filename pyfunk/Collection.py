import functools as ft
import builtins 
from pyfunk.utils import curry, compose

def _getClass(iterable):
  return getattr(builtins, type(iterable).__name__)

def _zip(*iterables):
  """Zips a tuple of iterables.
  
  Arguments:
    iterables {tuple} -- N arguments
  
  Yields:
    iterable
  """

  target_class = _getClass(iterables[0])
  sentinel = object()
  iterators = [iter(it) for it in iterables]

  while iterators:
    result = []
    for it in iterators:
      elem = next(it, sentinel)
      if elem is sentinel:
        return
      result.append(elem)

    yield target_class(result)

def _filter(func, iterable):
  return _getClass(iterable)(builtins.filter(func, iterable))

def _map(func, *iterables): 
  return _getClass(iterables[0])(builtins.map(func, *iterables))

def isIterable(value):
  """ Checks if the value implements iterator interface.

  Arguments:
    value {any}
  Return:
    boolean
  """
  return hasattr(value, '__iter__')

def isSubscriptable(value):
  """ Checks if the value is subscriptable.

  Arguments:
    value {any}
  Return:
    boolean
  """
  return hasattr(value, '__getitem__')

def isList(value):
  """ Checks if the value is a python list.

  Arguments:
    value {list}
  Return:
    boolean
  """
  return isIterable(value) and isSubscriptable(value)

def zip(*iterables):
  """ Zips collections together. 

  The collections can be of different length.

  Examples:
    # zip lists
    zip([1, 2, 3] # =>[[1], [2], [3]]
    zip([1, 2, 3], [1, 2, 3]) # => [[1, 1], [2, 2], [3, 3]]
    zip(*[[1, 2, 3], [1, 2, 3]]) # => [[1, 1], [2, 2], [3, 3]]

    # zip tupel
    zip((1, 2, 3)) # => ((1,), (2,), (3,))
    zip((1, 2, 3), (1, 2, 3)) # => ((1, 1), (2, 2), (3, 3))
  
  Arguments:
    iterables {tuple} -- N arguments
  Returns:
    collection
  """
  return _getClass(iterables[0])(_zip(*iterables))

def map(func, *iterables):
  """ Applies a function on each element of the collection and returns a new collection.
  
  Arguments:
    func      {function}
    iterables {tuple}    -- N arguments
  
  Returns:
    collection
  """
  return _map(func, *iterables)

def strictMap(func, iterable):
  """ Applies a function on each element of the collection and returns a new collection. 
  It is faster that collection.map

  Arguments:
    func     {fucntion}
    iterable {collection}

  Returns:
    collection
  """
  return _getClass(iterable)(func(i) for i in iterable)

def forEach(func, *iterables):
  """ Applies a function on each element of the collection.
  
  Examples:
    newList = []
    forEach(lambda i: newList.append(i + 1), [1, 2, 3]) or newList # => [2, 3, 4]
  
  Arguments:
    func      {func} 
    iterables {tuple} -- N arguments

  Returns:
    None
  """
  _map(func, *iterables)
  return None

def reduce(func, arr, agg):
  return ft.reduce(func, arr, agg)

def concat(arr=None, *args):
  return ft.reduce(lambda agg, item: (agg.extend(item) if isIterable(item) else agg.append(item)) or agg, args, arr.copy() if (arr and isList(arr)) else [])

def push(arr=None, *args):
  return ft.reduce(lambda agg, item: agg.append(item) or agg, args, arr.copy() if (arr and isList(arr)) else [])

def filter(func, arr):
  return _filter(func, arr)
