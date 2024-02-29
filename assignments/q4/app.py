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

# 데이터베이스 구성


class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


# 가위바위보 함수, 플레이어/컴퓨터 의 손패 와 게임 결과를 반환


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
    # 반환된 값이 있을 때 와 없을 때 를 구분해서, 반환된 값이 없을 때는 데이터 베이스를 초기화
    # 반환된 값이 있을 경우에는 반환된 값으로 가위바위보 함수를 호출 하고 결과값을 데이터베이스에 저장 및 필요한 데이터 html로 넘기기
    user_choice = request.args.get('hands')
    if user_choice == None:
        db.session.query(GameHistory).delete()  # 데이터 베이스 전부 삭제
        db.session.commit()
        return render_template('index.html')
    else:
        send_result = rock_paper_scissor()
        game = GameHistory(
            user_choice=send_result[0], computer_choice=send_result[1], result=send_result[2])
        db.session.add(game)
        db.session.commit()
        # 데이터 베이스에 결과가 'win'인 값을 찾아서 count
        win = GameHistory.query.filter_by(result='win').count()
        # 데이터 베이스에 결과가 'lose'인 값을 찾아서 count
        lose = GameHistory.query.filter_by(result='lose').count()
        # 데이터 베이스에 결과가 'draw'인 값을 찾아서 count
        draw = GameHistory.query.filter_by(result='draw').count()
        list = GameHistory.query.all()  # 데이터 베이스에 모든 값을 리스트로 저장
    return render_template('index.html', data=send_result, win=win, lose=lose, draw=draw, list=list)


if __name__ == '__main__':
    app.run(debug=True)
