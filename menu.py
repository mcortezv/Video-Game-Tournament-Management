import jugadores as modulo_jugadores, equipos as modulo_equipos, torneos as modulo_torneos, emparejamiento as modulo_emparejamientos, utilerias as modulo_utilerias

def main():
    jugadores, equipos, emparejamientos = list(), list(), list()
    itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos = list(), list(), list(), list(), list()
    itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados = list(), list(), list(), list(), list()
    TORNEO_INDIVIDUAL, TORNEO_EQUIPO = 16, 8
    fases = {"itson": ["ITSON Championship", 1, None], "racing": ["Racing Rivals", 1, None], "strike": ["Strike Showdown", 1, None], "champions": ["Champions Cup", 1, None], "smash": ["Smash Showdown", 1, None]}
    torneos_disponibles = [
        {"datos": ("ITSON Championship", "League of Legends", "Equipos de cinco jugadores se enfrentarán en la Grieta del Invocador para demostrar sus habilidades estratégicas y de trabajo en equipo en este popular MOBA.", TORNEO_EQUIPO), "estado": "Inscripción Abierta"},
        {"datos": ("Racing Rivals", "Mario Kart", "Los estudiantes de ITSON competirán en divertidas y frenéticas carreras de Mario Kart, donde la velocidad y el uso inteligente de los ítems serán clave para la victoria.", TORNEO_INDIVIDUAL), "estado": "Inscripción Abierta"},
        {"datos": ("Strike Showdown", "Counter-Strike: Global Offensive ", "Equipos de cinco jugadores se enfrentarán en intensos combates de disparos en primera persona para demostrar quién es el mejor en estrategia y puntería en ITSON.", TORNEO_EQUIPO), "estado": "Inscripción Abierta"},
        {"datos": ("Champions Cup", "FIFA", "Un torneo de fútbol virtual donde los mejores jugadores de FIFA de ITSON competirán por el título de campeón en emocionantes partidos llenos de goles y tácticas.", TORNEO_INDIVIDUAL), "estado": "Inscripción Abierta"},
        {"datos": ("Smash Showdown", "Super Smash Bros. Ultimate", "Los mejores luchadores de ITSON se enfrentarán en intensos combates en el popular juego de lucha Super Smash Bros. Ultimate, donde solo uno saldrá victorioso entre la multitud de personajes icónicos.", TORNEO_INDIVIDUAL), "estado": "Inscripción Abierta"}]
    while True:
        opcion = input("""\nSeleccione una opcion del Menú:\n    
            1. Registrar Nuevo Jugador
            2. Registrar Nuevo Equipo
            3. Actualizar Miembros de un Equipo
            4. Eliminar un Equipo
            5. Inscribir Jugador/Equipo en Torneo
            6. Mostrar Jugadores Registrados
            7. Mostrar Equipos Registrados
            8. Mostrar Torneos Disponibles
            9. Generar Emparejamiento Para Torneo
            10. Registrar Resultado de Emparejamiento
            11. Mostrar Clasificacion de Torneo
            12. Mostrar al Top 3 de Torneo
            13. Terminar Operacion\n""")
        if opcion == "13":
            input("Enter para Salir del Sistema...") 
            break
        elif opcion == "1":
            modulo_jugadores.registrar(jugadores)
        elif opcion == "2":
            modulo_equipos.registrar(equipos, jugadores)
        elif opcion == "3":
            modulo_equipos.actualizar(equipos, jugadores)
        elif opcion == "4":
            modulo_equipos.eliminar(equipos)
        elif opcion == "5":
            modulo_torneos.inscribir(equipos, jugadores, torneos_disponibles, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, TORNEO_INDIVIDUAL, TORNEO_EQUIPO)
        elif opcion == "6":
            modulo_jugadores.mostrar(jugadores)
        elif opcion == "7":
            modulo_utilerias.mostrar_equipos(equipos)
        elif opcion == "8":
            modulo_torneos.mostrar_torneos_disponibles(torneos_disponibles)
        elif opcion == "9":
            modulo_emparejamientos.generar(torneos_disponibles, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos, fases)
        elif opcion == "10":
            modulo_emparejamientos.registrar_resultado(torneos_disponibles, fases, emparejamientos, itson_inscritos, racing_inscritos, strike_inscritos, champions_inscritos, smash_inscritos, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados, jugadores, equipos)
        elif opcion == "11":
            modulo_torneos.mostrar_clasificacion(torneos_disponibles, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados)
        elif opcion == "12":
            modulo_torneos.mostrar_top_torneo(torneos_disponibles, itson_resultados, racing_resultados, strike_resultados, champions_resultados, smash_resultados)
        else: 
            print("Opcion no Valida, Ingrese una del 1 al 13")
            continue

if __name__ == '__main__':
    main()
