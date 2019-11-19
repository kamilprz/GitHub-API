from tmp import temp
import json
from github import Github

# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

sourceUser = "kamilprz"
targetUser = "gkoberger"

def main():
    source = g.get_user(sourceUser)
    target = g.get_user(targetUser)

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
    if lvl > 6:
        return -1
    # lvl odd so increment followers
    if lvl % 2 != 0:
        followers = [getFollowers(f) for f in list1]
        followers = [item for subl in followers for item in subl]
    # lvl even so increment following         
    else:
        following = [getFollowing(f) for f in list1]
        following = [item for subl in following for item in subl]


def getFollowers(user):
    followers = user.get_followers()
    return followers


def getFollowing(user):
    following = user.get_following()
    return following


def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 


main()
