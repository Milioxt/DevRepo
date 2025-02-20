'''
    Clase Team:Equipo
'''
from Athlete import Athlete
from Sport import Sport

class Team:
    '''Clase para representar un equipo'''
    def __init__(self, name:str, sport:Sport):
        self.name = name
        self.sport = sport
        self.players = []
    
    def add_player(self, player:Athlete):
        '''Agregar un jugador al equipo'''
        self.players.append(player)
    
    def __str__(self):
        return f"Team: {self.name}, {self.sport}"
    
    def __repr__(self):
        return f"Team(name= '{self.name}', sport= {self.sport})"
    
    def to_json(self)->dict:
        '''Convertir Team a JSON'''
        return {"name":self.name, "sport":self.sport.to_json(), "players":[p.to_json() for p in self.players]}
    
if __name__ == "__main__":
    a1 = Athlete("Michael Jordan")
    a2 = Athlete("Kobe Bryant")
    a3 = Athlete("Lebron James")
    a4 = Athlete("Stephen Curry")
    a5 = Athlete("Shaquille O'Neal")
    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Los angeles Lakers", s, [a1, a2, a3, a4, a5])
    print(lakers)
    print(repr(lakers))
