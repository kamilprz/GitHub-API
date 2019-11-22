from tmp import temp
import json
from github import Github


# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

sourceUser = "henrym2"
targetUser = "s-oravec"


def main():
    source = g.get_user(sourceUser)
    target = g.get_user(targetUser)

    lista = []

    print(degreesOfSep([source], [target], 1, lista))

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
    if lvl > 4:
        return -1
    # lvl odd so increment followers
    if lvl % 2 == 0:
        compare = [getFollowers(f) for f in target]        
        print("Followers - {} ".format(lvl))
        links = source
        compare = [item for subl in compare for item in subl]
    # lvl even so increment following         
    else:
        links = [getFollowing(f) for f in source]
        print("Followingi - {} ".format(lvl))
        compare = target
        links = [item for subl in links for item in subl]
    
    #print("lista {} ".format(str(links)))
    #print("lista2 {}".format(str(list2)))

    n = intersection(links, compare)
    print(n)
    if n:
        first = n[0]
        parent = links[links.index(first)].parent
        lista = []
        return(parent, first, lista)
    (parent, child, lista) = degreesOfSep(links, compare, lvl+1, lista)
    print("wyjscie")
    if lvl % 2 == 0:
        print(compare.index(child))
        lista =  lista + [compare[compare.index(child)].login]
        child = compare[compare.index(child)].child
        print(child)
    else:
        print(links.index(parent))
        lista = [links[links.index(parent)].login] + lista 
        parent = links[links.index(parent)].parent
        print(parent)
        
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


main()