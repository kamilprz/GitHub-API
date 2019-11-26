from tmp import temp
import json
from github import Github


# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

sourceUser = "kamilprz"
targetUser = "pioro"
targetUser = "jberesni"
targetUser = "felipebz" 
targetUser = "s-oravec" 
targetUser = "khailey"


def main():
    source = g.get_user(sourceUser)
    target = g.get_user(targetUser)

    lista = []

    path = (degreesOfSep([source], [target], 1, lista)[2])
    path = [source.login] + path + [target.login]
    
    # print(path)

    graphData = createGraphJson(path)
    with open('path.json', 'w') as outfile:
        json.dump(graphData, outfile)

    # srcFollowing = source.get_following()
    # for x in srcFollowing:
    #     print(x.login)
    # print("="*50)

    # srcFollowing2 = [getFollowing(f) for f in srcFollowing]
    # flat_list = [item for sublist in srcFollowing2 for item in sublist]
    # print(flat_list)
    # # srcFollowing3 = [getFollowing(f) for f in srcFollowing2]
    
    # check if source and target are in the contributors

def degreesOfSep(source, target, lvl, lista):
    if lvl > 6:
        return (-1, -1, -1)
    # lvl odd so increment followers
    if lvl % 2 == 0:
        compare = [getFollowers(f) for f in target]        
        #print("Followers - {} ".format(lvl))
        links = source
        compare = [item for subl in compare for item in subl]
    # lvl even so increment following         
    else:
        links = [getFollowing(f) for f in source]
        #print("Followingi - {} ".format(lvl))
        compare = target
        links = [item for subl in links for item in subl]
    
    #print("lista {} ".format(str(links)))
    #print("lista2 {}".format(str(list2)))

    n = intersection(links, compare)
    #print(n)
    if n:
        # take first of intersction
        first = n[0]
        # start a list
        lista = [first.login]
        # as intersection can return any of user
        # take a parent from list with parents
        # take child from a list with childs
        parent = links[links.index(first)]
        child = compare[compare.index(first)]

        # check if we are at begining of chain
        if hasattr(parent, "parent"):
            parent = parent.parent
        else:
            lista = []

        if hasattr(child, "child"):
            child = child.child
        else:
            lista = []
            
        return(parent, child, lista)
    (parent, child, lista) = degreesOfSep(links, compare, lvl+1, lista)
    if parent == -1:
        return -1
    #print("wyjscie")
    if lvl % 2 == 0:
        # if child is not end user - add child to list
        if ([child] != target):
            lista = lista + [child.login]
            child = child.child
        #print(child)
    else:
        # if parent is not start user - add parent to list
        if ([parent] != source):
            # lista = [links[links.index(parent)].login] + lista 
            # parent = links[links.index(parent)].parent
            lista = [parent.login] + lista
            parent = parent.parent
            
            
        #print(parent)
        
    return (parent, child, lista)


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


main()