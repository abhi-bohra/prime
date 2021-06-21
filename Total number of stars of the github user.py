#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import base64
from github import Github
from pprint import pprint

username = "chowmean"

g = Github()

user = g.get_user(username)
l = []
def print_repo(repo):

    repo.full_name
    
    repo.stargazers_count
    a = repo.stargazers_count
    l.append(a)
    
    
for repo in user.get_repos():
    print_repo(repo)
    
Sum = sum(l)
print('Total number of stars of the user:', Sum)

