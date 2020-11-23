class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)
    
    def has_player(self, player):
        for person in self.players:
            if person == player:
                return True
        else:
            return False
        
    def play_game(self,match_result):
        if match_result == True:
            self.points = 3
        
        
        