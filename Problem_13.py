# Write a Python program that concatenates all elements in a list into a string and returns it.
mylist = [1, 2, 3, 4, "ABC", "RAJAN"]
var = ""
for a in mylist:
    if type(a) == str:
       var = var + a
    else:
        var = var + str(a)

print(var)
print(type(var))