# **Sistema de Gestión de Torneos**

Este proyecto es un sistema interactivo para gestionar torneos, permitiendo el registro de jugadores y equipos, la creación de emparejamientos, el registro de resultados y la visualización de clasificaciones. Diseñado principalmente para videojuegos competitivos, el sistema puede adaptarse a varios contextos.

## **Características Principales**

### 1. **Gestión de Jugadores y Equipos**
- Registrar nuevos jugadores o equipos.
- Creación y gestión de equipos.

### 2. **Gestión de Torneos**
- Registro de jugadores o equipos en torneos.
- Generar emparejamientos.
- Registrar resultados de los partidos.

### 3. **Emparejamientos y Resultados**
- Generación de emparejamientos aleatorios por fase.
- Registro de resultados para determinar ganadores y actualizar puntuaciones.
- Visualización de clasificaciones, mejores jugadores o equipos.

## **Archivos del Proyecto**

| Archivo              | Descripción                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `main.py`            | Archivo principal que gestiona el menú interactivo para usar todas las funcionalidades del sistema.                         |
| `jugadores.py`       | Módulo para gestionar el registro, validación y consulta de jugadores.                                                      |
| `equipos.py`         | Módulo para gestionar equipos, incluyendo registro, actualización y eliminación.                                            |
| `torneos.py`         | Define las estructuras de los torneos y permite el registro de participantes, mostrar detalles y gestionar clasificaciones. |
| `emparejamientos.py` | Contiene la lógica para generar emparejamientos, registrar resultados y gestionar las fases del torneo.                     |
| `utilerias.py`       | Proporciona funciones auxiliares, como validación de datos de usuario e ingreso de datos.                                   |
---

## **Instalación y Ejecución**

### 1. **Requisitos**:

- Python 3.8 o superior.

### 2. **Instalación**: Clona este repositorio:

```bash
git clone https://github.com/mcortezv/Video-Game-Tournament-Management
```
### 3. **Ejecución**: Ejecuta el archivo principal:

```bash
python main.py
```

## **Uso**
Sigue el menú interactivo para realizar las siguientes acciones:
- Registrar jugadores y equipos.
- Registrar participantes en torneos.
- Generar emparejamientos y registrar resultados.

## **Licencia**
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](./LICENSE.md) para más detalles.