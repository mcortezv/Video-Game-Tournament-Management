def pedir_dato(texto:str) -> None:
    while True:
        dato_entrada = input(texto)
        if dato_entrada.strip(): 
            return dato_entrada
        else: 
            print("-------------------------------------------------------\nEl Dato no Puede Estar Vacio, Ingreselo de Nuevo\n")