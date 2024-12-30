import utilerias
jugadores = list()

def registrar() -> None:
    apodo = utilerias.pedir_dato("Ingrese el Apodo del Jugador: ")
    if validar_jugador_registrado(apodo) == True:
        print("\n-------------------------------------------------------\nEl Jugador ya se Encuentra Registrado")
    else:
        id = utilerias.pedir_dato("Ingrese el ID del Jugador: ")
        nombre = utilerias.pedir_dato("Ingrese el Nombre Real del Jugador: ")
        carrera = utilerias.pedir_dato("Ingrese la Carrera del Jugador: ")
        confirmar = ""
        while confirmar.lower() not in ("s", "n"):
            confirmar = input("\n-------------------------------------------------------\nConfirmar Registro (SI = S / NO = N): ").lower()
            if confirmar == "n": 
                print("\n-------------------------------------------------------\nRegistro Cancelado")
            elif confirmar == "s":
                jugador = {"id": id,
                            "nombre": nombre,
                            "apodo": apodo,
                            "carrera": carrera,
                            "puntos": 0,
                            "victorias": 0,
                            "derrotas": 0,
                            "torneos": []}
                jugadores.append(jugador)
                print("\n-------------------------------------------------------\nSe ha Registrado al Jugador: {} y se ha Actualizado el Registro de Jugadores: \n".format(apodo))
                mostrar()
    
   
def mostrar() -> None:
    if len(jugadores) < 0:
        print("\n-------------------------------------------------------\nEl Registro de Jugadores Esta Vacio")
    else:
        jugadores_ordenados = sorted(jugadores, key = lambda x: x["puntos"], reverse = True)
        print(f"\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n{"ID":^10}|{"Nombre":^20}|{"Apodo":^20}|{"Carrera":^30}|{"Puntos":^10}|{"Victorias":^12}|{"Derrotas":^10}|\t{"Torneos Inscritos":<60}\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for jugador in jugadores_ordenados:
            if len(jugador["torneos"]) == 0:
                print(f"{jugador["id"]:^10}|{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^30}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}|\t{"Ninguno":<60}\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            else:
                print(f"{jugador["id"]:^10}|{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^30}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}|", end="\t")
                for torneo in jugador["torneos"]:
                    if len(torneo) == 1:
                        print(torneo)
                    else: print("{}".format(torneo), end=", ")
                print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print("Cantidad Total de Jugadores Registrados: {}\n".format(len(jugadores)))
        
        
def validar_jugador_registrado(apodo:str) -> bool:
    for jugador in jugadores:
        if jugador["apodo"] == apodo:
            return True
    return False


def retornar_datos_jugador(apodo:str) -> dict:
    for jugador in jugadores:
        if jugador["apodo"] == apodo:
            return jugador


def retornar_lista_jugadores() -> list:
    return jugadores