import random
from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

hands = ('가위', '바위', '보')
win = 0
lose = 0
draw = 0


class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)


def rock_paper_scissor():

    computer = random.choice(hands)
    player = request.args.get('hands')

    if player in (hands):
        if player == computer:
            return player, computer, 'draw'
        elif player == '가위':
            if computer == '바위':
                return player, computer, 'lose'
            else:
                return player, computer, 'win'
        elif player == '바위':
            if computer == '보':
                return player, computer, 'lose'
            else:
                return player, computer, 'win'
        elif player == '보':
            if computer == '가위':
                return player, computer, 'lose'
            else:
                return player, computer, 'win'
    else:
        return None


@app.route('/')
def home():
    user_choice = request.args.get('hands')
    if user_choice == None:
        db.session.query(GameHistory).delete()
        db.session.commit()
        return render_template('index.html')
    else:
        send_result = rock_paper_scissor()
        game = GameHistory(
            user_choice=send_result[0], computer_choice=send_result[1], result=send_result[2])
        db.session.add(game)
        db.session.commit()
    return render_template('index.html', data=send_result)


if __name__ == '__main__':
    app.run(debug=True)
