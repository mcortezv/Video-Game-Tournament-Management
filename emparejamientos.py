import utilerias, torneos, random

emparejamientos = list()
fases = {"itson": ["ITSON Championship", 1, None], "racing": ["Racing Rivals", 1, None], "strike": ["Strike Showdown", 1, None], "champions": ["Champions Cup", 1, None], "smash": ["Smash Showdown", 1, None]}

def generar(torneos_disponibles:list, emparejamientos:list, itson_inscritos:list, racing_inscritos:list, strike_inscritos:list, champions_inscritos:list, smash_inscritos:list, itson_resultados:list, racing_resultados:list, strike_resultados:list, champions_resultados:list, smash_resultados:list, jugadores:list, equipos:list, fases:dict) -> None:
    nombre_torneo = input("Ingrese el Nombre del Torneo: ")
    validar_torneo = modulo_utilerias.validar_torneo(torneos_disponibles, nombre_torneo)
    if validar_torneo == False:
        print("\n-------------------------------------------------------\nEl Nombre No Corresponde a Ningun Torneo Disponible")
    else:
        validar_estado_torneo = modulo_utilerias.validar_estado_torneo(torneos_disponibles, nombre_torneo)
        if validar_estado_torneo == "Inscripción Abierta":
            print("\n-------------------------------------------------------\nEmparejamiento Para Este Torneo No Disponible ya que la Inscripcion Sigue Abierta")
        elif validar_estado_torneo == "Finalizado":
            print("\n-------------------------------------------------------\nEl Emparejamiento Para Este Torneo ha Sido Desabilitado ya que el Torneo ha Finalizado")
        else:
            validar_registro_completado = modulo_utilerias.validar_registro_completado(nombre_torneo, fases)
            if validar_registro_completado == False:
                print("\n-------------------------------------------------------\nAun No Se Han Registrado los Resultados del Emparejamiento Anterior, por lo Cual No se pueden Generar Nuevos Emparejamientos Todavia")
            else:
                for fase in fases.values():
                    if fase[0] == nombre_torneo:
                        if fase[1] > 1:
                            if fase[2] == True:
                                siguiente_emparejamiento(torneos_disponibles, emparejamientos, fases, nombre_torneo, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                            else:
                                print("\n-------------------------------------------------------\nAun no se Han Registrado los Resultados de la Fase: {} de Este Torneo, por lo que no se Pueden Generar Nuevos Emparejamientos".format(fase[1]))
                        else:
                            for torneo in torneos_disponibles:
                                if torneo["datos"][0] == nombre_torneo:
                                    torneo["estado"] = "En Curso"
                            if nombre_torneo == "ITSON Championship":
                                random.shuffle(itson_inscritos)
                                for i in range(len(itson_inscritos)):
                                    if i % 2 != 0:
                                        emparejamiento = {"torneo": nombre_torneo, "fase": fase[1], "equipo1": itson_inscritos[i - 1]["nombre_equipo"], "equipo2": itson_inscritos[i]["nombre_equipo"], "ganador": None}
                                        emparejamientos.append(emparejamiento)
                                    else: pass
                                fase[2] = False
                                mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
                                preguntar = ""
                                while preguntar.lower() != "s" and preguntar.lower() != "n":
                                    preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                    if preguntar.lower() == "s":
                                        registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                    elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Strike Showdown":
                                random.shuffle(strike_inscritos)
                                for i in range(len(strike_inscritos)):
                                    if i % 2 != 0:
                                        emparejamiento = {"torneo": nombre_torneo, "fase": fase[1], "equipo1": strike_inscritos[i - 1]["nombre_equipo"], "equipo2": strike_inscritos[i]["nombre_equipo"], "ganador": None}
                                        emparejamientos.append(emparejamiento)
                                    else: pass
                                fase[2] = False
                                mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
                                preguntar = ""
                                while preguntar.lower() != "s" and preguntar.lower() != "n":
                                    preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                    if preguntar.lower() == "s":
                                        registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                    elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Champions Cup":
                                random.shuffle(champions_inscritos)
                                for i in range(len(champions_inscritos)):
                                    if i % 2 != 0:
                                        emparejamiento = {"torneo": nombre_torneo, "fase": fase[1], "jugador1": champions_inscritos[i - 1]["apodo"], "jugador2": champions_inscritos[i]["apodo"], "ganador": None}
                                        emparejamientos.append(emparejamiento)
                                    else: pass
                                fase[2] = False
                                mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
                                preguntar = ""
                                while preguntar.lower() != "s" and preguntar.lower() != "n":
                                    preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                    if preguntar.lower() == "s":
                                        registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                    elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Racing Rivals":
                                random.shuffle(racing_inscritos)
                                for i in range(len(racing_inscritos)):
                                    if i % 2 != 0:
                                        emparejamiento = {"torneo": nombre_torneo, "fase": fase[1], "jugador1": racing_inscritos[i - 1]["apodo"], "jugador2": racing_inscritos[i]["apodo"], "ganador": None}
                                        emparejamientos.append(emparejamiento)
                                    else: pass
                                fase[2] = False
                                mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
                                preguntar = ""
                                while preguntar.lower() != "s" and preguntar.lower() != "n":
                                    preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                    if preguntar.lower() == "s":
                                        registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                    elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Smash Showdown":
                                random.shuffle(smash_inscritos)
                                for i in range(len(smash_inscritos)):
                                    if i % 2 != 0:
                                        emparejamiento = {"torneo": nombre_torneo, "fase": fase[1], "jugador1": smash_inscritos[i - 1]["apodo"], "jugador2": smash_inscritos[i]["apodo"], "ganador": None}
                                        emparejamientos.append(emparejamiento)
                                    else: pass
                                fase[2] = False
                                mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
                                preguntar = ""
                                while preguntar.lower() != "s" and preguntar.lower() != "n":
                                    preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                    if preguntar.lower() == "s":
                                        registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                    elif preguntar.lower() == "n": break
            
        
    
    
def registrar_resultado(torneos_disponibles:list, fases, emparejamientos:list, itson_inscritos:list, racing_inscritos:list, strike_inscritos:list, champions_inscritos:list, smash_inscritos:list, itson_resultados:list, racing_resultados:list, strike_resultados:list, champions_resultados:list, smash_resultados:list, jugadores:list, equipos:list) -> None:
    nombre_torneo = modulo_utilerias.pedir_dato("Ingrese el Nombre del Torneo: ")
    validar_torneo = modulo_utilerias.validar_torneo(torneos_disponibles, nombre_torneo)
    if validar_torneo == False:
        print("\n-------------------------------------------------------\nEl Nombre No Corresponde a Ningun Torneo Disponible")
    else:
        validar_estado_torneo = modulo_utilerias.validar_estado_torneo(torneos_disponibles, nombre_torneo)
        if validar_estado_torneo == "Inscripción Abierta" or validar_estado_torneo == "Cerrado":
            print("\n-------------------------------------------------------\nEl Registro de Resultados Aun no Se Encuentra Disponible ya que Aun No se Han Generado Emparejamientos")
        elif validar_estado_torneo == "Finalizado":
            print("\n-------------------------------------------------------\nEl Registro de Resultados Para Este Torneo ha Sido Desabilitado ya que el Torneo ha Finalizado")
        else:
             for fase in fases.values():
                if fase[0] == nombre_torneo:
                    valor_fase = fase[1]
                    entrada_fase = modulo_utilerias.pedir_numero_entero("Ingrese la Fase del Torneo: ")
                    if entrada_fase != valor_fase:
                        print("\n-------------------------------------------------------\nNo se Puede Registrar el Resultado para la Fase: {} ya que el Torneo: {} se Ecuentra en la Fase: {}".format(entrada_fase, nombre_torneo, valor_fase))
                    else:
                        if fase[2] == True:
                            print("\n-------------------------------------------------------\nYa se Han Registrado Los Resultados de la Fase Actual: {}".format( nombre_torneo))
                        else:
                            ganador = ""
                            for torneo in emparejamientos:
                                if torneo["torneo"] == nombre_torneo:
                                    if nombre_torneo == "ITSON Championship":
                                        while ganador not in [torneo["equipo1"], torneo["equipo2"]]:
                                            ganador = input("Ingrese al Ganador del Enfrentamiento {} vs {}: ".format(torneo["equipo1"], torneo["equipo2"]))
                                        torneo["ganador"] = ganador
                                        for equipo in equipos:
                                            if equipo["nombre_equipo"] == ganador:
                                                equipo["puntos"] += 3 
                                                equipo["victorias"] += 1
                                            if ganador == torneo["equipo1"]:
                                                perdedor = torneo["equipo2"]
                                            else: perdedor = torneo["equipo1"]
                                            if equipo["nombre_equipo"] == perdedor:
                                                equipo["derrotas"] += 1
                                        modulo_torneos.mostrar_equipos_inscritos_torneo(nombre_torneo, itson_resultados, strike_resultados)
                                    elif nombre_torneo == "Strike Showdown":
                                        while ganador not in [torneo["equipo1"], torneo["equipo2"]]:
                                            ganador = input("Ingrese al Ganador del Enfrentamiento {} vs {}: ".format(torneo["equipo1"], torneo["equipo2"]))
                                        torneo["ganador"] = ganador
                                        for equipo in equipos:
                                            if equipo["nombre_equipo"] == ganador:
                                                equipo["puntos"] += 3
                                                equipo["victorias"] += 1
                                            if ganador == torneo["equipo1"]:
                                                perdedor = torneo["equipo2"]
                                            else: perdedor = torneo["equipo1"]
                                            if equipo["nombre_equipo"] == perdedor:
                                                equipo["derrotas"] += 1
                                        modulo_torneos.mostrar_equipos_inscritos_torneo(nombre_torneo, itson_resultados, strike_resultados)
                                    elif nombre_torneo == "Champions Cup":
                                        while ganador not in [torneo["jugador1"], torneo["jugador2"]]:
                                            ganador = input("Ingrese al Ganador del Enfrentamiento {} vs {}: ".format(torneo["jugador1"], torneo["jugador2"]))
                                        torneo["ganador"] = ganador
                                        for jugador in jugadores:
                                            if jugador["apodo"] == ganador:
                                                jugador["puntos"] += 3
                                                jugador["victorias"] += 1
                                            if ganador == torneo["jugador1"]:
                                                perdedor = torneo["jugador2"]
                                            else: perdedor = torneo["jugador1"]
                                            if jugador["apodo"] == perdedor:
                                                jugador["derrotas"] += 1
                                        modulo_torneos.mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
                                    elif nombre_torneo == "Racing Rivals":
                                        while ganador not in [torneo["jugador1"], torneo["jugador2"]]:
                                            ganador = input("Ingrese al Ganador del Enfrentamiento {} vs {}: ".format(torneo["jugador1"], torneo["jugador2"]))
                                        torneo["ganador"] = ganador
                                        for jugador in jugadores:
                                            if jugador["apodo"] == ganador:
                                                jugador["puntos"] += 3
                                                jugador["victorias"] += 1
                                            if ganador == torneo["jugador1"]:
                                                perdedor = torneo["jugador2"]
                                            else: perdedor = torneo["jugador1"]
                                            if jugador["apodo"] == perdedor:
                                                jugador["derrotas"] += 1    
                                        modulo_torneos.mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
                                    elif nombre_torneo == "Smash Showdown":
                                        while ganador not in [torneo["jugador1"], torneo["jugador2"]]:
                                            ganador = input("Ingrese al Ganador del Enfrentamiento {} vs {}: ".format(torneo["jugador1"], torneo["jugador2"]))
                                        torneo["ganador"] = ganador
                                        for jugador in jugadores:
                                            if jugador["apodo"] == ganador:
                                                jugador["puntos"] += 3
                                                jugador["victorias"] += 1
                                            if ganador == torneo["jugador1"]:
                                                perdedor = torneo["jugador2"]
                                            else: perdedor = torneo["jugador1"]
                                            if jugador["apodo"] == perdedor:
                                                jugador["derrotas"] += 1
                                        modulo_torneos.mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
                            fase[1] += 1 
                            fase[2] = True
                            if nombre_torneo == "ITSON Championship":
                                if len(itson_inscritos) <= 2:
                                    for torneo in torneos_disponibles:
                                        if torneo["datos"][0] == nombre_torneo:
                                            torneo["estado"] = "Finalizado"
                                            print("\n-------------------------------------------------------\nTorneo Finalizado")
                                            input("Enter para Continuar...")
                                            modulo_torneos.mostrar_equipos_inscritos_torneo(nombre_torneo, itson_resultados, strike_resultados)
                                else:   
                                    preguntar = ""
                                    while preguntar.lower() != "s" and preguntar.lower() != "n":
                                        preguntar = input("\n-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                        if preguntar.lower() == "s":
                                            siguiente_emparejamiento(torneos_disponibles, emparejamientos, fases, nombre_torneo, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                        elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Strike Showdown":
                                if len(strike_inscritos) <= 2:
                                    for torneo in torneos_disponibles:
                                        if torneo["datos"][0] == nombre_torneo:
                                            torneo["estado"] = "Finalizado"
                                            print("\n-------------------------------------------------------\nTorneo Finalizado")
                                            input("Enter para Continuar...")
                                            modulo_torneos.mostrar_equipos_inscritos_torneo(nombre_torneo, itson_resultados, strike_resultados)
                                else:   
                                    preguntar = ""
                                    while preguntar.lower() != "s" and preguntar.lower() != "n":
                                        preguntar = input("\n-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                        if preguntar.lower() == "s":
                                            siguiente_emparejamiento(torneos_disponibles, emparejamientos, fases, nombre_torneo, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                        elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Champions Cup":
                                if len(champions_inscritos) <= 2:
                                    for torneo in torneos_disponibles:
                                        if torneo["datos"][0] == nombre_torneo:
                                            torneo["estado"] = "Finalizado"
                                            print("\n-------------------------------------------------------\nTorneo Finalizado")
                                            input("Enter para Continuar...")
                                            modulo_torneos.mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
                                else:   
                                    preguntar = ""
                                    while preguntar.lower() != "s" and preguntar.lower() != "n":
                                        preguntar = input("\n-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                        if preguntar.lower() == "s":
                                            siguiente_emparejamiento(torneos_disponibles, emparejamientos, fases, nombre_torneo, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                        elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Racing Rivals":
                                if len(racing_inscritos) <= 2:
                                    for torneo in torneos_disponibles:
                                        if torneo["datos"][0] == nombre_torneo:
                                            torneo["estado"] = "Finalizado"
                                            print("\n-------------------------------------------------------\nTorneo Finalizado")
                                            input("Enter para Continuar...")
                                            modulo_torneos.mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
                                else:   
                                    preguntar = ""
                                    while preguntar.lower() != "s" and preguntar.lower() != "n":
                                        preguntar = input("\n-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                        if preguntar.lower() == "s":
                                            siguiente_emparejamiento(torneos_disponibles, emparejamientos, fases, nombre_torneo, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                        elif preguntar.lower() == "n": break
                            elif nombre_torneo == "Smash Showdown":
                                if len(smash_inscritos) <= 2:
                                    for torneo in torneos_disponibles:
                                        if torneo["datos"][0] == nombre_torneo:
                                            torneo["estado"] = "Finalizado"
                                            print("\n-------------------------------------------------------\nTorneo Finalizado")
                                            input("Enter para Continuar...")
                                            modulo_torneos.mostrar_jugadores_inscritos_torneo(nombre_torneo, racing_resultados, champions_resultados, smash_resultados)
                                else:   
                                    preguntar = ""
                                    while preguntar.lower() != "s" and preguntar.lower() != "n":
                                        preguntar = input("\n-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                                        if preguntar.lower() == "s":
                                            siguiente_emparejamiento(torneos_disponibles, emparejamientos, fases, nombre_torneo, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                                        elif preguntar.lower() == "n": break
                            
                            
                
                
def siguiente_emparejamiento(torneos_disponibles:list, emparejamientos:list, fases:dict, nombre_torneo:str, itson_inscritos:list, racing_inscritos:list, strike_inscritos:list, champions_inscritos:list, smash_inscritos:list, itson_resultados:list, racing_resultados:list, strike_resultados:list, champions_resultados:list, smash_resultados:list, jugadores:list, equipos:list) -> None:
        if nombre_torneo == "ITSON Championship":
            itson_inscritos.clear()
            emparejamientos_a_eliminar = []
            for emparejamiento in emparejamientos:
                if emparejamiento["torneo"] == nombre_torneo:
                    ganador = modulo_utilerias.retornar_datos_equipo(equipos, emparejamiento["ganador"])
                    itson_inscritos.append(ganador)
                    emparejamientos_a_eliminar.append(emparejamiento)
            for emparejamiento in emparejamientos_a_eliminar:
                emparejamientos.remove(emparejamiento)
            for i in range(len(itson_inscritos)):
                if i % 2 != 0:
                    temporal = {"torneo": nombre_torneo, "fase": fases["itson"][1], "equipo1": itson_inscritos[i - 1]["nombre_equipo"], "equipo2": itson_inscritos[i]["nombre_equipo"], "ganador": None}
                    emparejamientos.append(temporal)
                else: pass
            fases["itson"][2] = False
            mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
            preguntar = ""
            while preguntar.lower() != "s" and preguntar.lower() != "n":
                preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                if preguntar.lower() == "s":
                    registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                elif preguntar.lower() == "n": break
        elif nombre_torneo == "Strike Showdown":
            strike_inscritos.clear()
            emparejamientos_a_eliminar = []
            for emparejamiento in emparejamientos:
                if emparejamiento["torneo"] == nombre_torneo:
                    ganador = modulo_utilerias.retornar_datos_equipo(equipos, emparejamiento["ganador"])
                    strike_inscritos.append(ganador)
                    emparejamientos_a_eliminar.append(emparejamiento)
            for emparejamiento in emparejamientos_a_eliminar:
                emparejamientos.remove(emparejamiento)
            for i in range(len(strike_inscritos)):
                if i % 2 != 0:
                    temporal = {"torneo": nombre_torneo, "fase": fases["strike"][1], "equipo1": strike_inscritos[i - 1]["nombre_equipo"], "equipo2": strike_inscritos[i]["nombre_equipo"], "ganador": None}
                    emparejamientos.append(temporal)
                else: pass
            fases["strike"][2] = False
            mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
            preguntar = ""
            while preguntar.lower() != "s" and preguntar.lower() != "n":
                preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                if preguntar.lower() == "s":
                    registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                elif preguntar.lower() == "n": break
        elif nombre_torneo == "Champions Cup":
            champions_inscritos.clear()
            emparejamientos_a_eliminar = []
            for emparejamiento in emparejamientos:
                if emparejamiento["torneo"] == nombre_torneo:
                    ganador = modulo_utilerias.retornar_datos_jugador(jugadores, emparejamiento["ganador"])
                    champions_inscritos.append(ganador)
                    emparejamientos_a_eliminar.append(emparejamiento)
            for emparejamiento in emparejamientos_a_eliminar:
                emparejamientos.remove(emparejamiento)
            for i in range(len(champions_inscritos)):
                if i % 2 != 0:
                    temporal = {"torneo": nombre_torneo, "fase": fases["champions"][1], "jugador1": champions_inscritos[i - 1]["apodo"], "jugador2": champions_inscritos[i]["apodo"], "ganador": None}
                    emparejamientos.append(temporal)
                else: pass
            fases["champions"][2] = False
            mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
            preguntar = ""
            while preguntar.lower() != "s" and preguntar.lower() != "n":
                preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                if preguntar.lower() == "s":
                    registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                elif preguntar.lower() == "n": break
        elif nombre_torneo == "Racing Rivals":
            racing_inscritos.clear()
            emparejamientos_a_eliminar = []
            for emparejamiento in emparejamientos:
                if emparejamiento["torneo"] == nombre_torneo:
                    ganador = modulo_utilerias.retornar_datos_jugador(jugadores, emparejamiento["ganador"])
                    racing_inscritos.append(ganador)
                    emparejamientos_a_eliminar.append(emparejamiento)
            for emparejamiento in emparejamientos_a_eliminar:
                emparejamientos.remove(emparejamiento)
            for i in range(len(racing_inscritos)):
                    if i % 2 != 0:
                        temporal = {"torneo": nombre_torneo, "fase": fases["racing"][1], "jugador1": racing_inscritos[i - 1]["apodo"], "jugador2": racing_inscritos[i]["apodo"], "ganador": None}
                        emparejamientos.append(temporal)
                    else: pass
            fases["racing"][2] = False
            mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
            preguntar = ""
            while preguntar.lower() != "s" and preguntar.lower() != "n":
                preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                if preguntar.lower() == "s":
                    registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                elif preguntar.lower() == "n": break
        elif nombre_torneo == "Smash Showdown":
            smash_inscritos.clear()
            emparejamientos_a_eliminar = []
            for emparejamiento in emparejamientos:
                if emparejamiento["torneo"] == nombre_torneo:
                    ganador = modulo_utilerias.retornar_datos_jugador(jugadores, emparejamiento["ganador"])
                    smash_inscritos.append(ganador)
                    emparejamientos_a_eliminar.append(emparejamiento)
            for emparejamiento in emparejamientos_a_eliminar:
                emparejamientos.remove(emparejamiento)
            for i in range(len(smash_inscritos)):
                if i % 2 != 0:
                    temporal = {"torneo": nombre_torneo, "fase": fases["smash"][1], "jugador1": smash_inscritos[i - 1]["apodo"], "jugador2": smash_inscritos[i]["apodo"], "ganador": None}
                    emparejamientos.append(temporal)
                else: pass
            fases["smash"][2] = False
            mostrar_emparejamientos(nombre_torneo, fases, emparejamientos)
            preguntar = ""
            while preguntar.lower() != "s" and preguntar.lower() != "n":
                preguntar = input("-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ")
                if preguntar.lower() == "s":
                    registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
                elif preguntar.lower() == "n": break




def mostrar_emparejamientos(nombre_torneo:str, fases:int, emparejamientos:list) -> None:
    if nombre_torneo == "ITSON Championship":
        fase = fases["itson"][1]
        print("\nEmparejamientos Para ITSON Championship - Fase: {}\n-------------------------------------------------------\nJugador1            Jugador2\n-------------------------------------------------------\n".format(fase))
        for emparejamiento in emparejamientos:
            if emparejamiento["torneo"] == nombre_torneo:
                print(f"{emparejamiento["equipo1"]:<20}{emparejamiento["equipo2"]:<20}\n")
    elif nombre_torneo == "Strike Showdown":
        fase = fases["strike"][1]
        print("\nEmparejamientos Para Strike Showdown - Fase: {}\n-------------------------------------------------------\nJugador1            Jugador2\n-------------------------------------------------------\n".format(fase))
        for emparejamiento in emparejamientos:
            if emparejamiento["torneo"] == nombre_torneo:
                print(f"{emparejamiento["equipo1"]:<20}{emparejamiento["equipo2"]:<20}\n")
    elif nombre_torneo == "Champions Cup":
        fase = fases["champions"][1]
        print("\nEmparejamientos Para Champions Cup - Fase: {}\n-------------------------------------------------------\nJugador1            Jugador2\n-------------------------------------------------------\n".format(fase))
        for emparejamiento in emparejamientos:
            if emparejamiento["torneo"] == nombre_torneo:
                print(f"{emparejamiento["jugador1"]:<20}{emparejamiento["jugador2"]:<20}\n")
    elif nombre_torneo == "Racing Rivals":
        fase = fases["racing"][1]
        print("\nEmparejamientos Para Racing Rivals - Fase: {}\n-------------------------------------------------------\nJugador1            Jugador2\n-------------------------------------------------------\n".format(fase))
        for emparejamiento in emparejamientos:
            if emparejamiento["torneo"] == nombre_torneo:
                print(f"{emparejamiento["jugador1"]:<20}{emparejamiento["jugador2"]:<20}\n")
    elif nombre_torneo == "Smash Showdown":
        fase = fases["smash"][1]
        print("\nEmparejamientos Smash Showdown - Fase: {}\n-------------------------------------------------------\nJugador1            Jugador2\n-------------------------------------------------------\n".format(fase))
        for emparejamiento in emparejamientos:
            if emparejamiento["torneo"] == nombre_torneo:
                print(f"{emparejamiento["jugador1"]:<20}{emparejamiento["jugador2"]:<20}\n")