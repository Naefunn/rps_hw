import re
from flask import render_template
from app import app
from models.player import Player
from models.game import Game


@app.route('/<choice_1>/<choice_2>')
def get_winner(choice_1, choice_2):
    player_1 = choice_1
    player_2 = choice_2
    game = Game(player_1, player_2)
    result = game.play_game(player_1, player_2)
    return render_template("index.html", result=result)