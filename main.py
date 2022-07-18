from typing import Dict, Any

from flask import Flask, render_template, request
import utils

app = Flask(__name__)

# Вывод на главную страницу"""
@app.route("/")
def page_index():
    list_candidates = utils.load_candidates('candidates.json')
    return render_template('list.html', list_cand=list_candidates)


#Вывод на страницу кандидата по номеру
@app.route("/candidates/<int:id>")
def page_candidate(id):
   single_candidate = utils.get_by_id(id)
   return render_template('single.html', candidate=single_candidate)


#Вывод на страницу кандидата по имени
@app.route("/search/<candidate_name>")
def page_search(candidate_name):
   candidate_by_name = utils.get_by_name(candidate_name)
   return render_template('search.html', candidate=candidate_by_name)


#Вывод на страницу кандидатов с навыками
@app.route("/skills/<skill_name>")
def page_skills(skill_name):
   candidate_by_skill = utils.get_by_skill(skill_name)
   return render_template('skill.html', candidates_by_skill=candidate_by_skill)


app.run(port=8000, debug=True)
