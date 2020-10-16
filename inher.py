class a:
    def __init__(self):
        print("in a init")
    def acls(self):
        print("in class a")

class b(a):
    def __init__(self):
        super().__init__()
        print("in b init")
    def bcls(self):
        print("in class b")

class c(b):
    def ccls(self):
        print("in c class")

b1=b()
b1.bcls()
b1.acls()

