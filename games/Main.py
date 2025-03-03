''' こにしわこにしわ '''
from Athlete import Athlete
from Sport import Sport
from Game import Game
from Team import Team
import json
import Game_logic as gl

def main(archivo_torneo:str):
    ''' Funcion principal de game '''
    if archivo_torneo != "":
        with open(archivo_torneo, "r") as f:
            torneo = json.load(archivo_torneo)
    else:
        gl.create_gamefile()
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "r", encoding='utf8') as f:
            torneo = json.load(f)

    # Jugar todos los juegos del torneo
    gl.play_game(torneo)
    # Calcular puntuación
    tablero = gl.scoring(torneo)
    gl.display_tablero(tablero)

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)
