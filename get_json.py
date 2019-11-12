import tmp
from github import Github

# using username and password
password = tmp.getPass()
g = Github("kamilprz", password)
user = g.get_user()

def main():
  followers = getFollowers(user)
  print(followers[0].get_followers())

def getFollowers(user):
    followers = []
    for follower in user.get_followers():
        followers.append(follower)
    return followers

main()
