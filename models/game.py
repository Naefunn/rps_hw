class Game():
    def __init__(self, _player_1, _player_2):
        self.player_1 = _player_1
        self.player_2 = _player_2

    def play_game(self, player_1, player_2):
        winner = "player 2"
        
        if player_1 == player_2:
            winner = "tie"
        if player_1 == "rock" and player_2 == "scissors":
            winner = "player 1"
        if player_1 == "scissors" and player_2 == "paper":
            winner = "player 1"
        if player_1 == "paper" and player_2 == "rock":
            winner = "player 1"
        
        return winner
