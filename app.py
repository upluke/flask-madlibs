from copyreg import constructor
from stories import Story
from modulefinder import packagePathMap
from flask import Flask, request, render_template
import sys

app = Flask(__name__)
sys.path.append(".")

templates = ["""1 Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
             """2 Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
             """3 Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""]


@app.route('/')
def index():

    return render_template('home.html', templates=templates)


@app.route('/story')
def compose_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    print(request.args)
    selected_temp = request.args["selected_temp"]

    s = Story(["place", "noun", "verb", "adjective",
              "plural_noun"], selected_temp)
    text = s.generate({"place": place, "noun": noun, "verb": verb,
                      "adjective": adjective, "plural_noun": plural_noun})

    return render_template('story.html', text=text)
