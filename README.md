# **Tournament Management System**

This project is an interactive system to manage tournaments, allowing registration of players and teams, creating matchups, recording results, and displaying rankings. Designed mainly for competitive video games, the system can be adapted to various contexts. [Versión Español](./README.es.md)

## **Main Features**

### 1. **Player and Team Management**
- Register new players or teams.
- Creation and management of teams.

### 2. **Tournament Management**
- Registration of players or teams in tournaments.
- Generate matchups.
- Record match results.

### 3. **Matchups and Results**
- Generation of random matchups by phase.
- Recording results to determine winners and update scores.
- Visualize rankings, top players or teams.

## **Project Files**

| File                 | Description                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------|
| `main.py`            | Main file that manages the interactive menu to use all system functionalities.                                 |
| `jugadores.py`       | Module for managing the registration, validation, and querying of players.                                     |
| `equipos.py`         | Module for managing teams, including registration, updating, and deletion.                                     |
| `torneos.py`         | Defines the tournament structures and allows participant registration, showing details, and managing rankings. |
| `emparejamientos.py` | Contains logic to generate matchups, record results, and manage tournament phases.                             |
| `utilerias.py`       | Provides auxiliary functions, such as user data validation and input.                                          |
---

## **Installation and Execution**

### 1. **Requisites**:

- Python 3.8 or higher.

### 2. **Installation**: Clone this repository:

```bash
git clone https://github.com/mcortezv/Video-Game-Tournament-Management
```
### 3. **Execution**: Run the main file:

```bash
python main.py
```

## **Usage**
Follow the interactive menu to perform the following actions:
- Register players and teams.
- Register participants in tournaments.
- Generate matchups and record results.

## **License**
This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for more details.