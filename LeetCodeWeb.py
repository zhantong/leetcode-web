from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import g
import os.path
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import sqlite3

app = Flask(__name__)
ROOT = os.path.realpath(os.path.dirname(__file__))

DATABASE = 'leetcode.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/')
def hello_world():
    return redirect('/problems')


@app.route('/problems')
def show_problem_list():
    problem_list = get_problem_list()
    return render_template('problems_summary.html', problem_list=problem_list)


@app.route('/problems/<slug>')
def show_problem(slug):
    c = get_db().cursor()
    c.execute('SELECT id,title FROM problem WHERE slug=?', (slug,))
    id, title = c.fetchone()
    description_file_name = str(id).zfill(3) + '. ' + title + '.html'
    file_path = os.path.join(ROOT, 'descriptions', description_file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            description = f.read()
    else:
        description = '收费题目'
    codes = get_codes(('python', 'java', 'c++'), id, title)
    title = str(id) + '. ' + title
    if 'X-PJAX' in request.headers:
        return render_template('problem_description.html', description=description, codes=codes, title=title,
                               id=id)
    return render_template('problem.html', description=description, codes=codes,
                           problem_list=get_problem_list(), title=title, id=id)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def get_codes(code_types, id, title):
    code_infos = {
        'java': ('Java', 'java'),
        'python': ('Python', 'py'),
        'c++': ('C++', 'cpp')
    }
    codes = []
    for code_type in code_types:
        code_info = code_infos[code_type]
        file_path = os.path.join(ROOT, 'submissions', str(id).zfill(3) + '. ' + title, code_info[0],
                                 'Solution.' + code_info[1])
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            code = highlight(f.read(), get_lexer_by_name(code_type), HtmlFormatter())
            codes.append((code_info[0], code))
    return codes


def get_problem_list():
    problem_list = []
    c = get_db().cursor()
    for id, title, slug in c.execute('SELECT id,title,slug FROM problem ORDER BY id'):
        problem_list.append({
            'id': id,
            'url': '/problems/' + slug,
            'name': str(id).zfill(3) + '. ' + title
        })
    return problem_list


if __name__ == '__main__':
    app.run()
