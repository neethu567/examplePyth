class student:
    school="abcd"
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        self.name="nneethu"
        self.age=24
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    @classmethod
    def classmet(cls):
        print("hi")

print(student.classmet())
s1=student(10,20)
s2=student(14,56)
s1.age=44
s1.school="eeee"
print(s1.school)
print(s1.name)
print(s1.age)

s2.m1=22
s3=s1+s2
print(s1.m2)
print(s2.m1)
print(s3.m1)
print(s3.m2)


