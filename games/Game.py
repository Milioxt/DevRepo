#SHE TOOK MY MONEY WELL I'M IN NEED YEAH SHE'S A TRIFLING FRIEND INDEED OH SHE'S A GOLD DIGGER WAY OVER TOWN THAT DIGS ON ME
#I AINT SAYING SHE A GOLD DIGGER BUT SHE AINT MESSING WITH NO BROKE NIGGAS


from random import choice
from Team import Team
from Sport import Sport
from Athlete import Athlete

class Game:
    '''Clase game: Juego entre dos equipos'''
    sports_dict = {
        'LMP' :[x for x in range(0,11)],
        'NBA' :[x for x in range(70,121)],
        'NFL' :[x for x in range(3,56)],
        'LMX' :[x for x in range(0,9)],

    }



    def __init__(self,A:Team,B:Team) -> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0



    def play(self):
        '''Juego simulado entre equipos'''
        league = self.A.sport.league
        points = self.sports_dict[league]
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b

    def __str__(self)-> str:
        '''Metodo para mostrar clase como string'''
        return f"""
        -----------------------------------------
        Game: 
        {self.A.name:20s}: {self.score[self.A.name]:3d} 
        {self.B.name:20s}: {self.score[self.B.name]:3d}
        ------------------------------------------
        """
        
    def __repr__(self)-> str:
        '''Metodo para representar clase como string'''
        return f"Game(A={repr(self.A)}, B={repr(self.B)})"
    
    def to_json(self)-> dict:
        '''Convertir Game a JSON'''
        return {"A":self.A.to_json(), "B":self.B.to_json(), "score":self.score}


if __name__ == "__main__":
    dt = ['Jordan','Jhonson','Pipen','Bird','Kobe']
    cz = ['Bjovik','Czack','Pfeizer','Leonard','Kempfe']
    player_a = [Athlete(x) for x in dt]
    player_b = [Athlete(x) for x in cz]
    basketball= Sport("DreamTeam",5,"NBA")
    t = Team("DreamTeam",basketball)
    c = Team("CzackTeam",basketball)
    game = Game(t,c)
    print(game)
    game.play()
    print(game)
    print(repr(game))
    print("---------")
    print(game.to_json())
    