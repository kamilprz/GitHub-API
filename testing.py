
from github import Github

# using username and password
g = Github("kamilprz", "password")

for repo in g.get_user().get_repos():
    print(repo.name)


