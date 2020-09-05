def cDezTo(b,a):
    c=[]
    while a>=1:
        c.append(a%b)
        a=a//b
    return list(reversed(c))

def cBaseToDez(b,o):
	a=0
	for i in o: a=(a+i)*b
	return a//b

a=cDezTo(2,25)
a

b=cBaseToDez(2,a)
b

base=2
a=cDezTo(base,17009)
b=cBaseToDez(base,a)
[a,b]

(x)*base for x in a

