import utilerias, jugadores

equipos = list()
jugadores = jugadores.retornar_lista_jugadores()


def registrar() -> None:
    if len(jugadores) > 1:
        nombre_equipo = input("Ingrese el Nombre del Equipo: ")
        validar_nombre_equipo = utilerias.validar_equipo(equipos, nombre_equipo)
        if validar_nombre_equipo == True:
            print("\n-------------------------------------------------------\nEl Equipo ya se Encuentra Registrado")
        else:
            capitan = input("Ingrese el Apodo del Capitan: ")
            validar_capitan = utilerias.validar_jugador(jugadores, capitan)
            if validar_capitan == False:
                print("\n-------------------------------------------------------\nEl Capitan no se Encuentra en el Registro de Jugadores")
            else:
                apodos = input("Ingrese los Apodos de los Miembros Separados por Comas: ")
                miembros = [apodo.strip() for apodo in apodos.split(',')]
                if len(miembros) > 7:
                    print("\n-------------------------------------------------------\nEl Maximo de Integrantes por Equipo es de 8")
                else:
                    for miembro in miembros:
                        if miembro == capitan:
                            print("\n-------------------------------------------------------\nEl Capitan no Puede ser un Miembro del Equipo")
                            break
                        else:
                            validar_miembro = utilerias.validar_jugador(jugadores, miembro)
                            if validar_miembro == False:
                                print("\n-------------------------------------------------------\nEl Jugador: {} no se Encuentra Registrado en la Lista de Jugadores".format(miembro))
                                break
                    else:
                        confirmar = ""
                        while confirmar.lower() != "s" and confirmar.lower() != "n":
                            confirmar = input("\n-------------------------------------------------------\nConfirmar Registro (SI = S / NO = N): ")
                            if confirmar.lower() == "s":
                                equipo = {"nombre_equipo": nombre_equipo,
                                            "capitan": capitan,
                                            "miembros": miembros,
                                            "puntos": 0, 
                                            "victorias": 0, 
                                            "derrotas": 0}
                                equipos.append(equipo)
                                print("\n-------------------------------------------------------\nSe ha Registrado al Equipo: {} y se ha Actualizado el Registro de Equipos: \n".format(nombre_equipo))
                                mostrar()
                                input("Enter para Continuar...")
                            elif confirmar.lower() == "n": print("\n-------------------------------------------------------\nRegistro de Equipo Cancelado")
    if len(jugadores) <= 1:
        print("\n-------------------------------------------------------\nNo se Cuenta Con el Minimo de Jugadores Registrado para un Crear un Equipo")


def mostrar() -> None:
    if len(equipos) > 0:
        equipos_ordenados = sorted(equipos, key = lambda x: x["puntos"], reverse = True)
        titulo = ["Nombre Equipo", "Capitan", "Miembros"]
        print(f"\n--------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^15}|\t{titulo[2]}\n--------------------------------------------------------------------------------\n")
        for i in range(len(equipos_ordenados)):
            print(f"{equipos_ordenados[i]["nombre_equipo"]:^20}|{equipos_ordenados[i]["capitan"]:^15}|", end="\t")
            for indice, miembro in enumerate(equipos_ordenados[i]["miembros"]):
                    if indice == len(equipos_ordenados[i]["miembros"]) - 1:
                        print(miembro)
                    else: print("{}".format(miembro), end=", ")
            print("\n--------------------------------------------------------------------------------\n")
        print("Cantidad Total de Equipos Registrados: {}\n".format(len(equipos_ordenados)))
    else:
        print("\n-------------------------------------------------------\nEl Registro de Equipos Esta Vacio")


def actualizar() -> None:
    if len(equipos) > 0:
        nombre_equipo = input("Ingrese el Nombre del Equipo a Actualizar: ")
        validar = utilerias.validar_equipo(equipos, nombre_equipo)
        if validar == False:
            print("\n-------------------------------------------------------\nEl Equipo No se Encuentra Registrado")
        else:
            for i, equipo in enumerate(equipos):
                if equipo["nombre_equipo"] == nombre_equipo:
                    capitan = equipo["capitan"]
                    print("\n----------------Miembros Actuales----------------------\nCapitan: {} \nMiembros: ".format(capitan), end="")
                    for i, miembro in enumerate(equipo["miembros"]):
                        if i == len(equipo["miembros"]) - 1:
                            print(miembro)
                        else: print("{}".format(miembro), end=", ")
                    preguntar = True
                    while preguntar == True:
                        opcion = input("""\nQue Desea Hacer?:
1. Agregar Miembro
2. Eliminar Miembro\n""")
                        if opcion == "1":
                            nuevo_miembro = input("Ingrese el Apodo del Jugador a Agregar: ")
                            validar_miembro_en_lista_de_jugadores = utilerias.validar_jugador(jugadores, nuevo_miembro)
                            validar_miembro_en_equipo_actual = utilerias.validar_miembro_equipo_actual(equipo, nuevo_miembro)
                            capitan = equipo["capitan"]
                            if validar_miembro_en_lista_de_jugadores == True and validar_miembro_en_equipo_actual == False and capitan != nuevo_miembro:
                                confirmar = ""
                                while confirmar.lower() != "s" and confirmar.lower() != "n":
                                    confirmar = input("\n-------------------------------------------------------\nConfirmar Registro (SI = S / NO = N): ")
                                    if confirmar.lower() == "s":
                                        equipo["miembros"].append(nuevo_miembro)
                                        print("\n-------------------------------------------------------\nSe ha Registrado al Jugador: {} en el Equipo: {} \n".format(nuevo_miembro, equipo["nombre_equipo"]))
                                        mostrar()
                                        preguntar = False
                                        break
                                    elif confirmar.lower() == "n": print("\n-------------------------------------------------------\nActualizacion de Equipo Cancelada")
                                    preguntar = False
                                    break
                            elif capitan == nuevo_miembro: 
                                print("\n-------------------------------------------------------\nEl Jugador ya se Encuentra en el Equipo y es el Capitan")
                                break
                            elif validar_miembro_en_lista_de_jugadores == False: 
                                print("\n-------------------------------------------------------\nEl Jugador No se Encuentra en el Registro de Jugadores")
                                break
                            else: 
                                print("\n-------------------------------------------------------\nEl Jugador ya se Encuentra en el Equipo, siendo Miembro")
                                break
                        elif opcion == "2": 
                            eliminar_miembro = input("Ingrese el Apodo del Jugador a Eliminar: ")
                            validar_miembro_en_lista_de_jugadores = utilerias.validar_jugador(jugadores, eliminar_miembro)
                            validar_miembro_en_equipo_actual = utilerias.validar_miembro_equipo_actual(equipo, eliminar_miembro)
                            capitan = equipo["capitan"]
                            if validar_miembro_en_lista_de_jugadores == True and validar_miembro_en_equipo_actual == True and capitan != eliminar_miembro and len(equipo["miembros"]) > 1:
                                confirmar = ""
                                while confirmar.lower() != "s" and confirmar.lower() != "n":
                                    confirmar = input("\n-------------------------------------------------------\nConfirmar Eliminacion (SI = S / NO = N): ")
                                    if confirmar.lower() == "s":
                                        equipo["miembros"].remove(eliminar_miembro)
                                        print("\n-------------------------------------------------------\nSe ha Eliminado al Jugador: {} del Equipo: {} \n".format(eliminar_miembro, equipo["nombre_equipo"]))
                                        mostrar()
                                        input("Enter para Continuar...")
                                        preguntar = False
                                        break
                                    elif confirmar.lower() == "n": 
                                        print("\n-------------------------------------------------------\nEliminacion Cancelada")
                                        preguntar = False
                                        break
                            elif len(equipo["miembros"]) == 1:
                                print("\n-------------------------------------------------------\nNo se Puede Eliminar a Todos los Miembros de un Equipo")
                                break    
                            elif capitan == eliminar_miembro:
                                print("\n-------------------------------------------------------\nNo se Puede Eliminar al Capitan de un Equipo")
                                break
                            elif validar_miembro_en_lista_de_jugadores == False: 
                                print("\n-------------------------------------------------------\nEl Jugadro No se Encuentra en el Registro de Jugadores")
                                break
                            else: 
                                print("\n-------------------------------------------------------\nEl Jugador no se Encuentra Registrado en el Equipo")
                                break
                        else:
                            print("\n-------------------------------------------------------\nOpcion no Valida, Ingrese una del 1 al 2")
                            continue
    elif len(equipos) == 0:
        print("\n-------------------------------------------------------\nNo se ha Registrado a Ningun Equipo")              


def eliminar() -> None:
    if len(equipos) > 0:
        nombre_equipo = input("Ingrese el Nombre del Equipo a Eliminar: ")
        validar = utilerias.validar_equipo(equipos, nombre_equipo)
        if validar == False:
            print("\n-------------------------------------------------------\nEl Equipo No se Encuentra Registrado")
        else:
            equipo_eliminar = 0
            for i, equipo in enumerate(equipos):
                if equipo["nombre_equipo"] == nombre_equipo:
                    equipo_eliminar = i
                    capitan = equipo["capitan"]
                    print("\n----------------Informacion del Equipo----------------------\nCapitan: {} \nMiembros: ".format(capitan), end="")
                    for indice, miembro in enumerate(equipo["miembros"]):
                        if indice == len(equipo["miembros"]) - 1:
                            print(miembro)
                        else: print("{}".format(miembro), end=", ")
            confirmar = ""
            while confirmar.lower() != "s" and confirmar.lower() != "n":
                confirmar = input("\n-------------------------------------------------------\nConfirmar Eliminacion de Equipo (SI = S / NO = N): ")
                if confirmar.lower() == "s":
                    del equipos[equipo_eliminar]
                    print("Se ha Eliminado al Equipo {} y el Registro de Equipos ha Sido Actualizado\n".format(nombre_equipo))
                    mostrar()
                    input("Enter para Continuar...")
                elif confirmar.lower() == "n": print("\n-------------------------------------------------------\nEliminacion de Equipo Cancelada")
    elif len(equipos) == 0:
        print("\n-------------------------------------------------------\nNo se ha Registrado a Ningun Equipo")