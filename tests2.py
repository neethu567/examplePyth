class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lap1=self.laptop()
    def show(self):
        print(self.name,self.age)
        self.lap1.show()

    class laptop:
        def __init__(self):
            self.brand="hp"
            self.conf="i5"

        def show(self):
            print(self.brand,self.conf)

s1=student('neethu',23)
s1.show()
print(s1.name,s1.age)
# lap2=student.laptop()
# lap2.show()
