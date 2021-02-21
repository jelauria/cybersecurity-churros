x = True
y = False
if x is True:
    print("hello")
if (x):
    print("hello")
if y:
    print("false")
elif x is not y:
    print("whoops")
else:
    print("dang")
if x or y:
    print("boom")
print("lmao")
# note: false-y variables in python are 0, None, False, {} and []
# note: you can put parentheses wherever you want it

x = "hello"  # scoped within the whole script


def new_func(x, y="", z="bazz"):  # x is scoped local to the function
    print(x)
    print(y)
    print(z)

def lol_write():
    # clunky way of witing to a file
    file = open("file_path", 'w')
    file.write("hewwo woowrld")
    file.close()
    # non-clunky way
    with open("file_path", 'w') as file:
        file.write("hewwo wowwrld")

new_func("meow")
new_func("meow", z="woof")

def sec_func(x, y = "world"):
    return x + "hello", y + "world"

print(sec_func("womp "))
print(type(sec_func("womp"))) #returns a tuple

# String things
thing = "whaddup! my dude!!"
print(len(thing))
print(thing.startswith("wha"), thing.startswith("Wha"))
print(thing.find("dude"), thing.find("puddy"), thing.find("d"))
thing2 = "hello {name} my name is {animal}".format(animal = "dog", name = "reed")
print(thing2)

n = thing[0]
q = thing[2:10:2]
print(n, q)
z = thing.split(" ")
print(z, type(z))
g = " ".join(z)
print(g)
g = g.strip("!") # removes trailing !
print(g)

# bytes stuff
biite = b'thingy'
print(biite, type(biite))
now_str = biite.decode('utf-8')
print(now_str)
print(now_str.encode('utf-16'))
