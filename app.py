from modulefinder import packagePathMap
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('home.html')


@app.route('/story')
def compose_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    return render_template('story.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
