import functools as ft

builtInMap = map
builtInZip = zip

def isIterable(value): 
  """Checks if the value implements iterator interface
  Arguments:
    value {any}
  Return:
    boolean
  """
  return hasattr(value, '__iter__')

def isSubscriptable(value): 
  """Checks if the value is subscriptable
  Arguments:
    value {any}
  Return:
    boolean
  """
  return hasattr(value, '__getitem__')

def isList(value):
  """Checks if the value is a list
  Arguments:
    value {list}
  Return:
    boolean
  """
  return isIterable(value) and isSubscriptable(value)

def zip(*args):
  """Zips arrays together. The arrays can be of the same length but it is not mandatory.
  Arguments:
    args {list}
  Returns:
    list
  """
  return map(list, builtInZip(*args))

def map(func, *arr):
  return list(builtInMap(func, *arr))

def reduce(func, agg, arr):
  return ft.reduce(func, arr, agg)

def concat(arr=None, *args):
  return ft.reduce(lambda agg, item: (agg.extend(item) if isList(item) else agg.append(item)) or agg, args, arr.copy() if (arr and isList(arr)) else [])

def push(arr=None, *args):
  return ft.reduce(lambda agg, item: agg.append(item) or agg, args, arr.copy() if (arr and isList(arr)) else [])
