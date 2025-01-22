lista_invitados=["1213123","97797979","6314646464","74979797","97979797"]

edad=int(input("ingrese su edad: "))
dni=input("ingrese su dni: ")

if edad>=18 and dni in lista_invitados:
    print("Pase usted")