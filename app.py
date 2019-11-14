
from github import Github
from flask import Flask, request, render_template, jsonify
from collections import defaultdict, OrderedDict
import collections
import sys
import json
 
app= Flask(__name__)

@app.route("/")
def index():
    # createFollowerGraph()
    # return render_template("index.html")
    return '<h1>Hello!</h1>'


def createFollowerGraph():
    followersGraph = readInFile('graph.json')


def readInFile(fileName):
    with open(fileName) as json_file:
        return json.load(json_file)