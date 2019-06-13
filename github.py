
from github import Github
import git
import sys, time, os
from os.path import expanduser
import subprocess

# GitHub access token
GH_tokken = "Your GitHub Access Tokken" # Get your own from https://github.com/settings/tokens

# Your favourite text editor. Default is Visual Studio code
editor = "code"

# Gets current user's home directory and concat "Projects" to it. ! Change it to your liking !
projects_dir =  expanduser("~") + "/Projects/"


def create_dir(project_path):
    if not os.path.isdir(projects_dir):
        print("Creating Projects folder.")
        os.makedirs(projects_dir)
    if not os.path.isdir(project_path):        
        os.makedirs(project_path)
    print("Folder {} created.".format(project_path))
 
def create_github_repo(project_name):
    myGH = Github(GH_tokken) 
    user = myGH.get_user()
    print("Checking if project repository alredy exists...")
    for repo in user.get_repos():
        if project_name == repo.name:
            print("Repository {} alredy exist on Github. Just cloning the repo...")
            return repo.html_url
    print("Repository not found, creating a new one.")
    repo = user.create_repo(project_name)
    return repo.html_url

def main():
    if len(sys.argv) is 1:
        project_name = "project-" + str(int(time.time()))
    else:
        project_name = sys.argv[1]

    project = projects_dir + project_name
    # Creates Project folder
    create_dir(project)
    # Creates new repository on Github.com and clones it into the folder
    git.Repo.clone_from(create_github_repo(project_name), project)
    # Runs Visual Studio Code in the new Project folder
    print("Starting editor...")
    subprocess.run([editor, project])


if __name__ == "__main__":
    main()