list_ = ["a", 0, False]
immutable_var = 1, 2, "Str", True, list_
print(immutable_var)

#изменить кортеж нельзя так как он является неизменяемым элементом,
#однако если в кортеж входит список то мы можем изменить элемент списка

list_.extend(["cocogoat"]) 
print(immutable_var)
immutable_var [4][1] = 200
print(immutable_var)

mutable_list = [1, 2, 3, "a", "d", "c", True]
print(mutable_list)
mutable_list [0] = 101
mutable_list [3] = "apple"
print(mutable_list)
