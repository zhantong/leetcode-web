from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import json
import os.path
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

app = Flask(__name__)
ROOT = os.path.realpath(os.path.dirname(__file__))
slug_dict = {}


@app.route('/')
def hello_world():
    return redirect('/problems')


@app.route('/problems')
def show_problem_list():
    problem_list = get_problem_list(slug_dict)
    return render_template('problems_summary.html', problem_list=problem_list)


@app.route('/problems/<slug>')
def show_problem(slug):
    info = slug_dict[slug]
    description_file_name = str(info['id']).zfill(3) + '. ' + info['title'] + '.html'
    file_path = os.path.join(ROOT, 'descriptions', description_file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            description = f.read()
    else:
        description = '收费题目'
    codes = get_codes(('python', 'java', 'c++'), info)
    title = str(info['id']) + '. ' + info['title']
    if 'X-PJAX' in request.headers:
        return render_template('problem_description.html', description=description, codes=codes, title=title,
                               id=info['id'])
    return render_template('problem.html', description=description, codes=codes,
                           problem_list=get_problem_list(slug_dict), title=title, id=info['id'])


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
        file_path = os.path.join(ROOT, 'leetcode', str(info['id']).zfill(3) + '. ' + info['title'], code_info[0],
                                 info['title'] + '.' + code_info[1])
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            code = highlight(f.read(), get_lexer_by_name(code_type), HtmlFormatter())
            codes.append((code_info[0], code))
    return codes


def get_problem_list(slug_dict):
    problem_list = []
    for key, value in slug_dict.items():
        problem_list.append({
            'id': value['id'],
            'url': '/problems/' + key,
            'name': str(value['id']).zfill(3) + '. ' + value['title']
        })
    problem_list.sort(key=lambda x: x['id'])
    return problem_list


init()
if __name__ == '__main__':
    app.run()
