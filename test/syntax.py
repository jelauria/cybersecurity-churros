# gather user input as type str and format it into a string
# animal = input("Enter your favorite animal: ")
# sound = input("What sound does that animal make? ")
# print("The {} says {}".format(animal, sound))

# get the type of any variable
# print(type(animal)) # class 'str'
x = 5
print(type(x)) # class 'int'

# variables can be set multiple at a time
a = 1
b = 2
c, d = 3, 4
c, d = d, c
print(a, b, c, d)

# multi-line strings
f = """
this
is
a
multiline string
"""

# escaping special characters
g = "backlashes to \"escape\" things"
print(g)

# python lists can hold anything that you want; you're not restricted to one type. Lists are also mutable
h = [1, 1.23, "hello"]
print(h)
h.append("world")
print(h)
h.remove(1.23)
print(h)
h.insert(6, "beep") # since 6 > len(h), it just gets tacked at the end
h.insert(2, "sheep")
print(h)
h2 = [7, 8, 9]
h.extend(h) # makes a copy of itself and appends it to the end of the original
h.extend(h2) #appends all of h2 to the end of h
print(h)
# note: python lists are 0-indexed
# note: you can access things with negative indexes; -1 being the last thing in the array

# range objects are literally a range of numbers. range(start, stop, step)
i = range(1, 100, 2)
j = list(i)
print(j) # prints out all odd numbers 1 thru 100

# slices grab certain sections of a list list[start:end:step] (start defaults to 0, step defaults to 1)
k = j[:3]
print(k) # prints 1, 3, 5

# dictionaries map keys to values and are mutable
l = {'key1':'v1', 'key2':["this", "is", 2]}
print(l)
print(l['key2']) #these two are
print(l.get('key2')) #equivalent statements
print(l.keys())
print(l.values())
m = l.get('key3') # None of type NoneType
print(m, type(m))
print('key1' in l) #prints true