import random
asesor=input("Ingrese el nombre de tienda: ")
cliente=input("ingrese el DNI del cliente: ")
monto_aprobado=0.0

risk=random.random()
print("el riesgo es: ", risk)

if risk >= 0.5:
    print("Lamentablemente no contamos con productos para usted en este momento")
salario=float(input("Ingrese el salario del cliente: "))
propiedades=input("cuenta con propiedades (S/N): ")

monto_propiedad=0.0
hasproperties=False

if propiedades.upper()=='S':
    hasproperties=True
    monto_propiedad=float(input("cual es la valuacion de la propiedad: "))
if risk<=0.3:
    if hasproperties:
        monto_aprobado=36*0.5*salario
    else: 
        pass
elif risk<=0.5:
    monto_aprobado=36*0.2*salario

print(f"el monto aprobado es {monto_aprobado} para el cliente DNI {cliente}")
