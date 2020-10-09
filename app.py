from flask import Flask
from flask import render_template, request, redirect

import numpy as np
import game_functions
from game_functions import play

session = []
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():

    if request.form.get("new_game"):
        game = np.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0] ).reshape( (3,3) )
        session.clear()
        session.append(game)
        response = ["New game, choose an empty slot and submit with 'Play' button"]
        return render_template('gameplay.html', game=game, response=response)

    else:
        if request.method == "POST":
            game = session[0]
            player_move = request.form.get("player move")
            if player_move == None:
                response = ["Please choose an empty cell and submit with 'Play' button"]
                return render_template('gameplay.html', game=game, response=response)
            else:
                game, response = play(game, int(player_move))
                session.clear()
                session.append(game)

                return render_template('gameplay.html', game=game, response=response)

    new = np.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0] ).reshape( (3,3) )
    session.append(new)
    response = ['Hi there new player!', 'To start playing please choose an empty cell and press "play"']

    return render_template('gameplay.html', game=new, response=response)

if __name__ == "__main__":
    app.run(debug=True)