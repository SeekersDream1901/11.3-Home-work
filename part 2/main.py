from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = load_candidates_from_json()
    candidates = render_template("list.html", candidates=candidates)
    return candidates


@app.route('/candidate/<int:id>')
def get_candidate_by_identification(id):
    candidate = get_candidate_by_id(id)

    candidate_name = candidate['name']
    candidate_position = candidate['position']
    candidate_picture = candidate['picture']
    candidate_skills = candidate['skills']

    candidate = render_template("single.html",
                                name=candidate_name,
                                position=candidate_position,
                                picture=candidate_picture,
                                skills=candidate_skills)
    return candidate


@app.route('/search/<candidate_name>')
def get_candidate_by_name(candidate_name):
    count, candidates = get_candidates_by_name(candidate_name)

    candidates = render_template("search.html",
                                 count=count,
                                 candidates=candidates)
    return candidates


@app.route("/skill/<skill_name>")
def get_candidate_by_skill(skill_name):
    count, candidates = get_candidates_by_skill(skill_name)
    skill = skill_name

    candidates = render_template("skill.html",
                                 skill=skill,
                                 count=count,
                                 candidates=candidates)
    return candidates


app.run(host='0.0.0.0', port=8000)
