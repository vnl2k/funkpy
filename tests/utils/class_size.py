import sys
from typing import Mapping, Any, Optional, Set

def get_class_size(obj: Mapping[str, Any], seen: Optional[Set] = None) -> int:
  """Recursively finds size of objects

  From https://goshippo.com/blog/measure-real-size-any-python-object/
  
  Important mark as seen *before* entering recursion to gracefully handle
  self-referential objects
  
  Arguments:
    obj {Mapping} -- can be any python object
  Keyword Arguments:
    seen {Set} -- a Set of methods to be excluded from the count (default: {None})
  
  Returns:
    int -- size of the object in bytes
  """
 
  size = sys.getsizeof(obj)
  if seen is None:
      seen = set()
  obj_id = id(obj)
  if obj_id in seen:
      return 0

 
  seen.add(obj_id)
  if isinstance(obj, dict):
    size += sum([get_class_size(v, seen) for v in obj.values()])
    size += sum([get_class_size(k, seen) for k in obj.keys()])
  elif hasattr(obj, '__dict__'):
    size += get_class_size(obj.__dict__, seen)
  elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
    size += sum([get_class_size(i, seen) for i in obj])
  return size

def dump(obj: Mapping[str, Any]):
  """Prints out all the methods of a given object
  
  From https://medium.com/@alexmaisiura/python-how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code-56be6443d524
  
  Arguments:
    obj {Mapping} -- can be any python object
  """
  
  for attr in dir(obj):
    print("  obj.%s = %r" % (attr, getattr(obj, attr)))