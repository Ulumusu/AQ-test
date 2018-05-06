from flask import Flask, request, redirect, url_for, flash
from flask import render_template
from questionAndAnswers import *

app = Flask(__name__)

app.config.update(dict(SECRET_KEY='123'))


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        points = 0
        answers = request.form

        for numQ, youanswer in answers.items():
            if youanswer == Q_and_A[int(numQ)]['good_answer']:
                points += 1

        flash('Liczba punktów: {0}'.format(points))
        return redirect(url_for('index'))


    return render_template('index.html', questions=Q_and_A)


if __name__ == '__main__':
    app.run(debug=True)
