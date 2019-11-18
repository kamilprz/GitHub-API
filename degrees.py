from tmp import temp
import json
from github import Github

# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

sourceUser = "neasatang"
targetUser = "YasirZardari"

def main():
    source = g.get_user(sourceUser)
    target = g.get_user(targetUser)

    srcFollowing = source.get_following()
    if target in srcFollowing:
        print("success : degree of separation is 1")
        # path : src -> tgt
    else:
        tgtFollowers = target.get_followers()
        n = intersection(srcFollowing, tgtFollowers)
        if n:
            print("success : degree of separation is 2")
            print(n)
            # path : src -> n -> tgt
        else:
            srcFollowing2 = [getFollowing(f) for f in srcFollowing]
            n = intersection(srcFollowing2, tgtFollowers)
            if n:
                print("success : degree of separation is 3")
                print(n)
                # path : src -> a -> n -> tgt
            else:
                tgtFollowers2 = [getFollowers(f) for f in tgtFollowers]
                n = intersection(srcFollowing2, tgtFollowers)
                if n:
                    print("success : degree of separation is 4")
                    print(n)
                    # path : src -> a -> n -> b -> tgt
                else:
                srcFollowing3 = [getFollowing(f) for f in srcFollowing2]
                n = intersection(srcFollowing3, tgtFollowers2)
                    if n:
                        print("success : degree of separation is 5")
                        print(n)
                        # path : src -> a -> b -> n -> c -> tgt
                    else:
                    tgtFollowers3 = [getFollowers(f) for f in tgtFollowers2]
                    n = intersection(srcFollowing3, tgtFollowers3)
                        if n:
                            print("success : degree of separation is 6")
                            print(n)
                            # path : src -> a -> b -> n -> c -> d -> tgt
                        


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
