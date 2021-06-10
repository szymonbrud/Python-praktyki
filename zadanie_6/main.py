class MyFirstClass:

    def __init__(self):
        self.i = 0

    def sayI(abc):
        return abc.i

    def increaseI(self):
        self.i += 1


print('\n')
print("Class 1")

c1 = MyFirstClass()

print(c1.sayI())
c1.increaseI()
print(c1.sayI())


print('\n')
print("Class 2")

c2 = MyFirstClass()
print(c2.sayI())
