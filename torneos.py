import jugadores, equipos, textwrap
TORNEO_INDIVIDUAL = 16 
TORNEO_EQUIPO = 8

torneos_disponibles = {
    "itson": {"nombre": "ITSON Championship", "juego": "League of Legends", "descripcion": "Equipos de cinco jugadores se enfrentarán en la Grieta del Invocador para demostrar sus habilidades estratégicas y de trabajo en equipo en este popular MOBA.", "tipo": "equipo", "cantidad_participantes": TORNEO_EQUIPO, "estado": "Inscripcion Abierta"},
    "racing": {"nombre": "Racing Rivals", "juego": "Mario Kart", "descripcion": "Los estudiantes de ITSON competirán en divertidas y frenéticas carreras de Mario Kart, donde la velocidad y el uso inteligente de los ítems serán clave para la victoria.", "tipo": "individual", "cantidad_participantes": TORNEO_INDIVIDUAL, "estado": "Inscripcion Abierta"},
    "strike": {"nombre": "Strike Showdown", "juego": "Counter-Strike: Global Offensive ", "descripcion": "Equipos de cinco jugadores se enfrentarán en intensos combates de disparos en primera persona para demostrar quién es el mejor en estrategia y puntería en ITSON.", "tipo": "equipo", "cantidad_participantes": TORNEO_EQUIPO, "estado": "Inscripcion Abierta"},
    "champions": {"nombre": "Champions Cup", "juego": "FIFA", "descripcion": "Un torneo de fútbol virtual donde los mejores jugadores de FIFA de ITSON competirán por el título de campeón en emocionantes partidos llenos de goles y tácticas.", "tipo": "individual", "cantidad_participantes": TORNEO_INDIVIDUAL, "estado": "Inscripcion Abierta"},
    "smash": {"nombre": "Smash Showdown", "juego": "Super Smash Bros. Ultimate", "descripcion": "Los mejores luchadores de ITSON se enfrentarán en intensos combates en el popular juego de lucha Super Smash Bros. Ultimate, donde solo uno saldrá victorioso entre la multitud de personajes icónicos.", "tipo": "individual", "cantidad_participantes": TORNEO_INDIVIDUAL, "estado": "Inscripcion Abierta"}
}

inscritos = {"itson": list(), "racing": list(), "strike": list(), "champions": list(), "smash": list()}
resultados = {"itson": list(), "racing": list(), "strike": list(), "champions": list(), "smash": list()}


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
            if torneo["tipo"] == "equipo":
                print("El Torneo: {} es de Equipos".format(nombre_torneo))
                nombre_equipo = input("Ingrese el Nombre del Equipo: ")
                if equipos.validar_equipo_registrado(nombre_equipo) == False:
                    print("\n-------------------------------------------------------\nEl Equipo No se Encuentra Registrado")
                elif validar_equipo_en_torneo(nombre_equipo, nombre_torneo) == True:
                    print("\n-------------------------------------------------------\nEl Equipo Ya Se Encuentra Registrado en Este Torneo")
                else:   
                    confirmar = ""
                    while confirmar.lower() not in ("s", "n"):
                        confirmar = input("\n-------------------------------------------------------\nConfirmar Registro del Equipo: {} en el Torneo: {} (SI = S / NO = N): ".format(nombre_equipo, nombre_torneo)).lower()
                        if confirmar == "s":
                            
                            equipo = equipos.retornar_datos_equipo(nombre_equipo)
                            capitan = equipo["capitan"]
                            miembros = equipo["miembros"]
                                                
                            for inscrito in inscritos:
                                if inscrito.get("key") == torneo.get(("key")):
                                    inscrito.append(equipo)
                                    print(inscrito)
                    
                                                
                                                        
            #                                     if nombre_torneo == "ITSON Championship":
            #                                         itson_inscritos.append(equipos[indice])
            #                                         itson_resultados.append(equipos[indice])
            #                                         print(itson_inscritos)
            #                                         for jugador in jugadores:
            #                                             if jugador["apodo"] == capitan:
            #                                                 jugador["torneos"].append(nombre_torneo)
            #                                         for miembro in miembros:
            #                                             for jugador in jugadores:
            #                                                 if jugador["apodo"] == miembro:
            #                                                     jugador["torneos"].append(nombre_torneo)
            #                                         if len(itson_inscritos) == TORNEO_EQUIPO:
            #                                             for torneo in torneos_disponibles:
            #                                                 if torneo["datos"][0] == nombre_torneo:
            #                                                     torneo["estado"] = "Cerrado"
                                                                
                                                                
                                                                
            #                                     elif nombre_torneo == "Strike Showdown":
            #                                         strike_inscritos.append(equipos[indice])
            #                                         strike_resultados.append(equipos[indice])
            #                                         print(strike_inscritos)
            #                                         for jugador in jugadores:
            #                                             if jugador["apodo"] == capitan:
            #                                                 jugador["torneos"].append(nombre_torneo)
            #                                         for miembro in miembros:
            #                                             for jugador in jugadores:
            #                                                 if jugador["apodo"] == miembro:
            #                                                     jugador["torneos"].append(nombre_torneo)
            #                                         if len(strike_inscritos) == TORNEO_EQUIPO:
            #                                             for torneo in torneos_disponibles:
            #                                                 if torneo["datos"][0] == nombre_torneo:
            #                                                     torneo["estado"] = "Cerrado"
                                                                
                                                                
                                                                
                                                                
                                                                
            #                                     mostrar_equipos_inscritos_torneo(nombre_torneo, itson_inscritos, strike_inscritos)
            #                                     input("Enter para Continuar...")
            #                                 elif confirmar.lower() == "n": print("\n-------------------------------------------------------\nRegistro Cancelado")
            #                 else:
            #                     print("El Torneo: {} es Individual".format(nombre_torneo))
            #                     apodo = input("Ingrese el Apodo del Jugador: ")
            #                     validar_jugador_en_torneo = modulo_utilerias.validar_jugador_en_torneo(apodo, nombre_torneo, racing_inscritos, champions_inscritos, smash_inscritos)
            #                     if validar_jugador_en_torneo == True:
            #                         print("\n-------------------------------------------------------\nEl Jugador Ya Se Encuentra Registrado en Este Torneo")
            #                     else:
            #                         validar_jugador_en_registro = modulo_utilerias.validar_jugador(jugadores, apodo)
            #                         if validar_jugador_en_registro == False:
            #                             print("\n-------------------------------------------------------\nEl Jugador No se Encuentra Registrado")
            #                         else:
            #                             while confirmar.lower() != "s" and confirmar.lower() != "n":
            #                                 confirmar = input("\n-------------------------------------------------------\nConfirmar Registro del Jugador: {} en el Torneo: {} (SI = S / NO = N): ".format(apodo, nombre_torneo))
            #                                 if confirmar.lower() == "s":
            #                                     for i, jugador in enumerate(jugadores):
            #                                         if jugador["apodo"] == apodo:
            #                                             indice = i
            #                                     if nombre_torneo == "Racing Rivals":
            #                                         racing_inscritos.append(jugadores[indice])
            #                                         racing_resultados.append(jugadores[indice])
            #                                         print(racing_inscritos)
            #                                         jugadores[indice]["torneos"].append(nombre_torneo)
            #                                         if len(racing_inscritos) == TORNEO_INDIVIDUAL:
            #                                             for torneo in torneos_disponibles:
            #                                                 if torneo["datos"][0] == nombre_torneo:
            #                                                     torneo["estado"] = "Cerrado"
            #                                     elif nombre_torneo == "Champions Cup":
            #                                         champions_inscritos.append(jugadores[indice])
            #                                         champions_resultados.append(jugadores[indice])
            #                                         jugadores[indice]["torneos"].append(nombre_torneo)
            #                                         if len(champions_inscritos) == TORNEO_INDIVIDUAL:
            #                                             for torneo in torneos_disponibles:
            #                                                 if torneo["datos"][0] == nombre_torneo:
            #                                                     torneo["estado"] = "Cerrado"
            #                                     elif nombre_torneo == "Smash Showdown":
            #                                         smash_inscritos.append(jugadores[indice])
            #                                         smash_resultados.append(jugadores[indice])
            #                                         jugadores[indice]["torneos"].append(nombre_torneo)
            #                                         if len(smash_inscritos) == TORNEO_INDIVIDUAL:
            #                                             for torneo in torneos_disponibles:
            #                                                 if torneo["datos"][0] == nombre_torneo:
            #                                                     torneo["estado"] = "Cerrado"
            #                                     mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_inscritos, champions_inscritos, smash_inscritos)
            #                                     input("Enter para Continuar...")
            #                                 elif confirmar.lower() == "n": print("\n-------------------------------------------------------\nRegistro Cancelado")
            # preguntar = ""
            # while preguntar.lower() != "s" and preguntar.lower() != "n":
            #     preguntar = input("\n-------------------------------------------------------\n¿Desea Continuar Inscribiendo otro Jugador/Equipo en un Torneo? (SI = S / NO = N): ")
            #     if preguntar.lower() == "s":
            #         validacion = True
            #     elif preguntar.lower() == "n": validacion = False
        
        
        

def mostrar_torneos_disponibles(torneos_disponibles:list) -> None:
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
            
            
            
            
def mostrar_jugadores_inscritos_torneo(nombre_torneo:str, racing_resultados:list, champions_resultados:list, smash_resultados:list) -> None:
    if nombre_torneo == "Champions Cup":
        if len(champions_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Champions Cup")
        else:
            torneo = sorted(champions_resultados, key = lambda x: x['puntos'], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre", "Apodo", "Carrera", "Puntos", "Victorias", "Derrotas"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^40}|{titulo[3]:^10}|{titulo[4]:^12}|{titulo[5]:^10}\n----------------------------------------------------------------------------------------------------------------------\n")
            for jugador in torneo:
                print(f"{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^40}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}")
                print("\n----------------------------------------------------------------------------------------------------------------------\n")
            print("Cantidad Total de Jugadores Registrados: {}".format(len(torneo)))
    elif nombre_torneo == "Racing Rivals":
        if len(racing_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Racing Rivals")
        else:
            torneo = sorted(racing_resultados, key = lambda x: x['puntos'], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre", "Apodo", "Carrera", "Puntos", "Victorias", "Derrotas"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^40}|{titulo[3]:^10}|{titulo[4]:^12}|{titulo[5]:^10}\n----------------------------------------------------------------------------------------------------------------------\n")
            for jugador in torneo:
                print(f"{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^40}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}")
                print("\n----------------------------------------------------------------------------------------------------------------------\n")
            print("Cantidad Total de Jugadores Registrados: {}".format(len(torneo)))
    elif nombre_torneo == "Smash Showdown":
        if len(smash_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Smash Showdown")
        else:
            torneo = sorted(smash_resultados, key=lambda x: x['puntos'], reverse=True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre", "Apodo", "Carrera", "Puntos", "Victorias", "Derrotas"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^40}|{titulo[3]:^10}|{titulo[4]:^12}|{titulo[5]:^10}\n----------------------------------------------------------------------------------------------------------------------\n")
            for jugador in torneo:
                print(f"{jugador["nombre"]:^20}|{jugador["apodo"]:^20}|{jugador["carrera"]:^40}|{jugador["puntos"]:^10}|{jugador["victorias"]:^12}|{jugador["derrotas"]:^10}")
                print("\n----------------------------------------------------------------------------------------------------------------------\n")
            print("Cantidad Total de Jugadores Registrados: {}".format(len(torneo)))
        
        
        
        
def mostrar_equipos_inscritos_torneo(nombre_torneo:str, itson_resultados:list, strike_resultados:list) -> None:
    if nombre_torneo == "ITSON Championship":
        if len(itson_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo ITSON Championship")
        else:
            torneo = sorted(itson_resultados, key = lambda x: x["puntos"], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo)) 
            titulo = ["Nombre Equipo", "Capitan", "Puntos", "Victorias", "Derrotas", "Miembros"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^10}|{titulo[3]:^12}|{titulo[4]:^10}|\t{titulo[5]:<40}\n----------------------------------------------------------------------------------------------------------------------\n")
            for equipo in torneo:
                print(f"{equipo["nombre_equipo"]:^20}|{equipo["capitan"]:^20}|{equipo["puntos"]:^10}|{equipo["victorias"]:^12}|{equipo["derrotas"]:^10}|", end="\t")
                for indice, miembro in enumerate(equipo["miembros"]):
                    if indice == len(equipo["miembros"]) - 1:
                        print(miembro)
                    else: print("{}".format(miembro), end=", ")
                print("\n----------------------------------------------------------------------------------------------------------------------\n")
            print("Cantidad Total de Equipos Registrados: {}\n".format(len(torneo)))
    elif nombre_torneo == "Strike Showdown":
        if len(strike_resultados) < 1:
            print("\n-------------------------------------------------------\nNo se han Registrado Participantes en el Torneo Strike Showdown")
        else:
            torneo = sorted(strike_resultados, key = lambda x: x["puntos"], reverse = True)
            print("\nNombre del Torneo: {}".format(nombre_torneo))
            titulo = ["Nombre Equipo", "Capitan", "Puntos", "Victorias", "Derrotas", "Miembros"]
            print(f"\n----------------------------------------------------------------------------------------------------------------------\n{titulo[0]:^20}|{titulo[1]:^20}|{titulo[2]:^10}|{titulo[3]:^12}|{titulo[4]:^10}|\t{titulo[5]:<40}\n----------------------------------------------------------------------------------------------------------------------\n")
            for equipo in torneo:
                print(f"{equipo["nombre_equipo"]:^20}|{equipo["capitan"]:^20}|{equipo["puntos"]:^10}|{equipo["victorias"]:^12}|{equipo["derrotas"]:^10}|", end="\t")
                for indice, miembro in enumerate(equipo["miembros"]):
                    if indice == len(equipo["miembros"]) - 1:
                        print(miembro)
                    else: print("{}".format(miembro), end=", ")
                print("\n----------------------------------------------------------------------------------------------------------------------\n")
            print("Cantidad Total de Equipos Registrados: {}\n".format(len(torneo)))




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
    for torneo in torneos_disponibles:
        if torneo["datos"][0] == nombre_torneo:
            return True
    return False


def mostrar_torneos_activos() -> None:
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
        
        
def validar_equipo_en_torneo(nombre_equipo:str, nombre_torneo:str) -> bool:
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
    

def retornar_estado_torneo(nombre_torneo:str) -> str:
    for torneo in torneos_disponibles:
        if torneo["datos"][0] == nombre_torneo and torneo["estado"] == "Inscripcion Abierta":
            estado = "Inscripción Abierta"
        elif torneo["datos"][0] == nombre_torneo and torneo["estado"] == "Cerrado":
            estado = "Cerrado"
        elif torneo["datos"][0] == nombre_torneo and torneo["estado"] == "En Curso":
            estado = "En Curso"
        elif torneo["datos"][0] == nombre_torneo and torneo["estado"] == "Finalizado":
            estado = "Finalizado"
    return estado


def validar_jugador_en_torneo(apodo:str, nombre_torneo:str) -> bool:
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
    
def retornar_torneo(nombre_torneo:str):
    for torneo in torneos_disponibles:
        if torneo["nombre"] == nombre_torneo:
            return torneo