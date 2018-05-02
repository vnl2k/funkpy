# PyFunctional
_PyFunctional_ is a small library which is trying to bring a few well-established concepts from functional programing to Python. The package was inspired by libraries like [lodash](https://lodash.com/) and [rambdajs](http://ramdajs.com/). The monads section is modeled after [Scala](https://www.scala-lang.org/) and influenced heavily by ["Scala with Cats"](https://underscore.io/books/scala-with-cats/)

One of the main drivers to start this library was the frustrating switch to generators/iterators in Python 3.x. They can incredibly powerful if one needs to efficiently process thousands of entries in list. They less convenient when the list has just 3 items. Hence, `functional.collection` was born. `collection` provides an implementation for side-effect free operations on lists, whereas most in-built list operations are anything but.

Functional programing is not complete without `curry` and `compose` methods available directly from `functional.tools` or `functional.collection`.

Last but not least are the glorious _functor_ and _monads_ from `functional.monads`, which many people are unfamiliar with.  

_PyFunctional_ is not an attempt to re-define Python itself. It provides just a skeleton for more functional way of writing code and that's it. Also the implementation here does not make any claims on performance. Whereas, there are no obvious problems, wrapping millions of values in a monad each may not be the right answer.

# Installation
Copy this repository locally and run `build.py`:
```bash
python3 build.py # to generates tar.gz file
pip3 install functional*
```
_Tested for Unix systems only._

# Examples

## Collection

```python
from functional import collection as _

l = [1, 2, 3]
# concatenate n lists
_.concat(l, [4, 5, 6], [7, 8, 9], 10) # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# append a list
_.push(l, [4, 5, 6]) # => [1, 2, 3, [4, 5, 6]]

# It's crazy to curry and compose!
addOne = _.curry(_.strict_map)(lambda i: i+1)
addOne([1, 2, 3]) # => [2, 3, 4]

addTwo = _.compose(addOne, addOne)
addTwo([1, 2, 3]) # => [3, 4, 5]
```

## Functor and Monads