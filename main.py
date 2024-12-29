import jugadores, equipos, torneos, emparejamientos

def main():
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
            jugadores.registrar()
        elif opcion == "2":
            equipos.registrar()
        elif opcion == "3":
            equipos.actualizar()
        elif opcion == "4":
            equipos.eliminar()
        elif opcion == "5":
            torneos.inscribir()
        elif opcion == "6":
            jugadores.mostrar()
        elif opcion == "7":
            equipos.mostrar()
        elif opcion == "8":
            torneos.mostrar_torneos_disponibles()
        elif opcion == "9":
            emparejamientos.generar()
        elif opcion == "10":
            emparejamientos.registrar_resultado()
        elif opcion == "11":
            torneos.mostrar_clasificacion()
        elif opcion == "12":
            torneos.mostrar_top_torneo()
        else: 
            print("Opcion no Valida, Ingrese una del 1 al 13")
            continue

if __name__ == "__main__":
    main()