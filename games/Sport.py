class Sport:
    ''' Class for Sport games
    '''

    def __init__(self, name:str, players:int, league:str):
        self.name = name
        if isinstance(players, int): #verificamos que players sea un entero
            self.players = players 
        else:
            self.players = int(players) 
        self.league = league

    def __str__(self)->str:
        '''Reperesentacion en string de Sport'''
        return f"Sport: {self.name}, {self.players}, {self.league}"
    

    def __repr__(self)->str:
        '''Reperesentacion en string de Sport'''
        return f"Sport(name= '{self.name}', players= {self.players}, league= '{self.league}')"
    
    def to_json(self)->dict:
        '''Convertir Sport a JSON'''
        return {"name":self.name, "players":self.players, "league":self.league}
    
if __name__ == "__main__":
    nfl = Sport("Football", 11, "NFL")
    print(nfl)
    print(repr(nfl))
    print(nfl.to_json())