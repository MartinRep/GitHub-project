from github import Github
import git
import sys, time, os
from os.path import expanduser
import subprocess

# GitHub access token
GH_tokken = "Your Github Token" # Get your own from https://github.com/settings/tokens

# Your favourite text editor. Default is Visual Studio code
editor = "code"

# Gets current user's home directory and concat "Projects" to it. ! Change it to your liking !
projects_dir =  expanduser("~") + "/Projects/"
project_path = projects_dir

def create_dir():
    if not os.path.isdir(projects_dir):
        print("Creating Projects folder.")
        os.makedirs(projects_dir)
    if not os.path.isdir(project_path):        
        os.makedirs(project_path)
        print("Folder {} created.".format(project_path))
 
def github_repo(project_name):
    os.chdir(projects_dir)
    myGH = Github(GH_tokken) 
    user = myGH.get_user()
    print("Checking if project repository alredy exists...")
    for repo in user.get_repos():
        # Local project files found
        if project_name == repo.name:
            print("Repository {} alredy exist on Github. Just cloning the repo...".format(project_name))
            if os.path.isdir(project_path + "/.git"):
                print("Repository folder already exist, Repository Pull initialized..")
                git.Repo(project_name).remotes.origin.pull()
                origin = git.Repo(project_name).remotes.origin
                # Modify repository remote URL from https to ssh. This allows to use git push with RSA key (no need for password)
                origin.config_writer.set("pushurl", "git@github.com:{}".format(repo.git_url[16:]))
                return
            git.Repo.clone_from(repo.html_url, project_path)
            # Modify repository remote URL from https to ssh. This allows to use git push with RSA key (no need for password)
            origin.config_writer.set("pushurl", "git@github.com:{}".format(repo.git_url[16:]))
            return
    print("Repository not found, creating a new one.")
    repo = user.create_repo(project_name)
    git.Repo.clone_from(repo.html_url, project_path)

def github_getall():
    myGH = Github(GH_tokken) 
    user = myGH.get_user()
    for repo in user.get_repos():
        print(repo.name)

def printout_help():
    print("Github repository tool.\n Creates or Clones GitHub project and start editor.\n github <project name>")
    print("--help or -H for this very usefull help")
    print("--all or -A to list all your GitHub repositories")


def main():
    global project_path
    # Prints out small help info
    if "--help" in sys.argv or "-H" in sys.argv:
        printout_help()
        return
    # Prints out all yours GitHub repositories
    elif "-all" in sys.argv or "-A" in sys.argv:
        print("Listing all your repositories...")
        github_getall()
        return
    elif sys.argv[1].startswith("-") or sys.argv[1].startswith("--"):
        print("Unknown command: {}\n".format(sys.argv[1]))
        printout_help()
        return
    # Create a new project with Generated name
    elif len(sys.argv) is 1:
        project_name = "project-" + str(int(time.time()))
        print("Generating a new Project with name: {}".format(project_name))
    else:
        project_name = sys.argv[1]
    project_path = projects_dir + project_name
    # Creates Project folder
    create_dir()
    # Deals with github repos
    github_repo(project_name)
    # Runs Visual Studio Code in the new Project folder
    print("Starting editor...")
    subprocess.run([editor, project_path])


if __name__ == "__main__":
    main()
