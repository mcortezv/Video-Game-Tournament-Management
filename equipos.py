import utilerias, jugadores
equipos = list()

def registrar() -> None:
    if len(jugadores.retornar_lista_jugadores()) <= 1:
        print("\n-------------------------------------------------------\nNo se Cuenta Con el Minimo de Jugadores Registrado para un Crear un Equipo")
    else:
        nombre_equipo = input("Ingrese el Nombre del Equipo: ")
        if validar_equipo_registrado(nombre_equipo) == True:
            print("\n-------------------------------------------------------\nEl Equipo ya se Encuentra Registrado")
        else:
            capitan = input("Ingrese el Apodo del Capitan: ")
            if jugadores.validar_jugador_registrado(capitan) == False:
                print("\n-------------------------------------------------------\nEl Capitan no se Encuentra en el Registro de Jugadores")
            else:
                apodo_miembros = input("Ingrese los Apodos de los Miembros Separados por Comas: ")
                miembros = [apodo.strip() for apodo in apodo_miembros.split(",")]
                if len(miembros) > 7:
                    print("\n-------------------------------------------------------\nEl Maximo de Integrantes por Equipo es de 8")
                else:
                    for miembro in miembros:
                        if miembro == capitan:
                            print("\n-------------------------------------------------------\nEl Capitan no Puede ser un Miembro del Equipo")
                        elif jugadores.validar_jugador_registrado(miembro) == False:
                                print("\n-------------------------------------------------------\nEl Jugador: {} no se Encuentra Registrado en la Lista de Jugadores".format(miembro))
                    else:
                        confirmar = ""
                        while confirmar.lower() not in ("s", "n"):
                            confirmar = input("\n-------------------------------------------------------\nConfirmar Registro (SI = S / NO = N): ").lower()
                            if confirmar == "n": 
                                print("\n-------------------------------------------------------\nRegistro de Equipo Cancelado")
                            elif confirmar == "s":
                                equipos.append({"nombre_equipo": nombre_equipo,
                                            "capitan": capitan,
                                            "miembros": miembros,
                                            "puntos": 0, 
                                            "victorias": 0, 
                                            "derrotas": 0})
                                print("\n-------------------------------------------------------\nSe ha Registrado al Equipo: {} y se ha Actualizado el Registro de Equipos: \n".format(nombre_equipo))
                                mostrar()
                                input("Enter para Continuar...")


def mostrar() -> None:
    if len(equipos) < 1:
        print("\n-------------------------------------------------------\nEl Registro de Equipos Esta Vacio")
    else:
        equipos_ordenados = sorted(equipos, key = lambda x: x["puntos"], reverse = True)
        print(f"\n--------------------------------------------------------------------------------\n{"Nombre Equipo":^20}|{"Capitan":^15}|\t{"Miembros"}\n--------------------------------------------------------------------------------\n")
        for equipo in equipos_ordenados:
            print(f"{equipo["nombre_equipo"]:^20}|{equipo["capitan"]:^15}|", end="\t")
            for miembro in equipo["miembros"]:
                    if equipo["miembros"] == 1:
                        print(miembro)
                    else: print("{}".format(miembro), end=", ")
            print("\n--------------------------------------------------------------------------------\n")
        print("Cantidad Total de Equipos Registrados: {}\n".format(len(equipos)))
    
    
def mostrar_equipo_especifico(nombre_equipo:str):
    for equipo in equipos:
        if equipo["nombre_equipo"] == nombre_equipo:
            print("\n----------------Miembros Actuales----------------------\nCapitan: {} \nMiembros: ".format(equipo["capitan"]), end="")
            for miembro in equipo["miembros"]:
                if equipo["miembros"] == 1:
                    print(miembro)
                else: print("{}".format(miembro), end=", ")
            return equipo


def actualizar() -> None:
    if len(equipos) < 1:
        print("\n-------------------------------------------------------\nNo se ha Registrado a Ningun Equipo") 
    else:
        nombre_equipo = input("Ingrese el Nombre del Equipo a Actualizar: ")
        if validar_equipo_registrado(nombre_equipo) == False:
            print("\n-------------------------------------------------------\nEl Equipo No se Encuentra Registrado")
        else:
            equipo = mostrar_equipo_especifico(nombre_equipo)
            opcion = ""
            while opcion not in ("1", "2"):
                opcion = input("\nQue Desea Hacer?: \n1. Agregar Miembro\n2. Eliminar Miembro\n")
                if opcion == "1":
                    nuevo_miembro = input("Ingrese el Apodo del Jugador a Agregar: ")
                    if jugadores.validar_jugador_registrado(nuevo_miembro) == False: 
                        print("\n-------------------------------------------------------\nEl Jugador No se Encuentra en el Registro de Jugadores")
                    elif nuevo_miembro == equipo["capitan"]: 
                        print("\n-------------------------------------------------------\nEl Jugador ya se Encuentra en el Equipo y es el Capitan")
                    elif validar_miembro_equipo_actual(equipo, nuevo_miembro) == True: 
                        print("\n-------------------------------------------------------\nEl Jugador ya se Encuentra en el Equipo, siendo Miembro")
                    else:
                        confirmar = ""
                        while confirmar.lower() not in ("s", "n"):
                            confirmar = input("\n-------------------------------------------------------\nConfirmar Registro (SI = S / NO = N): ").lower()
                            if confirmar == "s":
                                equipo["miembros"].append(nuevo_miembro)
                                print("\n-------------------------------------------------------\nSe ha Registrado al Jugador: {} en el Equipo: {} \n".format(nuevo_miembro, equipo["nombre_equipo"]))
                                mostrar()
                            elif confirmar == "n": 
                                print("\n-------------------------------------------------------\nActualizacion de Equipo Cancelada")
                elif opcion == "2": 
                    miembro_eliminar = input("Ingrese el Apodo del Jugador a Eliminar: ")
                    if jugadores.validar_jugador_registrado(miembro_eliminar) == False: 
                        print("\n-------------------------------------------------------\nEl Jugador No se Encuentra en el Registro de Jugadores")
                    elif validar_miembro_equipo_actual(equipo, miembro_eliminar) == False: 
                        print("\n-------------------------------------------------------\nEl Jugador no se Encuentra Registrado en el Equipo")
                    elif len(equipo["miembros"]) == 1:
                        print("\n-------------------------------------------------------\nNo se Puede Eliminar a Todos los Miembros de un Equipo")    
                    elif miembro_eliminar == equipo["capitan"]:
                        print("\n-------------------------------------------------------\nNo se Puede Eliminar al Capitan de un Equipo")
                    else:
                        confirmar = ""
                        while confirmar.lower() not in ("s", "n"):
                            confirmar = input("\n-------------------------------------------------------\nConfirmar Eliminacion (SI = S / NO = N): ").lower()
                            if confirmar == "s":
                                equipo["miembros"].remove(miembro_eliminar)
                                print("\n-------------------------------------------------------\nSe ha Eliminado al Jugador: {} del Equipo: {} \n".format(miembro_eliminar, equipo["nombre_equipo"]))
                                mostrar()
                                input("Enter para Continuar...")
                            elif confirmar == "n": 
                                print("\n-------------------------------------------------------\nEliminacion Cancelada")
                else:
                    print("\n-------------------------------------------------------\nOpcion no Valida, Ingrese una del 1 al 2")            


def eliminar() -> None:
    if len(equipos) < 1:
        print("\n-------------------------------------------------------\nNo se ha Registrado a Ningun Equipo")
    else:
        nombre_equipo = input("Ingrese el Nombre del Equipo a Eliminar: ")
        if validar_equipo_registrado(nombre_equipo) == False:
            print("\n-------------------------------------------------------\nEl Equipo No se Encuentra Registrado")
        else:
            equipo = mostrar_equipo_especifico(nombre_equipo)
            confirmar = ""
            while confirmar.lower() not in ("s", "n"):
                confirmar = input("\n-------------------------------------------------------\nConfirmar Eliminacion de Equipo (SI = S / NO = N): ").lower()
                if confirmar == "s":
                    del equipos[equipo]
                    print("Se ha Eliminado al Equipo {} y el Registro de Equipos ha Sido Actualizado\n".format(nombre_equipo))
                    mostrar()
                    input("Enter para Continuar...")
                elif confirmar == "n": print("\n-------------------------------------------------------\nEliminacion de Equipo Cancelada")
    
        
def validar_equipo_registrado(nombre_equipo:str) -> bool:
    for equipo in equipos:
        if equipo["nombre_equipo"] == nombre_equipo:
                return True
    return False


def retornar_datos_equipo(nombre_equipo:str) -> dict:
    for equipo in equipos:
        if equipo["nombre_equipo"] == nombre_equipo:
            return equipo


def validar_miembro_equipo_actual(equipo:dict, nuevo_miembro:str) -> bool:
    for miembro in equipo["miembros"]:
        if nuevo_miembro == miembro:
            return True
    return False

def retornar_lista_equipos():
    return equipos