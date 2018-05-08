from pyfunctional2 import collection as _
from pyfunctional2.monads import Functor, Monad, Option, Either

l = [1, 2, 3]
# concatenate n lists
_.concat(l, [4, 5, 6], [7, 8, 9], 10) # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# append a list
_.push(l, [4, 5, 6]) # => [1, 2, 3, [4, 5, 6]]

addOne = _.curry(_.strictMap)(lambda i: i+1)
print(addOne([1, 2, 3])) # => [2, 3, 4]

addTwo = _.compose(addOne, addOne)
print(addTwo([1, 2, 3])) # => [3, 4, 5]



# How to construct this functor thing? 
Functor(5)
# OR
Functor.of(5)

# I love mapping functors
print(Functor.of("Start here").map(lambda i: i+" and keep walking!"))

# and some extra magic for free allows you to compare functors based 
# on the values they hold

print(Functor.of(5) == Functor.of(5)) # => True (fingers crossed) 



my_monad = Monad.of(5)
my_monad == Monad(5) # => True

# So far so good! How about something actually useful?
my_option = Option.of({"street": "Times Ave"}) \
	.map(lambda i: i.get("postcode")) \
	.maybe("postcode not found") # => "postcode not found
print(my_option)