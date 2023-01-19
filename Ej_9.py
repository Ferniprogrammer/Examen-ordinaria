
def calculalunes(edad,):
    if edad <= 22:
     print("te quedan todos los lunes posibles")
    elif 22 < edad < 78:
        lunes = str((78*365-edad*365)/7)
        print("te quedan " + lunes + " lunes")
    else:
       print("ya no te qudan lunes") 
edad = int(input("introduzca su edad: "))
calculalunes(edad)
