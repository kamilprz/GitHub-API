from tmp import temp
import json
from github import Github


# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

sourceUser = "henrym2"
targetUser = "sasunts"

def main():
    source = g.get_user(sourceUser)
    target = g.get_user(targetUser)

    print(degreesOfSep([source], [target], 1))

    # srcFollowing = source.get_following()
    # for x in srcFollowing:
    #     print(x.login)
    # print("="*50)

    # srcFollowing2 = [getFollowing(f) for f in srcFollowing]
    # flat_list = [item for sublist in srcFollowing2 for item in sublist]
    # print(flat_list)
    # # srcFollowing3 = [getFollowing(f) for f in srcFollowing2]
    
    # check if source and target are in the contributors

def degreesOfSep(list1, list2, lvl):
    if lvl > 3:
        return -1
    # lvl even so increment followers
    if lvl % 2 == 0:
        links = [getFollowers(f) for f in list1]        
        print("Followers - {} ".format(lvl))
    # lvl odd so increment following         
    else:
        links = [getFollowing(f) for f in list1]
        print("Followingi - {} ".format(lvl))

    links = [item for subl in links for item in subl]

    n = intersection(links, list2)
    #print(n)
    if n:
        return(lvl, n)
    return degreesOfSep(list2, links, lvl+1)


def getFollowers(user):
    followers = user.get_followers()
    return followers


def getFollowing(user):
    following = user.get_following()
    return following


def intersection(lst1, lst2): 
    lst3 = set.intersection(set(lst1), set(lst2)) 
    return list(lst3) 


main()
