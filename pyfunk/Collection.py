import functools as ft
import builtins 
from pyfunk.utils import curry, compose

_zip = builtins.zip

def _filter(func, arr):
  return getattr(builtins, type(arr[0]).__name__)(builtins.filter(func, arr))

def _map(func, *arr): 
  return getattr(builtins, type(arr[0]).__name__)(builtins.map(func, *arr))

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

def zip(*args):
  """ Zips collections together. 

  The collections can be of different length.
  
  Arguments:
    args {list}
  Returns:
    list
  """
  return _map(list, _zip(*args))

def map(func, *arr):
  """ Applies a function on each element of the collection and returns a new collection.
  
  Arguments:
    func {function}
    *arr {tuple}    -- N arguments
  
  Returns:
    [type] -- [description]
  """
  return _map(func, *arr)

def strictMap(func, arr):
  """ Applies a function on each element of the collection and returns a new collection. 
  It is faster that collection.map

  Arguments:
    func {fucntion}
    arr {List}
  """
  return [func(i) for i in arr]

def forEach(func, *arr):
  """ Applies a function on each element of the collection
  
  Example
  
  Arguments:
    func {func} 
    *arr {tuple} -- one or many arguments
  """
  _map(func, *arr)

def reduce(func, arr, agg):
  return ft.reduce(func, arr, agg)

def concat(arr=None, *args):
  return ft.reduce(lambda agg, item: (agg.extend(item) if isIterable(item) else agg.append(item)) or agg, args, arr.copy() if (arr and isList(arr)) else [])

# def strictConcat(arr=None, *args):
#   return ft.reduce(lambda agg, item: agg.extend(item) or agg, args, arr.copy() if (arr and isList(arr)) else [])


def push(arr=None, *args):
  return ft.reduce(lambda agg, item: agg.append(item) or agg, args, arr.copy() if (arr and isList(arr)) else [])

def filter(func, arr):
  return _filter(func, arr)
