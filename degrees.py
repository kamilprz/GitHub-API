from tmp import temp
import json
from github import Github


# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

def generateDegrees(sourceUser, targetUser, repoAddress):
    source = g.get_user(sourceUser)
    target = g.get_user(targetUser)

    contributors = g.get_repo(repoAddress).get_contributors()
    # if source or target not in contributors
    if (source not in contributors) or (target not in contributors):
        return -1

    path = []

    answer = (degreesOfSep([source], [target], 1, path))
    # if degree of sep > 6
    if answer == (-1, -1, -1):
        return -2

    path = answer[2]
    path = [source.login] + path + [target.login]

    graphData = createGraphJson(path)
    with open('path.json', 'w') as outfile:
        json.dump(graphData, outfile)


def degreesOfSep(source, target, lvl, path):
    if lvl > 6:
        return (-1, -1, -1)
    # lvl odd so increment followers
    if lvl % 2 == 0:
        compare = [getFollowers(f) for f in target]        
        links = source
        compare = [item for subl in compare for item in subl]
    # lvl even so increment following         
    else:
        links = [getFollowing(f) for f in source]
        compare = target
        links = [item for subl in links for item in subl]
    

    n = intersection(links, compare)
    if n:
        # take first of intersction
        first = n[0]
        # start a list
        path = [first.login]
        # as intersection can return any of user
        # take a parent from list with parents
        # take child from a list with childs
        parent = links[links.index(first)]
        child = compare[compare.index(first)]

        # check if we are at begining of chain
        if hasattr(parent, "parent"):
            parent = parent.parent
        else:
            path = []

        if hasattr(child, "child"):
            child = child.child
        else:
            path = []
            
        return(parent, child, path)
    (parent, child, path) = degreesOfSep(links, compare, lvl+1, path)
    if parent == -1:
        return (-1, -1, -1)
    if lvl % 2 == 0:
        # if child is not end user - add child to list
        if ([child] != target):
            path = path + [child.login]
            child = child.child
    else:
        # if parent is not start user - add parent to list
        if ([parent] != source):
            path = [parent.login] + path
            parent = parent.parent
            
    return (parent, child, path)


def getFollowers(user):
    followers = user.get_followers()
    for i in followers:
        i.child = user
    return followers


def getFollowing(user):
    following = user.get_following()
    for i in following:
        i.parent = user
    return following


def intersection(lst1, lst2): 
    lst3 = set.intersection(set(lst1), set(lst2)) 
    return list(lst3) 


def createGraphJson(path):
    graphData = {}
    graphData["nodes"] = []
    graphData["links"] = []

    for user in path:
        graphData["nodes"].append({
            'name' : user,
            'id' : path.index(user)
        })
        
    for i in range(len(path) - 1):
        graphData["links"].append({
        'source' : i,
        'target' : i+1
        })

    return graphData

