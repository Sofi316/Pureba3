import csv
lista=[]
def menu():
    print(".-.-.- M E N U .-.-.-")
    print("")
    print("1.- Agregar plan")
    print("2.- Listar planes")
    print("3.- Eliminar plan por ID")
    print("4.- Generar csv")
    print("5.- Cargar csv")
    print("6.- Estadisticas")
    print("0.- Salir")
    print("")
    
def validar(e): 
    while e<0 or e>100:
        print("El procentaje debe ser entre 0 y 100, ingrese nuevamente")
        e=int(input("Ingrese porcentaje de efectividad\n"))
def categoria():
    if porcentaje>=0 and porcentaje<=25:
        categoria="Chiste"
    elif porcentaje>=26 and porcentaje<=50:
        categoria="Anecdota"
    elif porcentaje>=51 and porcentaje<=75:
        categoria="Peligro"
    elif porcentaje>=76 and porcentaje<=99:
        categoria="Atención"
    else:
        categoria="Esclavitud"
    return categoria
   
while True:
    acum=0
    menu()
    op=int(input("Ingrese una opción\n"))
    if op==1:
        id=int(input("Ingrese la ID\n"))
        nombre=input("Ingrese nombre\n")
        porcentaje=int(input("Ingrese porcentaje de efectividad\n"))
        validar(porcentaje)
        cate=categoria()
        listap=[id,nombre,porcentaje,cate]
        lista.append(listap)
        print("Plan agregado exitosamente")
    elif op==2:
        if len(lista)!=0:
            for x in lista:
                print("ID", x[0],"Nombre", x[1], "Porcentaje",x[2],"Categoria",x[3])
        else:
            print("No se ha agregado plan")
    elif op==3:
        id=int(input("Ingrese ID a eliminar\n"))
        encontrado=False
        for x in lista:
            if id==int(x[0]):
                print("ID", x[0],"Nombre", x[1], "Porcentaje",x[2],"Categoria",x[3])
                encontrado=True
                break
        if encontrado==False:
            print("ID no encontrada")
        if encontrado==True:
            confirmar=input("¿Desea eliminar el plan?\n").lower()
            if confirmar=="si" or confirmar=="sí":
                lista.remove(x)
                print("Plan eliminado exitosamente")
            else:
                print("Se ha cancelado la eliminación")
    elif op==4:
        with open ('plan.csv','w',newline='') as planes:
            escritor=csv.writer(planes)
            escritor.writerow(['ID','Nombre','Porcentaje','Categoria'])
            escritor.writerows(lista)
            print("Archivo generado correctamente")
    elif op==5:
        lista.clear()
        cont=0
        with open ('plan.csv','r',newline='') as planes:
            lector=csv.reader(planes)
            for x in lector:
                if cont==0:
                    cont=cont+1
                    continue
                else:
                    id=int(x[0])
                    nom=x[1]
                    por=int(x[2])
                    cat=x[3]
                    nueva=[id,nom,por,cat]
                    lista.append(nueva)
            print("Archivo cargado exitosamente")
    elif op==6:
        mayor=-5
        if len(lista)!=0:
            for x in lista:
                acum=acum+int(x[2])
                if int(x[2])>mayor:
                    mayor=x[2]
            promedio=acum/len(lista)
            print(f"El promedio es {promedio}")
            print(f"El valor del porcentaje de efectividad más alto es {mayor}")
        else:
            print("No se han agregado planes")
    elif op==0:
        print("Adios!!")
        break
    else:
        print("Error, ingrese una opción valida")