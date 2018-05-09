import re, math

from pyfunctional2.tools import compose, curry 
from pyfunctional2 import collection as _



class doc:

  def __init__(self, data=None):
    if data is not None: 
      self.val = data
    self.__compose__ = list()

  @staticmethod
  def of(data=None):
    return doc(data)

  def filter(self, func):
    return self.of(filter(func, self.val))

  def map(self, func):
    return self.of(map(func, self.val))
  
  def compose(self, arrFuncs):
    if  len(self.__compose__): self.__compose__.append(arrFuncs) 
    else: self.__compose__ = arrFuncs
    
    return self

  def composeMap(self, *funcs):
    return self.of(map(compose(*funcs), self.val))
  
  def apply(self, func):
    return self.of(func(self.val))

  def zip(self):
    return self.of(zip(*self.val))

  def reduce(self, func):
    return self.of(_.reduce(func,self.val))

  def value(self):
    return self.val

  def eval(self):
    return self.of(list(self.val))

  def foreach(self, func):
    for i in self.val: func(i)
    return self.of(None)
    
  def pick(self, keys):
    def dictGet(keys,dct):
      if isinstance(dct, dict):
        return {k: dct.get(k,None) for k in keys}
      else:
        return None
    
    return self.of(dictGet(keys,self.val))

  def pickRegex(self,arr):
    regF_arr = map(regTest,arr)

    def updateDct(d,i): d.update(i); return d

    def extract(dct):
      keys = dct.keys()
      keyArr = map(lambda regF: filter(regF,keys),regF_arr)
      CgetF = curry(getF)(dct);
      # the reduce call concatenates the multiple dictionaries produced by map()
      return _.reduce(updateDct, map(lambda ks: CgetF(ks) ,keyArr), {})

    return self.of(map(extract,self.val))

  def pickRegexToA(self,regex):
    regF = regTest(regex)
    
    def toArr(dct,k):
      val = dct.get(k, None)
      if isinstance(val, dict): val.update({'_name_': k})
      return val
    CtoArr = curry(toArr)(self.val);

    return self.of(
      map( CtoArr, filter(regF,self.val.keys()) )
    )
  
  def getField(self,key):

    def extract(dct):
      if isinstance(dct,dict): return dct.get(key, None)
      else: None

    if isinstance(self.val,dict):
      return self.of(extract(self.val))

    elif isinstance(self.val,list):
      return self.of(map(extract,self.val))

    else: return None

  def getFieldRegex(self,key):
    regF = regTest(key);

    def extract(dct):
      if isinstance(dct,dict): return map(lambda k: dct.get(k, None) , filter(regF,dct.keys()) )
      else: None

    if isinstance(self.val,dict):
      return self.of(extract(self.val))

    elif isinstance(self.val,list):
      return self.of(map(extract,self.val))

    else: return None




def regTest(reg):
  def test(str):
    return  re.compile(reg).findall(str).__len__()>0
  return test


def getF(dct,ks):
  return {k: dct.get(k, None) for k in ks}