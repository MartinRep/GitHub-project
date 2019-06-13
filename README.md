# GitHub-project

Small python script for starting a Project on Github.  
I was fed up with repeating the same steps every time I wanted to work on a project, so I wrote this script.

# What it does?

 - Creates a new folder in a specified Project folder. I have a `Projects` folder in my Home folder, where I keep all my coding projects. Being tidy and all.  
 - Checks your GitHub repositories, and if the project already exists, it will be cloned.
 - If the repository doesn't exist, it will be created.
 - Visual Studio Code will start in the new Project folder.
 - Code away. :relaxed:
 
 # Installation
 
 - You need Python, of course. I used Python 3.7
 - Two extra packages: `pip install gitpython` , `pip install PyGithub`
 - Visit https://github.com/settings/tokens and generate a new Access Token. You only need access to repositories, nothing else.  
 - Copy the token and paste it into the `github.py` and/or `github` script. Variables are on the top of the file.  
 - Or simply use `pip install -r requirements.txt`
 - Change your preferred Project folder and Code editor in the script. Variables are on the top.
 
 ## Optional for Linux based systems users.
 
  - Install to your local bin folder so you can run it anywhere `./install.sh`
  - You will be asked for a password to access the `/usr/local/bin` folder.
  - Change file attributes in case it's not marked as executable `chmod +x ./install.sh`
  

# Usage

python github.py "project name"  
`python github.py my-newproject`  
Or with the bash file provided  
`github new-project`


