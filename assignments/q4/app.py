import random
from flask import Flask, render_template, request
app = Flask(__name__)

hands = ('가위', '바위', '보')
win = 0
lose = 0
draw = 0


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
    send_result = rock_paper_scissor()
    return render_template('index.html', data=send_result)


if __name__ == '__main__':
    app.run(debug=True)
