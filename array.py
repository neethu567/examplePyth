from array  import*
vals=array('i',[2,3,4,5,7])
vals.reverse()
print(vals[3])
for e in vals:
    print(e)
newarray=array(vals.typecode(a for a in vals))
# newarr=array(vals.typecode(w for w in vals))
for e in newarray:
    print(e)
