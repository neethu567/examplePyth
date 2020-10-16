class student:
    school="abcd"
    def __init__(self):
        self.name="neeth"
        self.age=26
    def update(self):
        self.name="anu"
    def update1(self,value):
        self.age=value
    @classmethod
    def schoolupdate(cls):
        cls.school="qwer"
        return cls.school
    @staticmethod
    def info():
        print("hi static")
s1=student()
s1.update()
print(s1.name,s1.age)
print(student.schoolupdate())
student.info()
s1.update1(23)
print(s1.age)
