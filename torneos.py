import jugadores, equipos, textwrap
TORNEO_INDIVIDUAL = 16 
TORNEO_EQUIPO = 8

torneos_disponibles = {
    "itson": {"nombre": "ITSON Championship", "juego": "League of Legends", "descripcion": "Equipos de cinco jugadores se enfrentarán en la Grieta del Invocador para demostrar sus habilidades estratégicas y de trabajo en equipo en este popular MOBA.", "tipo": "Equipos", "cantidad_participantes": TORNEO_EQUIPO, "estado": "Inscripcion Abierta"},
    "racing": {"nombre": "Racing Rivals", "juego": "Mario Kart", "descripcion": "Los estudiantes de ITSON competirán en divertidas y frenéticas carreras de Mario Kart, donde la velocidad y el uso inteligente de los ítems serán clave para la victoria.", "tipo": "Jugadores", "cantidad_participantes": TORNEO_INDIVIDUAL, "estado": "Inscripcion Abierta"},
    "strike": {"nombre": "Strike Showdown", "juego": "Counter-Strike: Global Offensive ", "descripcion": "Equipos de cinco jugadores se enfrentarán en intensos combates de disparos en primera persona para demostrar quién es el mejor en estrategia y puntería en ITSON.", "tipo": "Equipos", "cantidad_participantes": TORNEO_EQUIPO, "estado": "Inscripcion Abierta"},
    "champions": {"nombre": "Champions Cup", "juego": "FIFA", "descripcion": "Un torneo de fútbol virtual donde los mejores jugadores de FIFA de ITSON competirán por el título de campeón en emocionantes partidos llenos de goles y tácticas.", "tipo": "Jugadores", "cantidad_participantes": TORNEO_INDIVIDUAL, "estado": "Inscripcion Abierta"},
    "smash": {"nombre": "Smash Showdown", "juego": "Super Smash Bros. Ultimate", "descripcion": "Los mejores luchadores de ITSON se enfrentarán en intensos combates en el popular juego de lucha Super Smash Bros. Ultimate, donde solo uno saldrá victorioso entre la multitud de personajes icónicos.", "tipo": "Jugadores", "cantidad_participantes": TORNEO_INDIVIDUAL, "estado": "Inscripcion Abierta"}
}

registros = {"itson": {"inscritos": list(), "resultados": list()}, 
            "racing": {"inscritos": list(), "resultados": list()},
            "strike": {"inscritos": list(), "resultados": list()},
            "champions": {"inscritos": list(), "resultados": list()}, 
            "smash": {"inscritos": list(), "resultados": list()}
            }


def inscribir() -> None:
    if len(jugadores.retornar_lista_jugadores()) < 1:
        print("\n-------------------------------------------------------\nEl Registro de Jugadores Esta Vacio")
    else:
        mostrar_torneos_activos()
        nombre_torneo = input("Ingrese el Nombre del Torneo: ") 
        if validar_torneo_existente(nombre_torneo) == False:
            print("\n-------------------------------------------------------\nEl Nombre No Corresponde a Ningun Torneo Disponible")
        elif retornar_estado_torneo(nombre_torneo) != "Inscripcion Abierta":
                print("\n-------------------------------------------------------\nEl Torneo No se encuentra Disponible para Inscripcion")
        else:
            torneo = retornar_torneo(nombre_torneo)
            confirmar = ""
            if torneos_disponibles[torneo]["tipo"] == "Equipos":
                print("El Torneo: {} es de Equipos".format(nombre_torneo))
                nombre_equipo = input("Ingrese el Nombre del Equipo: ")
                if equipos.validar_equipo_registrado(nombre_equipo) == False:
                    print("\n-------------------------------------------------------\nEl Equipo No se Encuentra Registrado")
                elif validar_participante_en_torneo(nombre_equipo, torneo) == True:
                    print("\n-------------------------------------------------------\nEl Equipo Ya Se Encuentra Registrado en Este Torneo")
                else:   
                    while confirmar.lower() not in ("s", "n"):
                        confirmar = input("\n-------------------------------------------------------\nConfirmar Registro del Equipo: {} en el Torneo: {} (SI = S / NO = N): ".format(nombre_equipo, nombre_torneo)).lower()
                        if confirmar == "s":
                            equipo = equipos.retornar_datos_equipo(nombre_equipo)    
                            registros[torneo]["inscritos"].append(equipo)
                            registros[torneo]["resultados"].append(equipo)
                            if len(registros[torneo]["inscritos"]) == TORNEO_EQUIPO:
                                torneos_disponibles[torneo]["estado"] = "Cerrado"
                            jugadores.retornar_datos_jugador(equipo["capitan"])["torneos"].append(nombre_torneo)
                            for miembro in equipo["miembros"]:
                                 jugadores.retornar_datos_jugador(miembro)["torneos"].append(nombre_torneo)                     
                            mostrar_equipos_inscritos_torneo(torneo)
                            input("Enter para Continuar...")
                        elif confirmar == "n": print("\n-------------------------------------------------------\nRegistro Cancelado")
            elif torneos_disponibles[torneo]["tipo"] == "Jugadores":
                print("El Torneo: {} es Individual".format(nombre_torneo))
                apodo = input("Ingrese el Apodo del Jugador: ")
                if jugadores.validar_jugador_registrado(apodo) == False:
                    print("\n-------------------------------------------------------\nEl Jugador No se Encuentra Registrado")
                elif validar_participante_en_torneo(apodo, torneo) == True:
                    print("\n-------------------------------------------------------\nEl Jugador Ya Se Encuentra Registrado en Este Torneo")
                else:
                    while confirmar.lower() not in ("s", "n"):
                        confirmar = input("\n-------------------------------------------------------\nConfirmar Registro del Jugador: {} en el Torneo: {} (SI = S / NO = N): ".format(apodo, nombre_torneo)).lower()
                        if confirmar == "s":
                            jugador = jugadores.retornar_datos_jugador(apodo)
                            registros[torneo]["inscritos"].append(jugador)
                            registros[torneo]["resultados"].append(jugador)
                            if len(registros[torneo]["inscritos"]) == TORNEO_INDIVIDUAL:
                                torneos_disponibles[torneo]["estado"] = "Cerrado"
                            jugador["torneos"].append(nombre_torneo)
                            mostrar_jugadores_inscritos_torneo(torneo)
                            input("Enter para Continuar...")
                        elif confirmar == "n": print("\n-------------------------------------------------------\nRegistro Cancelado")
            preguntar = ""
            while preguntar.lower() not in ("s", "n"):
                preguntar = input("\n-------------------------------------------------------\n¿Desea Continuar Inscribiendo otro Jugador/Equipo en un Torneo? (SI = S / NO = N): ").lower()
                if preguntar == "s":
                    inscribir()
 
 
    
def mostrar_torneos_activos() -> None:
    print(f"\nTorneos Activos:\n-----------------------------------------------------------------------------------------\n{"Nombre del Torneo":^24}|{"Videojuego":^40}|{"Tope de Particpantes":^24}\n-----------------------------------------------------------------------------------------\n")
    for torneo in torneos_disponibles.values():
        if torneo["estado"] == "Inscripcion Abierta":
            print(f"{torneo["nombre"]:^24}|{torneo["juego"]:^40}|{(torneo["cantidad_participantes"]):>7}{" ":>1}{torneo["tipo"]:<12}")
        else: continue
        print("\n-----------------------------------------------------------------------------------------\n") 
    
        

def mostrar_torneos_disponibles() -> None:
    torneos_orden_alfabetico = sorted(torneos_disponibles, key=lambda x: x["datos"][0])
    titulo = ["Nombre del Torneo", "Videojuego", "Descripcion", "Tope de Jugadores", "Estado"]
    print(f"\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^24}|{titulo[1]:^24}|{titulo[2]:^80}|{titulo[3]:^22}|{titulo[4]:^30}\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    for tupla in torneos_orden_alfabetico:
        videojuego = textwrap.fill(tupla["datos"][1], width=20) 
        descripcion = textwrap.fill(tupla["datos"][2], width=76) 
        videojuego_dividido = videojuego.split("\n")
        descripcion_dividido = descripcion.split("\n")
        for i in range(max(len(videojuego_dividido), len(descripcion_dividido))):
            if i < len(videojuego_dividido):
                videojuego_formateado = videojuego_dividido[i]
            else:
                videojuego_formateado = ""
            if i < len(descripcion_dividido):
                descripcion_formateado = descripcion_dividido[i]
            else:
                    descripcion_formateado = ""
            if i == 0:
                print(f"{tupla["datos"][0]:^24}|{videojuego_formateado:^24}|{descripcion_formateado:^80}|{tupla["datos"][3]:^22}|{tupla["estado"]:^30}")
            else:
                print(f"{"":^24}|{videojuego_formateado:^24}|{descripcion_formateado:^80}|{"":^22}|{"":^30}")
        print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        input("Enter para Continuar...")
        
        
        
        
def mostrar_clasificacion(torneos_disponibles:list, itson_resultados:list, racing_resultados:list, strike_resultados:list, champions_resultados:list, smash_resultados:list) -> None:
    validacion = True
    while validacion == True:
        nombre_torneo = input("Ingrese el Nombre del Torneo: ")
        validar_torneo = modulo_utilerias.validar_torneo(torneos_disponibles, nombre_torneo)
        if validar_torneo == False:
            print("\n-------------------------------------------------------\nEl Nombre No Corresponde a Ningun Torneo Disponible")
        else:
            validar_estado_torneo = modulo_utilerias.validar_estado_torneo(torneos_disponibles, nombre_torneo)
            if validar_estado_torneo != "Finalizado":
                print("\n-------------------------------------------------------\nAun No se Puede Ver la Clasificacion de Este Torneo ya que se encuentra en Estado: {}".format(validar_estado_torneo))
            else:
                if nombre_torneo == "ITSON Championship" or nombre_torneo == "Strike Showdown":
                    mostrar_equipos_inscritos_torneo(nombre_torneo, itson_resultados, strike_resultados)
                elif nombre_torneo == "Champions Cup" or nombre_torneo == "Racing Rivals" or nombre_torneo == "Smash Showdown":
                    mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
        preguntar = ""
        while preguntar.lower() != "s" and preguntar.lower() != "n":
            preguntar = input("\n-------------------------------------------------------\n¿Desea Ver la Clasificacion de Otro Torneo? (SI = S / NO = N): ")
            if preguntar.lower() == "s":
                validacion = True
            elif preguntar.lower() == "n": validacion = False
            
            
            
            
def mostrar_jugadores_inscritos_torneo(torneo:str) -> None:
    if len(registros[torneo]["inscritos"]) < 1:
        print("\n-------------------------------------------------------\nNo se han Registrado Participantes en este Torneo")
    else:
        lista_ordenada = sorted(registros[torneo]["inscritos"], key = lambda x: x['puntos'], reverse = True)
        print("\nNombre del Torneo: {}".format(torneos_disponibles[torneo]["nombre"]))
        print(f"\n----------------------------------------------------------------------------------------------------------------------\n{"Nombre":^20}|{"Apodo":^20}|{"Carrera":^40}|{"Puntos":^10}|{"Victorias":^12}|{"Derrotas":^10}\n----------------------------------------------------------------------------------------------------------------------\n")
        for jugador in lista_ordenada:
            print(f"{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^40}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}")
            print("\n----------------------------------------------------------------------------------------------------------------------\n")
        print("Cantidad Total de Jugadores Registrados: {}".format(len(lista_ordenada)))

        
def mostrar_equipos_inscritos_torneo(torneo:str) -> None:
    if len(registros[torneo]["inscritos"]) < 1:
        print("\n-------------------------------------------------------\nNo se han Registrado Participantes en este Torneo")
    else:
        lista_ordenada = sorted(registros[torneo]["inscritos"], key = lambda x: x["puntos"], reverse = True)
        print("\nNombre del Torneo: {}".format(torneos_disponibles[torneo]["nombre"])) 
        print(f"\n----------------------------------------------------------------------------------------------------------------------\n{"Nombre Equipo":^20}|{"Capitan":^20}|{"Puntos":^10}|{"Victorias":^12}|{"Derrotas":^10}|\t{"Miembros":<40}\n----------------------------------------------------------------------------------------------------------------------\n")
        for equipo in lista_ordenada:
            print(f"{equipo["nombre_equipo"]:^20}|{equipo["capitan"]:^20}|{equipo["puntos"]:^10}|{equipo["victorias"]:^12}|{equipo["derrotas"]:^10}|", end="\t")
            for miembro in equipo["miembros"]:
                if len(equipo["miembros"]) == 1:
                    print(miembro)
                else: 
                    print("{}".format(miembro), end=", ")
            print("\n----------------------------------------------------------------------------------------------------------------------\n")
        print("Cantidad Total de Equipos Registrados: {}\n".format(len(lista_ordenada)))
            




def mostrar_top_torneo(torneos_disponibles:list, itson_resultados:list, racing_resultados:list, strike_resultados:list, champions_resultados:list, smash_resultados:list) -> None:
    validacion = True
    while validacion == True:
        nombre_torneo = input("Ingrese el Nombre del Torneo: ")
        validar_torneo = modulo_utilerias.validar_torneo(torneos_disponibles, nombre_torneo)
        if validar_torneo == False:
            print("\n-------------------------------------------------------\nEl Nombre No Corresponde a Ningun Torneo Disponible")
        else:
            validar_estado_torneo = modulo_utilerias.validar_estado_torneo(torneos_disponibles, nombre_torneo)
            if validar_estado_torneo != "Finalizado":
                print("\n-------------------------------------------------------\nAun No se Puede Ver la Clasificacion de Este Torneo ya que se encuentra en Estado: {}".format(validar_estado_torneo))
            else:
                if nombre_torneo == "ITSON Championship" or nombre_torneo == "Strike Showdown":
                    mostrar_top_equipos_torneo(nombre_torneo, itson_resultados, strike_resultados)
                    input("Enter para Continuar...")
                elif nombre_torneo == "Champions Cup" or nombre_torneo == "Racing Rivals" or nombre_torneo == "Smash Showdown":
                    mostrar_top_jugadores_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
                    input("Enter para Continuar...")
        preguntar = ""
        while preguntar.lower() != "s" and preguntar.lower() != "n":
            preguntar = input("\n-------------------------------------------------------\n¿Desea Ver la Clasificacion de Otro Torneo? (SI = S / NO = N): ")
            if preguntar.lower() == "s":
                validacion = True
            elif preguntar.lower() == "n": validacion = False




def mostrar_top_jugadores_torneo(nombre_torneo:str, racing_resultados:list, champions_resultados:list, smash_resultados:list) -> None:
    if nombre_torneo == "Champions Cup":
        if len(champions_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Champions Cup")
        else:
            torneo = sorted(champions_resultados, key = lambda x: x['puntos'], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre", "Apodo", "Carrera", "Puntos", "Victorias", "Derrotas"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^40}|{titulo[3]:^10}|{titulo[4]:^12}|{titulo[5]:^10}\n----------------------------------------------------------------------------------------------------------------------\n")
            for i, jugador in enumerate(torneo):
                if i < 3:
                    print(f"{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^40}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}")
                    print("\n----------------------------------------------------------------------------------------------------------------------\n")
    elif nombre_torneo == "Racing Rivals":
        if len(racing_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Racing Rivals")
        else:
            torneo = sorted(racing_resultados, key = lambda x: x['puntos'], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre", "Apodo", "Carrera", "Puntos", "Victorias", "Derrotas"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^40}|{titulo[3]:^10}|{titulo[4]:^12}|{titulo[5]:^10}\n----------------------------------------------------------------------------------------------------------------------\n")
            for i, jugador in enumerate(torneo):
                if i < 3:
                    print(f"{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^40}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}")
                    print("\n----------------------------------------------------------------------------------------------------------------------\n")
    elif nombre_torneo == "Smash Showdown":
        if len(smash_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Smash Showdown")
        else:
            torneo = sorted(smash_resultados, key=lambda x: x['puntos'], reverse=True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre", "Apodo", "Carrera", "Puntos", "Victorias", "Derrotas"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^40}|{titulo[3]:^10}|{titulo[4]:^12}|{titulo[5]:^10}\n----------------------------------------------------------------------------------------------------------------------\n")
            for i, jugador in enumerate(torneo):
                if i < 3:
                    print(f"{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^40}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}")
                    print("\n----------------------------------------------------------------------------------------------------------------------\n")
        
      
      
         
def mostrar_top_equipos_torneo(nombre_torneo:str, itson_resultados:list, strike_resultados:list) -> None:
    if nombre_torneo == "ITSON Championship":
        if len(itson_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo ITSON Championship")
        else:
            torneo = sorted(itson_resultados, key = lambda x: x["puntos"], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo)) 
            titulo = ["Nombre Equipo", "Capitan", "Puntos", "Victorias", "Derrotas", "Miembros"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^10}|{titulo[3]:^12}|{titulo[4]:^10}|\t{titulo[5]:<40}\n----------------------------------------------------------------------------------------------------------------------\n")
            for i, equipo in enumerate(torneo):
                if i < 3:
                    print(f"{equipo["nombre_equipo"]:^20}|{equipo["capitan"]:^20}|{equipo["puntos"]:^10}|{equipo["victorias"]:^12}|{equipo["derrotas"]:^10}|", end="\t")
                    for indice, miembro in enumerate(equipo["miembros"]):
                        if indice == len(equipo["miembros"]) - 1:
                            print(miembro)
                        else: print("{}".format(miembro), end=", ")
                    print("\n----------------------------------------------------------------------------------------------------------------------\n")
    elif nombre_torneo == "Strike Showdown":
        if len(strike_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Strike Showdown")
        else:
            torneo = sorted(strike_resultados, key = lambda x: x["puntos"], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre Equipo", "Capitan", "Puntos", "Victorias", "Derrotas", "Miembros"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^10}|{titulo[3]:^12}|{titulo[4]:^10}|\t{titulo[5]:<40}\n----------------------------------------------------------------------------------------------------------------------\n")
            for i, equipo in enumerate(torneo):
                if i < 3:
                    print(f"{equipo["nombre_equipo"]:^20}|{equipo["capitan"]:^20}|{equipo["puntos"]:^10}|{equipo["victorias"]:^12}|{equipo["derrotas"]:^10}|", end="\t")
                    for indice, miembro in enumerate(equipo["miembros"]):
                        if indice == len(equipo["miembros"]) - 1:
                            print(miembro)
                        else: print("{}".format(miembro), end=", ")
                    print("\n----------------------------------------------------------------------------------------------------------------------\n")
            
 
 
def validar_torneo_existente(nombre_torneo:str) -> bool:
    for torneo in torneos_disponibles.values():
        if torneo["nombre"] == nombre_torneo:
            return True
    return False
 
def retornar_estado_torneo(nombre_torneo:str) -> str:
    for torneo in torneos_disponibles.values():
        if torneo["nombre"] == nombre_torneo:
            return torneo["estado"]
  
  
def validar_participante_en_torneo(nombre_participante:str, torneo:str) -> bool:
    if torneos_disponibles[torneo]["tipo"] == "Equipos":
        for equipo in registros[torneo]["inscritos"]:
            if equipo["nombre_equipo"] == nombre_participante:
                return True
        return False
    elif torneos_disponibles[torneo]["tipo"] == "Jugadores":
        for jugador in registros[torneo]["inscritos"]:
            if jugador["apodo"] == nombre_participante:
                return True
        return False     
    

def retornar_torneo(nombre_torneo:str):
    for key, torneo in torneos_disponibles.items():
        if torneo["nombre"] == nombre_torneo:
            return key