from functools import reduce
nums=[1,2,3,4,2,2,4,4,3,2,3,4]
even=list(filter(lambda n:n%2==0,nums))
print(even)
doubles=list(map(lambda a:a*2,even))
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)