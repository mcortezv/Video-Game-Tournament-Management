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