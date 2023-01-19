def agrupar(a, b, c, x, y, z, equacion):
    if a*x + b*x + c*x + a*y + b*y + c*y + a*z + b*z * c*z == equacion:
        print(x*(a+b+c + y*(a+b+c) + z*(a+b+c)))
    elif a*x*y + b*x*y + c*x*y + a*y*z + b*y*z + c*y*z + a*z*x + b*z*x * c*z*x == equacion:
        print(x*y*(a+b+c + y*z*(a+b+c) + z*x*(a+b+c)))
    elif a*x*y + b*x*y + c*x*y + a*y + b*y + c*y + a*z + b*z * c*z == equacion:
        print(x*(a+b+c + y*(a+b+c)) + z*(a+b+c))
    elif a*x*z + b*x*z + c*x*z + a*y + b*y + c*y + a*z + b*z * c*z == equacion:
        print(x*(a+b+c + z*(a+b+c)) + y*(a+b+c))
    elif a*x + b*x + c*x + a*y*z + b*y*z + c*y*z + a*z + b*z * c*z == equacion:
        print(y*(a+b+c + z*(a+b+c)) + x*(a+b+c))
    elif a*x + b*x +c*x + a*y*x + b*y*x + c*y*x + a*z*x + b*z*x * c*z*x == equacion:
        print(x*(a+b+c + y*(a+b+c) + z*(a+b+c)))
    elif a*x*y + b*x*y + c*x*y + a*y + b*y + c*y + a*z*y + b*z*y * c*z*y == equacion:
        print(y*(a+b+c + x*(a+b+c) + z*(a+b+c)))
    elif a*x*z + b*x*z + c*x*z + a*y*z + b*y*z + c*y*z + a*z + b*z * c*z == equacion:
        print(z*(a+b+c + x*(a+b+c) + y*(a+b+c)))
    elif a*x*y*z + b*x*y*z + c*x*y*z + a*x*y*z + b*x*y*z + c*x*y*z + a*z + b*z * c*z == equacion:
        print(z*(a+b+c + x*y*(a+b+c)))
    elif a*x + b*x + c*x + a*x*y*z + b*x*y*z + c*x*y*z + a*x*y*z + b*x*y*z * c*x*y*z == equacion:
        print(x*(a+b+c + y*z*(a+b+c)))
    elif a*x*y*z + b*x*y*z + c*x*y*z + a*y + b*y + c*y + a*x*y*z + b*x*y*z * c*x*y*z == equacion:
        print(y*(a+b+c + x*z*(a+b+c)))
    elif a*x*y*z + b*x*y*z + c*x*y*z == equacion:
        print(x*y*z(a*b*c))
    else:
        print("no se puede agrupar")
a = int(input("introduzca el valor de a: "))
b = int(input("introduzca el valor de b: "))
c = int(input("introduzca el valor de c: "))
x = "x"
y = "y"
z = "z"
equacion = input("introduzca una ecuacion con 3 variables: ")
agrupar(a,b,c,x,y,z,equacion)
