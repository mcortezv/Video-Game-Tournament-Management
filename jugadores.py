import utilerias as modulo_utilerias

def registrar(jugadores:list) -> None:
    apodo = modulo_utilerias.pedir_dato("Ingrese el Apodo del Jugador: ")
    validar = modulo_utilerias.validar_jugador(jugadores, apodo)
    if validar == True:
        print("\n-------------------------------------------------------\nEl Jugador ya se Encuentra Registrado")
    else:
        puntos, victorias, derrotas, confirmar = 0, 0, 0, ""
        id = modulo_utilerias.pedir_dato("Ingrese el ID del Jugador: ")
        nombre = modulo_utilerias.pedir_dato("Ingrese el Nombre Real del Jugador: ")
        carrera = modulo_utilerias.pedir_dato("Ingrese la Carrera del Jugador: ")
        print("Puntos Iniciales del Jugador: {} \nNumero Inicial de Victorias: {} \nNumero Inicial de Derrotas: {}".format(puntos, victorias, derrotas))
        while confirmar.lower() != "s" and confirmar.lower() != "n":
            confirmar = input("\n-------------------------------------------------------\nConfirmar Registro (SI = S / NO = N): ")
            if confirmar.lower() == "s":
                jugador = {"id": id,
                            "nombre": nombre,
                            "apodo": apodo,
                            "carrera": carrera,
                            "puntos": puntos,
                            "victorias": victorias,
                            "derrotas": derrotas,
                            "torneos": []}
                jugadores.append(jugador)
                print("\n-------------------------------------------------------\nSe ha Registrado al Jugador: {} y se ha Actualizado el Registro de Jugadores: \n".format(apodo))
            elif confirmar.lower() == "n": print("\n-------------------------------------------------------\nRegistro Cancelado")
        mostrar(jugadores)
    
    
    
def mostrar(jugadores:list) -> None:
    if len(jugadores) > 0:
        jugadores_ordenados = sorted(jugadores, key = lambda x: x["puntos"], reverse = True)
        titulo = ["ID", "Nombre", "Apodo", "Carrera", "Puntos", "Victorias", "Derrotas", "Torneos Inscritos", "Ninguno"]
        print(f"\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^10}|{titulo[1]:^20}|{titulo[2]:^20}|{titulo[3]:^30}|{titulo[4]:^10}|{titulo[5]:^12}|{titulo[6]:^10}|\t{titulo[7]:<60}\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for i in range(len(jugadores_ordenados)):
            if len(jugadores_ordenados[i]["torneos"]) == 0:
                print(f"{jugadores_ordenados[i]["id"]:^10}|{jugadores_ordenados[i]["nombre"]:^20}|{jugadores_ordenados[i]["apodo"]:^20}|{jugadores_ordenados[i]["carrera"]:^30}|{jugadores_ordenados[i]["puntos"]:^10}|{jugadores_ordenados[i]["victorias"]:^12}|{jugadores_ordenados[i]["derrotas"]:^10}|\t{titulo[8]:<60}\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            else:
                print(f"{jugadores_ordenados[i]["id"]:^10}|{jugadores_ordenados[i]["nombre"]:^20}|{jugadores_ordenados[i]["apodo"]:^20}|{jugadores_ordenados[i]["carrera"]:^30}|{jugadores_ordenados[i]["puntos"]:^10}|{jugadores_ordenados[i]["victorias"]:^12}|{jugadores_ordenados[i]["derrotas"]:^10}|", end="\t")
                for indice, nombre_torneo in enumerate(jugadores_ordenados[i]["torneos"]):
                    if indice == len(jugadores_ordenados[i]["torneos"]) - 1:
                        print(nombre_torneo)
                    else: print("{}".format(nombre_torneo), end=", ")
                print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print("Cantidad Total de Jugadores Registrados: {}\n".format(len(jugadores_ordenados)))
    else:
        print("\n-------------------------------------------------------\nEl Registro de Jugadores Esta Vacio")