name = "Julie"

age = 42

sentence = "Hi my name is {} and I am {} years old".format(name, age)

print(sentence)
# here is the comment
"""
long
comment
"""
if age > 18:
	print("I am so old")

def hello(mystr):
	print("hello world")
	print("here is {}".format(mystr))
	return "lalala"

str1 = hello("sss")
str2 = hello("yyy")

# list data structure
dognames = ["a", "b","c","d"]
dognames.insert(0,"yang")
del(dognames[2])
print(dognames)
print(len(dognames))

for dog in dognames:
	print(dog)	# add newline automatically

for dog in range(1,10):
	print(dog)

#Dictionary
dogs = {"a":1,"b":2,"c":3}
dogs["b"] = False		#type can be different
print(dogs["a"])
print(dogs)

