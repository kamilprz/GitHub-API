
from github import Github
from flask import Flask, request, render_template, jsonify
from collections import defaultdict, OrderedDict
import collections
import sys
import json
 
app= Flask(__name__)

@app.route("/")
def index():
    graph = createFollowerGraph()
    render_template("index.html", graph = graph)

def createFollowerGraph():
    followersGraph = readInFile('graph.json')


def readInFile(fileName):
    with open(fileName) as json_file:
        return json.load(json_file)