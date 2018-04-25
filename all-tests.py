import functional as _

print(_.array.concat())
print(_.array.concat([1]))
print(_.array.concat([1], 1))
print(_.array.concat(None, 1, 1))
print(_.array.concat([1,2,3], [1, 2, 3], [1, 2, 3]))


print(_.array.push([1], 2, 3, [1, 2, 3]))
