'''Programa principal de games'''


from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json

def main(archivo_torneo:str):
    '''Funcion principal'''
    if archivo_torneo != "":
        with open(archivo_torneo, "r", encoding = "utf-8") as f:
            torneo = json.load(f)

    else:
        players_mexico = ['Chicharito','Chucky','Ochoa','Tecatito','Guardado','Herrera','Layun','Moreno','Oribe','Jimenez']
        players_españia = ['Casillas','Ramos','Pique','Iniesta','Xavi','Torres','Villa','Silva','Fabregas','Pedro']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_españia = [Athlete(x) for x in players_españia]
        soccer = Sport("Soccer",11,"FIFA")
        mexico = Team("Mexico",soccer,lista_mexico)
        españa = Team("España",soccer ,lista_españia)
        juego = Game(mexico,españa)
        torneo = [juego.to_json()]
        archivo = "torneo.json"
        with open(archivo, "w", encoding = "utf-8") as file:
            json.dump(torneo,file,ensure_ascii = False , indent=4)
        print(f"Se escribio archivo {archivo} satisfactoriamente")

    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = "torneo.json"
    main(archivo_torneo)