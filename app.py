from flask import Flask, render_template, request
from test import get_questions, get_result

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answers = []
        for i in range(1, 58):
            answers.append(request.form['quest%s' % str(i).zfill(2)])

        return render_template('results.html', results=get_result(answers))

    return render_template('home.html', questions=get_questions())


if __name__ == '__main__':
    app.secret_key = 'Aizenka App Key'
    app.run()
