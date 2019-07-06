class Dog:
	dogInfo = "infoinfo"
	def __init__(self, name="", age=0, color):
		#constructor
		self.name = name
		self.age = age
		self.color = color

	def bark(self, str):
		print("BARK "+str)

mydog = Dog("aaa",11,"blue")
mydog.bark("meow")

mydog.name = "aaa"		#evem tho not defined in class
mydog.age = 16
print(mydog.name)

dog2 = Dog("bbb",22,"pink")
print(dog2.name)