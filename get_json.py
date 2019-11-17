from tmp import temp
from github import Github

# using username and password
password = temp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

repoAddress = "nating/cs-exams"

def main():
    repo = g.get_repo(repoAddress)
    contributorUsers = repo.get_contributors()
    # contributorNames = [getUserName(x) for x in repo.get_contributors()]

    for x in contributorUsers:
        followers = intersection(contributorUsers, x.get_followers())


def getFollowers(user):
    followers = {}
    index = 0
    for follower in user.get_followers():
        followers[str(index)] = follower
        index = index + 1
    return followers

def getUserName(user):
    username = user.login
    return username

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

main()
