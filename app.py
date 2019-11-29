
from github import Github
from flask import Flask, request, render_template, jsonify
from collections import defaultdict, OrderedDict
import collections
import sys
import json

from get_json import*
from degrees import*
 
app= Flask(__name__)

@app.route("/")
def index():
    return render_template("homePage.html")


@app.route("/degrees", methods=['POST'])
def index2():
    source = request.form['source']
    target = request.form['target']
    repoAddress = request.form['repoAddress']
    result = generateDegrees(source, target, repoAddress)
    # error 1
    if result == -1:
        return render_template("degreesError.html", repo = repoAddress, error = "At least one of the users is not a contributor to this repository.")
    # error 2
    elif result == -2:
       return render_template("degreesError.html", repo = repoAddress, error = "The degree of separation is over 6.")
    else:
        graph = createPathGraph()
        return render_template("degreesPage.html", graph = graph, repo = repoAddress, sourceUser = source, targetUser = target)


@app.route("/repo", methods=['POST'])
def index3():
    repoAddress = request.form['repoAddress']
    generateFollowers(repoAddress)
    graph = createFollowerGraph()
    return render_template("contributorsPage.html", graph = graph, repo = repoAddress)


def createFollowerGraph():
    followersGraph = readInFile('data.json')
    return followersGraph

def createPathGraph():
    pathGraph = readInFile('path.json')
    return pathGraph

def readInFile(fileName):
    with open(fileName) as json_file:
        return json.load(json_file)