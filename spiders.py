import json
from dictionary import coolwords
from random import choice, randint

from flask import Flask, request, g, render_template

# config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    words = []
    for i in xrange(0, randint(33, 133)):
        words.append({
            'word': [choice(coolwords), choice(coolwords)]
        })

    g.words = words

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html', words=g.words)


if __name__ == '__main__':
    app.run()
