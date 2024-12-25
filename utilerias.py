
def pedir_dato(texto:str) -> str:
    while True:
        dato_entrada = input(texto)
        if dato_entrada.strip(): 
            return dato_entrada
        else: 
            print("-------------------------------------------------------\nEl Dato no Puede Estar Vacio, Ingreselo de Nuevo\n")


def pedir_numero_entero(texto:str) -> int:
    while True:
        try:
            dato_entrada = int(input(texto))
            return dato_entrada
        except ValueError:
            print("-------------------------------------------------------\nFase no Valida, Ingrese un número entero\n")


def validar_jugador(jugadores:list, apodo:str) -> bool:
    for jugador in jugadores:
        if jugador["apodo"] == apodo:
            return True
    return False


def validar_equipo(equipos:list, nombre_equipo:str) -> bool:
    for equipo in equipos:
        if equipo["nombre_equipo"] == nombre_equipo:
                return True
    return False


def validar_miembro_equipo_actual(equipo:dict, nuevo_miembro:str) -> bool:
    for miembro in equipo["miembros"]:
        if nuevo_miembro == miembro:
            return True
    return False


def validar_torneo(torneos_disponibles:list, nombre_torneo:str) -> bool:
    for torneo in torneos_disponibles:
        if torneo["datos"][0] == nombre_torneo:
            return True
    return False


def validar_estado_torneo(torneos_disponibles:list, nombre_torneo:str) -> str:
    for torneo in torneos_disponibles:
        if torneo["datos"][0] == nombre_torneo and torneo["estado"] == "Inscripción Abierta":
            estado = "Inscripción Abierta"
        elif torneo["datos"][0] == nombre_torneo and torneo["estado"] == "Cerrado":
            estado = "Cerrado"
        elif torneo["datos"][0] == nombre_torneo and torneo["estado"] == "En Curso":
            estado = "En Curso"
        elif torneo["datos"][0] == nombre_torneo and torneo["estado"] == "Finalizado":
            estado = "Finalizado"
    return estado


def validar_jugador_en_torneo(apodo:str, nombre_torneo:str, racing_inscritos:list, champions_inscritos:list, smash_inscritos:list) -> bool:
    if nombre_torneo == "Racing Rivals":
        for jugador in racing_inscritos:
            if jugador["apodo"] == apodo:
                return True
        return False
    elif nombre_torneo == "Champions Cup":
        for jugador in champions_inscritos:
            if jugador["apodo"] == apodo:
                return True
        return False
    elif nombre_torneo == "Smash Showdown":
        for jugador in smash_inscritos:
            if jugador["apodo"] == apodo:
                return True
        return False

  
def validar_registro_completado(nombre_torneo:str, fases:dict) -> bool:
    for fase in fases.values():
        if fase[0] == nombre_torneo:
            if fase[2] == True or fase[2] == None:
                return True
    return False
    
        
def validar_equipo_en_torneo(nombre_equipo:str, nombre_torneo:str, itson_inscritos:list, strike_inscritos:list) -> bool:
    if nombre_torneo == "ITSON Championship":
        for equipo in itson_inscritos:
            if equipo["nombre_equipo"] == nombre_equipo:
                return True
        return False
    elif nombre_torneo == "Strike Showdown":
        for equipo in strike_inscritos:
            if equipo["nombre_equipo"] == nombre_equipo:
                return True
        return False


def mostrar_equipos(equipos:list) -> None:
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


def mostrar_torneos_activos(torneos_disponibles:list) -> None:
    titulo = ["Nombre del Torneo", "Videojuego", "Tope de Jugadores"]
    print(f"\nTorneos Activos:\n-----------------------------------------------------------------------------------------\n{titulo[0]:^24}|{titulo[1]:^40}|{titulo[2]:^24}\n-----------------------------------------------------------------------------------------\n")
    for torneo in torneos_disponibles:
        if torneo["estado"] == "Inscripción Abierta":
            if torneo["datos"][3] == 10:
                texto = " Equipos"
            else: texto = " Jugadores"
            print(f"{torneo["datos"][0]:^24}|{torneo["datos"][1]:^40}|{torneo["datos"][3]:>8}{texto:<12}")
        else: continue
        print("\n-----------------------------------------------------------------------------------------\n")
                  

def retornar_datos_jugador(jugadores:list, apodo:str) -> dict:
    for jugador in jugadores:
        if jugador["apodo"] == apodo:
            return jugador
    
    
def retornar_datos_equipo(equipos:list, nombre_equipo:str) -> dict:
    for equipo in equipos:
        if equipo["nombre_equipo"] == nombre_equipo:
            return equipo





