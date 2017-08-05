from flask import Flask
from flask import render_template
import json
import os.path

app = Flask(__name__)
ROOT = os.path.realpath(os.path.dirname(__file__))
slug_dict = {}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/problems/<slug>')
def show_problem(slug):
    info = slug_dict[slug]
    description_file_name = str(info['id']).zfill(3) + '. ' + info['title'] + '.html'
    with open(os.path.join(ROOT, 'descriptions', description_file_name), 'r', encoding='utf-8') as f:
        description = f.read()
    return render_template('problem.html', description=description)


def init():
    with open(os.path.join(ROOT, 'problem_list.json'), 'r', encoding='utf-8') as f:
        content = json.loads(f.read())
    for item in content:
        slug_dict[item['stat']['question__title_slug']] = {
            'id': item['stat']['question_id'],
            'title': item['stat']['question__title']
        }


init()
if __name__ == '__main__':
    app.run()
