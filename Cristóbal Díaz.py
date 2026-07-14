peliculas = {}
cartelera = {}
def leer_opcion():
    opcion = int
    print("\n========== MENÚ PRINCIPAL ==========\n1. Cupos por género\n2. Búsqueda de películas por rango de precio\n3. Actualizar precio de película\n4. Agregar película\n5. Eliminar película\n6. Salir\n=====================================\n")
    while opcion != 6:
        opcion = 0
        try:
            opcion = int(input("Ingrese la opción que desea realizar: "))
        except:
            print("Debe seleccionar una opción válida.\n")
        if opcion == 1:
            genero = str(input("Ingresar nombre de género para buscar cupos totales: ")).lower()
            cupos_genero(genero)
        elif opcion == 2:
            try:
                minimo = int(input("Ingrese precio mínimo: "))
                maximo = int(input("Ingrese precio máximo: "))
            except:
                print("Debe ingresar valores enteros.\n")
            busqueda_precio(minimo, maximo)
        elif opcion == 3:
            try:
                codigo = str(input("Ingrese el código de la película: ")).lower()
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                if validacion_duracion(nuevo_precio) == False:
                    print("Precio debe ser entero mayor que 0.\n")
                    return
            except:
                print("Precio debe ser entero mayor que 0.\n")
            actualizar_precio(codigo, nuevo_precio)
        elif opcion == 4:
            error = False
            codigo_repetido = False
            codigo = str(input("Ingresar código: ")).lower()
            titulo = str(input("Ingresar titulo: ")).lower()
            genero = str(input("Ingresar genero: ")).lower()
            duracion = input("Ingresar duración: ")
            clasificacion = str(input("Ingresar clasificación: ")).upper()
            idioma = str(input("Ingresar idioma: "))
            es_3d = str(input("¿Es 3d? (s/n): ")).lower()
            precio = input("Ingresar precio: ")
            cupos = input("Ingresar cupos: ")
            if buscar_codigo == True:
                error = True
                codigo_repetido = True
                print("Error al ingresar el código.")
            elif validacion_nombre(titulo) == False:
                error = True
                print("Error al ingresar el título.")
            elif validacion_nombre(genero) == False:
                error = True
                print("Error al ingresar el género.")
            elif validacion_duracion(duracion) == False:
                error = True
                print("Error al ingresar la duración.")
            elif validacion_clasificacion(clasificacion) == False:
                error = True
                print("Error al ingresar la clasificación.")
            elif validacion_nombre(idioma) == False:
                error = True
                print("Error al ingresar el idioma.")
            elif validacion_3d(es_3d) != True or validacion_3d(es_3d) != False:
                error = True
                print("Error al ingresar si es 3d.")
            elif validacion_duracion(precio) == False:
                error = True
                print("Error al ingresar el precio.")
            elif validacion_cupos(cupos) == False:
                error = True
                print("Error al ingresar los cupos.")
            if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos) == True:
                print("Película agregada.\n")
            else:
                print("El código ya existe.\n")
        elif opcion == 5:
            codigo = str(input("Ingrese el codigo de la película que desea borrar: "))
            if buscar_codigo(codigo) == True:
                eliminar_pelicula(codigo)
                if eliminar_pelicula(codigo) == True:
                    print("Película Eliminada.")
            else:
                print("Codigo no existe.\n")
        elif opcion == 6:
            print("Programa finalizado.")
def cupos_genero(genero):
    if validacion_nombre(genero) == False:
        print("No debe contener solo espacios en blanco ni estar vacío.\n")
        return
    cupos_totales = 0
    for i in peliculas:
        if peliculas[i][genero] == genero:
            suma_cupos = cartelera[i][cupos]
            cupos_totales += suma_cupos
    if cupos_totales == 0:
        print(f"No hay cupos disponibles para el género {genero}.")
    else:
        print(f"Quedan {cupos_totales} cupos totales para el género solicitado.")
def validacion_nombre(nombre):
    if len(nombre.strip()) == 0:
        return False
def validacion_duracion(duracion):
    if int(duracion) < 1:
        return False
def validacion_clasificacion(clasificacion):
    if clasificacion != "A" and clasificacion != "B" and clasificacion != "C":
        return False
def validacion_cupos(cupos):
    if int(cupos) < 0:
        return False
def validacion_3d(es_3d):
    if es_3d == "s":
        es_3d = True
        return True
    elif es_3d == "n":
        es_3d = False
        return False
    else:
        print("Error al ingresar el dato.\n")
        return
def busqueda_precio(p_min, p_max):
    peliculas_rango = []
    if p_min < 0 or p_min > p_max:
        print("Precio mínimo debe ser mayor o igual a 0 y menor que el precio máximo.\n")
        return
    if p_max < 0:
        print("Precio máximo debe ser mayor o igual a 0.\n")
        return
    for i in cartelera:
        if p_max > cartelera[i]["precio"] > p_min:
            if cartelera[i]["cupos"] > 0:
                peliculas_rango = [peliculas[i]["titulo"], peliculas[i]["codigo"]]
    if peliculas_rango:
        print(peliculas_rango.sort())
    else:
        print("No hay películas en ese rango de precios.\n")
def buscar_codigo(codigo):
    for i in peliculas:
        if peliculas[i]["codigo"] == codigo:
            return True
        return False
def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo) == True:
        peliculas[codigo]["precio"] = nuevo_precio
        print("Precio actualizado.\n")
    else:
        print("El código no existe.\n")
        return False
def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    if buscar_codigo(codigo) == True:
        return False
    nuevapelicula = {codigo: [titulo, genero, duracion, clasificacion, idioma, es_3d]}
    nuevacartelera = {codigo: [precio, cupos]}
    peliculas.update(nuevapelicula)
    cartelera.update(nuevacartelera)
    return True
def eliminar_pelicula(codigo):
    if buscar_codigo(codigo) == True:
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    else:
        return False
leer_opcion()