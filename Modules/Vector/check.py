import vector2D
def func(x:int,v:str)->int:
	print (v*x)
	return 3
#print(func(5,"hello"))
v = vector2D.vector2D(3,4)
v2 = vector2D.vector2D(5,100)
print(v.length()+v2.length())
v = v+v2
print(v.length())