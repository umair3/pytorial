list = [1,2,3]

print(list[0])

list = [1,2,3,"a"]
print(list[3])

list.append(3)
print(list.count(3))

list.reverse()
print(list)

#list.sort(), does not work due to presense of both str and int values
print(list)

print(list.index("a"))

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
