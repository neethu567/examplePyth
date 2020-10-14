def add(x,y):
    return x+y
def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        raise ValueError("cant divide by 0")
    return x/y

add(2,3)
mul(3,4)
div(5,6)