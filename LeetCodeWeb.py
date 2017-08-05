from flask import Flask
from flask import render_template
import json
import os.path
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

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
    codes = get_codes(('python', 'java', 'c++'), info)
    return render_template('problem.html', description=description, codes=codes)


def init():
    with open(os.path.join(ROOT, 'problem_list.json'), 'r', encoding='utf-8') as f:
        content = json.loads(f.read())
    for item in content:
        slug_dict[item['stat']['question__title_slug']] = {
            'id': item['stat']['question_id'],
            'title': item['stat']['question__title']
        }


def get_codes(code_types, info):
    code_infos = {
        'java': ('Java', 'java'),
        'python': ('Python', 'py'),
        'c++': ('C++', 'cpp')
    }
    codes = []
    for code_type in code_types:
        code_info = code_infos[code_type]
        with open(os.path.join(ROOT, 'leetcode', str(info['id']).zfill(3) + '. ' + info['title'], code_info[0],
                               info['title'] + '.' + code_info[1]), 'r', encoding='utf-8') as f:
            python_code = highlight(f.read(), PythonLexer(), HtmlFormatter())
            codes.append(python_code)
    return codes


init()
if __name__ == '__main__':
    app.run()
