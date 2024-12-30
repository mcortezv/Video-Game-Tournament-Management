import jugadores, equipos, torneos, utilerias, random

emparejamientos = {"itson": list(), 
         "racing": list(), 
         "strike": list(),  
         "champions": list(), 
         "smash": list(), 
         }

fases = {"itson": {"numero": 1, "resultados_registrados": None}, 
         "racing": {"numero": 1, "resultados_registrados": None}, 
         "strike": {"numero": 1, "resultados_registrados": None}, 
         "champions": {"numero": 1, "resultados_registrados": None}, 
         "smash": {"numero": 1, "resultados_registrados": None}
         }


def generar() -> None:
    nombre_torneo = utilerias.pedir_dato("Ingrese el Nombre del Torneo: ")
    if torneos.validar_torneo_existente(nombre_torneo) == False:
        print("\n-------------------------------------------------------\nEl Nombre No Corresponde a Ningun Torneo Disponible")
    else:
        estado_torneo = torneos.retornar_estado_torneo(nombre_torneo)
        if estado_torneo == "Inscripcion Abierta":
            print("\n-------------------------------------------------------\nEmparejamiento Para Este Torneo No Disponible ya que la Inscripcion Sigue Abierta")
        elif estado_torneo == "Finalizado":
            print("\n-------------------------------------------------------\nEl Emparejamiento Para Este Torneo ha Sido Desabilitado ya que el Torneo ha Finalizado")
        else:
            torneo = torneos.retornar_torneo(nombre_torneo)
            if validar_resultados_registrados(torneo) == False:
                print("\n-------------------------------------------------------\nAun no se Han Registrado los Resultados de la Fase: {} de Este Torneo, por lo que no se Pueden Generar Nuevos Emparejamientos".format(fases[torneo]["numero"]))
            else:     
                torneos.torneos_disponibles[torneo]["estado"] = "En Curso"
                participantes = torneos.registros[torneo]["resultados"]
                random.shuffle(participantes)
                emparejamientos[torneo].clear()
                if torneos.torneos_disponibles[torneo]["tipo"] == "Equipos":
                    for i, _ in enumerate(participantes):
                        if i % 2 != 0:
                            emparejamientos[torneo].append({"contrincante1": participantes[i - 1]["nombre_equipo"], "contrincante2": participantes[i]["nombre_equipo"], "ganador": None})
                elif torneos.torneos_disponibles[torneo]["tipo"] == "Jugadores":     
                    for i, _ in enumerate(participantes):
                        if i % 2 != 0:
                            emparejamientos[torneo].append({"contrincante1": participantes[i - 1]["apodo"], "contrincante2": participantes[i]["apodo"], "ganador": None})
                fases[torneo]["resultados_registrados"] = False
                mostrar_emparejamientos(torneo)
                preguntar = ""
                while preguntar.lower() not in ("s", "n"):
                    preguntar = input("-------------------------------------------------------\n¿Desea Registrar los Resultados para Algun Torneo? (SI = S / NO = N): ").lower()
                    if preguntar == "s":
                        registrar_resultado()
    
            
      
def registrar_resultado() -> None:
    nombre_torneo = utilerias.pedir_dato("Ingrese el Nombre del Torneo: ")
    if torneos.validar_torneo_existente(nombre_torneo) == False:
        print("\n-------------------------------------------------------\nEl Nombre No Corresponde a Ningun Torneo Disponible")
    else:
        estado_torneo = torneos.retornar_estado_torneo(nombre_torneo)
        torneo = torneos.retornar_torneo(nombre_torneo)
        if estado_torneo == "Inscripcion Abierta" or estado_torneo == "Cerrado":
            print("\n-------------------------------------------------------\nEl Registro de Resultados Aun no Se Encuentra Disponible ya que Aun No se Han Generado Emparejamientos")
        elif estado_torneo == "Finalizado":
            print("\n-------------------------------------------------------\nEl Registro de Resultados Para Este Torneo ha Sido Desabilitado ya que el Torneo ha Finalizado")
        elif fases[torneo]["resultados_registrados"] == True:
            print("\n-------------------------------------------------------\nYa se Han Registrado Los Resultados de la Fase {}".format(fases[torneo]["numero"]))
        else:
            for emparejamiento in emparejamientos[torneo]:
                ganador = ""
                while ganador not in (emparejamiento["contrincante1"], emparejamiento["contrincante2"]):
                    ganador = utilerias.pedir_dato("Ingrese al Ganador del Enfrentamiento {} vs {}: ".format(emparejamiento["contrincante1"], emparejamiento["contrincante2"]))
                    emparejamiento["ganador"] = ganador
                perdedor = emparejamiento["contrincante1"] if ganador == emparejamiento["contrincante2"] else emparejamiento["contrincante2"]
                if torneos.torneos_disponibles[torneo]["tipo"] == "Equipos":
                    for equipo in equipos.equipos:
                        if equipo["nombre_equipo"] == ganador:
                            equipo["puntos"] += 3 
                            equipo["victorias"] += 1
                        elif equipo["nombre_equipo"] == perdedor:
                            equipo["derrotas"] += 1
                    for i, participante in enumerate(torneos.registros[torneo]["resultados"]):
                        if participante["nombre_equipo"] == perdedor:
                            del torneos.registros[torneo]["resultados"][i]
                elif torneos.torneos_disponibles[torneo]["tipo"] == "Jugadores":   
                    for jugador in jugadores.jugadores:
                        if jugador["apodo"] == ganador:
                            jugador["puntos"] += 3 
                            jugador["victorias"] += 1
                        elif jugador["apodo"] == perdedor:
                            jugador["derrotas"] += 1
                    for i, participante in enumerate(torneos.registros[torneo]["resultados"]):
                        if participante["apodo"] == perdedor:
                            del torneos.registros[torneo]["resultados"][i]
            torneos.mostrar_participantes_inscritos_torneo(torneo)
            fases[torneo]["numero"] += 1
            fases[torneo]["resultados_registrados"] = True
            if len(torneos.registros[torneo]["resultados"]) < 2:
                torneos.torneos_disponibles[torneo]["estado"] = "Finalizado"
                print("\n-------------------------------------------------------\nTorneo Finalizado")
                input("Enter para Continuar...")
                torneos.mostrar_participantes_inscritos_torneo(torneo)
            else:   
                preguntar = ""
                while preguntar.lower() not in ("s", "n"):
                    preguntar = input("\n-------------------------------------------------------\n¿Desea Generar Emparejamientos para Otro Torneo o Fase? (SI = S / NO = N): ").lower()
                    if preguntar == "s":
                        generar()                         


def mostrar_emparejamientos(torneo:str) -> None:
    print("\nEmparejamientos Para ITSON Championship - Fase: {}\n-------------------------------------------------------\nContrincante 1            Contrincante 2\n-------------------------------------------------------\n".format(fases[torneo]["numero"]))
    for emparejamiento in emparejamientos[torneo]:
        print(f"{emparejamiento["contrincante1"]:<20}{emparejamiento["contrincante2"]:<20}\n")
                

def validar_resultados_registrados(torneo:str) -> bool:
    return fases[torneo]["resultados_registrados"]