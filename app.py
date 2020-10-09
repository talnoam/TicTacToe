from flask import Flask
from flask import render_template, request, redirect

import numpy as np
import game_functions
from game_functions import play


app = Flask(__name__)

@app.route("/game", methods=["GET", "POST"])
def game():
    game = np.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0] ).reshape( (3,3) )

    if request.form.get("new_game"):
        return render_template('gameplay.html', game=game)

    else:
        if request.method == "POST":
            player_move = request.form.get("player move")
            game = play(game, int(player_move))

            return render_template('gameplay.html', game=game)

    return render_template('gameplay.html', game=game)

if __name__ == "__main__":
    app.run(debug=True)