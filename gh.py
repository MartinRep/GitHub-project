from github import Github
import git
import sys, time, os
from os.path import expanduser
import subprocess
import platform

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
    git_ssh_identity_file = os.path.expanduser('~/.ssh/id_rsa')
    git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file
    print("Checking if project repository alredy exists...")
    for repo in user.get_repos():
        # Local project files found
        if project_name == repo.name:
            with git.Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
                print("Repository {} alredy exist on Github. Just cloning the repo...".format(project_name))
                if os.path.isdir(project_path + "/.git"):
                    print("Repository folder already exist, Repository Pull initialized..")
                    git.Repo(project_name).remotes.origin.pull()
                else:
                    git.Repo.clone_from(repo.html_url, project_path)
                # Modify repository remote URL from https to ssh. This allows to use git push with RSA key (no need for password)
                origin = git.Repo(project_name).remotes.origin
                origin.config_writer.set("pushurl", "git@github.com:{}".format(repo.git_url[16:]))
                return
    print("Repository not found, creating a new one.")
    # Creates Repository on Github
    repo = user.create_repo(project_name)
    # Clone the repository into local folder
    git.Repo.clone_from(repo.html_url, project_path)
    # Modify repository remote URL from https to ssh. This allows to use git push with RSA key (no need for password)
    origin = git.Repo(project_name).remotes.origin
    origin.config_writer.set("pushurl", "git@github.com:{}".format(repo.git_url[16:]))

def github_getall():
    myGH = Github(GH_tokken) 
    user = myGH.get_user()
    for repo in user.get_repos():
        print(repo.name)

def github_commit():
    try:
        # Checking if git is installed.
        proc = subprocess.run(["git", "--version"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        if not "git version" in str(proc.stdout):
            raise Exception("git not found")
        message = ""
        for word in sys.argv[2:]:
            message = message + word + " "
        message = message[:-1]
        cur_dir = os.getcwd()
        if os.path.isdir(cur_dir + "/.git"):
            subprocess.run(["git", "add", cur_dir, "-A"])
            subprocess.run(["git", "commit", "-m", message])
            answer = input("Push Commit with message: \"{}\" ?[y/n]".format(message))
            if "y" in answer:
                subprocess.run(["git", "push"])
            else:
                subprocess.run(["git", "reset", "--soft", "HEAD^"])
        else:
            print("{} is not an Git folder".format(cur_dir))
    except Exception as e:
        print("! Something went wrong with git ! " + str(e))

def install():
    if "Linux" in platform.system():
        script_file = "gh"
    elif "Windows" in platform.system():
        script_file = "gh.py"
    script = open(script_file, "w")
    if "Linux" in platform.system():
        script.write("#!/usr/bin/env python3\n\n")
    with open(script_file) as f:
        line = f.readline()
        if "GH_tokken = \"Your Github Token\"" in line:
            line = "GH_tokken = \"{}\"".format(GH_tokken)
        elif "editor = \"code\"" in line and editor is not "":
            line = "editor = \"{}\"".format(editor)
        script.write(line)
    script.close()

    # gh=python C:\Users\Martin\Projects\GitHub-project\gh.py $*
    # subprocess.run("reg add \"HKCU\Software\Microsoft\Command Processor\" /v Autorun /d \"doskey /macrofile=\\\"c:\bat\macros.doskey\\\"\" /f")

def printout_help():
    print("Github repository tool.\n Creates or Clones GitHub project and start editor.\n Usage: github <project name>")
    print("     --help or -H for this very usefull help")
    print("     --all or -A to list all your GitHub repositories")
    print("     --push or -P <Commit message> This will create a new commit with message and push it to GitHub.")
    print("          Works with git repository of CURRENT WORKING FOLDER!")
    print("          Example: github -P This is my commit message. No quotations needed.")


def main():
    global project_path
    global editor
    global GH_tokken
    # Prints out small help info
    if "--help" in sys.argv or "-H" in sys.argv:
        printout_help()
        return
    # Install scirpt file OS dependent (Still in development)
    # elif "--install" in sys.argv[1] or "-I" in sys.argv[1]:
    #     if len(sys.arv) == 3:
    #         GH_tokken = sys.argv[2]
    #     if len(sys.argv) == 4:
    #         editor = sys.argv[3]
    #     install()
    #     return
    # Prints out all yours GitHub repositories
    elif "-all" in sys.argv or "-A" in sys.argv:
        print("Listing all your repositories...")
        github_getall()
        return
    elif "-P" in sys.argv or "--push" in sys.argv:
        github_commit()
        return
    elif len(sys.argv) > 1 and sys.argv[1].startswith("-"):
        print("Unknown command: {}\n".format(sys.argv[1]))
        printout_help()
        return
    # Pull current folder project from Github
    elif os.path.isdir(os.getcwd() + "/.git"):
        print("Repository folder found. Pull initialized..")
        git.Repo(os.getcwd()).remotes.origin.pull()
    elif len(sys.argv) > 1:
        project_name = sys.argv[1]
        project_path = projects_dir + project_name
        # Creates Project folder
        create_dir()
        # Deals with github repos
        github_repo(project_name)
    else:
        print('\x1b[6;30;41m' + "No project in current folder!" + '\x1b[0m')
        printout_help()
        return
    # Runs Visual Studio Code in the new Project folder
    print("Starting editor...")
    subprocess.run([editor, project_path])

if __name__ == "__main__":
    main()
