# from flask import Flask, render_template
# from utils import load_candidates_from_json, get_candidates_by_name
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def all_condidates():
#     a = get_candidates_by_name(load_candidates_from_json())
#     return render_template('card.html', a=a)
#
#
# app.run(host='0.0.0.0', port=8000)


from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def page_main():
    candidates = get_names(load_candidates_from_json())
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>")
def page_candidate(id):
    candidate = get_candidate(id)
    return render_template('single.html', user=candidate)


@app.route('/search/<candidate_name>')
def page_name(candidate_name):
    candidate = get_candidates_by_name(candidate_name)
    return render_template('search.html', user=candidate)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidates = get_names(get_candidates_by_skill(skill_name))
    quantity = int(len(candidates))
    return render_template("skill.html", quantity=quantity, candidates=candidates)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)