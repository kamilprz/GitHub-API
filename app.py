
from github import Github
from flask import Flask, request, render_template, jsonify
from collections import defaultdict, OrderedDict
import collections
import sys
import json

from get_json import repoAddress
from degrees import sourceUser, targetUser
 
app= Flask(__name__)

@app.route("/")
def index():
    graph = createFollowerGraph()
    return render_template("index.html", graph = graph, repo = repoAddress)


@app.route("/degrees")
def index2():
    graph = createPathGraph()
    return render_template("index2.html", graph = graph, repo = repoAddress, sourceUser = sourceUser, targetUser = targetUser)

def createFollowerGraph():
    followersGraph = readInFile('data.json')
    return followersGraph

def createPathGraph():
    pathGraph = readInFile('path.json')
    return pathGraph

def readInFile(fileName):
    with open(fileName) as json_file:
        return json.load(json_file)