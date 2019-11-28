from tmp import temp
import json
from github import Github

# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

# repoAddress = "nating/cs-exams"

def generateFollowers(repoAddress):
    repo = g.get_repo(repoAddress)
    contributorUsers = repo.get_contributors()
    contributorNames = [getUserName(x) for x in repo.get_contributors()]
    graphData = {}
    graphData["nodes"] = []
    graphData["links"] = []

    for x in contributorUsers:
        followers = intersection(contributorUsers, x.get_followers())
        graphData["nodes"].append({
            'name' : x.login,
            'id' : contributorNames.index(x.login)
        })
        
        for f in followers:
           graphData["links"].append({
            'source' : contributorNames.index(f.login),
            'target' : contributorNames.index(x.login)
        }) 

    with open('data.json', 'w') as outfile:
        json.dump(graphData, outfile)


def getUserName(user):
    username = user.login
    return username

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
