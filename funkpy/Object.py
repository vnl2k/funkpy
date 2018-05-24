import re, math

from pyfunctional2.tools import compose, curry 
from pyfunctional2 import collection as _

def apply(func, item): 
  return func(item)

def isGood(func, item):
  return func(item) is True

def pick(keys, doc):
  """Picks the provided keys from the dictionary.
  
  Example
    pick(["a", "b"], {"a": 1, "b": 2, "c": 3}) # => {"a": 1, "b": 2}

  Arguments:
    keys {List}      -- list of key names which have to be an exact match
    doc  {Dictionary} 
  
  Returns:
    Dictionary
  """

  if not _.isIterable(keys):
    return None

  if not isinstance(doc, dict):
    return None

  return {k: doc.get(k, None) for k in keys}

def pickRegex(keys, doc):
  if not isinstance(doc, dict):
    return None

  regex_keys = _.map(regTest, keys)

  extract = lambda doc: pick(_.filter(regex_keys, doc.keys()), doc)

  return extract

def regTest(regex):

  def test(str):
    return  len(re.compile(regex).findall(str))>0

  return test


def get(doc, key):
  """Gets the value for key from the dictionary.
  
  Example
    get("a", {"a": 1, "b": 2, "c": 3}) # => 1

  Arguments:
    doc {Dictionary} 
    key {String}      -- key name
  
  Returns:
    Any or None
  """

  if not isinstance(doc, dict):
    return None

  if not isinstance(key, str):
    return None

  return doc.get(key, None)

def getValues(doc, keys):
  if not _.isIterable(keys):
    return None
  return _.map(lambda k: get(doc, k), keys)

def update(doc, new_doc):
  """ Updates a Dictionary without side-effects.
  
  Example
    dc = {"a": 1, "b": 2, "c": 3}
    newDC = update(dc, {"d": 4})
    newDC = update(newDC, ("e", 5)) # => {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    
  Arguments:
    doc    {Dictionary}
    newDoc {Dictionary}
  
  Returns:
    Dictionary
  """
  if not isinstance(doc, dict):
    return None

  d = doc.copy()
  return d.update(new_doc) or d



class Item:

  def __init__(self, data=None):
    if data != None: 
      self.val = data

  @staticmethod
  def of(data=None):
    return Item(data)

  def filter(self, func):
    return self.of(isGood(func, self.val))

  def map(self, func):
    return self.of(apply(func, self.val))
  
  def apply(self, func):
    return self.of(func(self.val))
  
  def pick(self, keys):
    return self.of(pick(keys, self.val))

  def pickRegex(self, keys):
    return self.of(pickRegex(keys, self.val))

  def get(self, key):
    return get(self.val, key)

  def getValues(self, keys):
    return getValues(self.val, keys)
