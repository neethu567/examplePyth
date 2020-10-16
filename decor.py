# def div(a,b):
#     print(a/b)
#
# def smartdiv(function):
#
#     def innerfun(a,b):
#         if a<b:
#             a,b=b,a
#         return function(a,b)
#
#     return innerfun
#
# div=smartdiv(div)
# div(2,4)

def div1(a,b):
    print(a/b)
def smartdiv(function):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return function(a,b)
    return inner

div1=smartdiv(div1)
div1(2,4)