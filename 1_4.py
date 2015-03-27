def foo():
    print "Hello World"
    
foo()
var = "comme"

def woo(x):
    print var,
    print x,
    
woo("ci,")
woo("ca.")
     
def factorial(y):
    prod = 1
    for i in range (1,y+1):
        prod=prod*i
    return prod

prod=factorial(5)
print prod


def eq():
    least=4
    for x in range (-20,21):
        y=x**2-4*x+4
        if y<least:
            least=y
            leastx=x
    return leastx
    
print eq()