import functional as _
from functional.monads import Option

print(_.array.concat())
print(_.array.concat([1]))
print(_.array.concat([1], 1))
print(_.array.concat(None, 1, 1))
print(_.array.concat([1,2,3], [1, 2, 3], [1, 2, 3]))


print(_.array.push([1], 2, 3, [1, 2, 3]))



addOne = lambda i: Option.of(i+1)
print(Option.of(1).flatMap(addOne) == Option.of(2))
print(Option.of(1).flatMap(addOne).flatMap(addOne) == Option.of(1).flatMap(lambda i: addOne(i).flatMap(addOne)))

print(Option.of(2).map(lambda i: i+5))