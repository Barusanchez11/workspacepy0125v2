#Realice un programa que busque alumnos por DNI

Alumnos=[
    {"nombre":"Juan",
     "dni":"71043589",
     "cursos":["Python","SQL","Java"]},
    {"nombre":"Pedro",
     "dni":"71043587",
     "cursos":["Python"]},
    {"nombre":"Diego",
     "dni":"71043588",
     "cursos":["Python","PowerBi","Java"]},
    {"nombre":"Mateo",
     "dni":"71043580",
     "cursos":["Python"]},
]

#agregar un alumno

nombre=input("Ingrese su nombre: ")
dni=input("ingrese su DNI: ")
curso=input("ingrese el curso a matricularse: ")

Alumnos.append(
    {"nombre":nombre,"dni":dni,"curso":curso}
)

print(Alumnos)