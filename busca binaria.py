import math

def f(x):
    y=5*x-5
    return y

a=float(input("Digite o limite esquerdo "))
b=float(input("Digite o limite direito "))

# comentario teste

tol=1e-6
ya=f(a)
yb=f(b)
c=(a+b)/2
yc=f(c)
cont=0


while math.fabs(b-a)>tol and math.fabs(yc)>tol:
    if ya*yc<0:
        b=c
        yb=yc
    else:
        a=c
        ya=yc
    c=(a+b)/2
    yc=f(c)
    cont =+ 1
print(f"A raiz é {c:.7f}.")


