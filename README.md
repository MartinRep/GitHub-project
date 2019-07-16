# GitHub-project

A small Python based tool for working with projects on Github.  
I was fed up with repeating the same steps every time I wanted to work on a project, so I wrote this script.  
It's a terminal abstraction for GitHub.  

# What it does?

 - Creates a new folder in a specified Project folder. I have a `Projects` folder in my Home folder, where I keep all my coding projects. Being tidy and all.  
 - Checks your GitHub repositories.
 - If the project already exists, it will be Cloned or Pulled.
 - If the repository doesn't exist, it will be created on GitHub and Cloned.
 - Visual Studio Code will start in the new Project folder.
 - Code away. :relaxed:
 - Also it makes commits easier.
 
 # Installation
 
 - Visit https://github.com/settings/tokens and generate a new Access Token. You only need access to repositories, nothing else.  
 - You need Python, of course. I used Python 3.7
 - Two extra packages: `pip install gitpython` , `pip install PyGithub`
 - Or simply use `pip install -r requirements.txt`
 - Copy the token and paste it into the `gh.py`. Variables for customization purposes are on the top of the file.  
 
 ## Linux based systems (Optional, but Recommended)
 
  - The script will install `github` script to your local bin folder so you can run it from anywhere  
  `./install.sh <GiTHub Access Token>`
  - Or if you don't provide Token in argument it will prompt you for it.
  - You will be asked for a sudo password to access the `/usr/local/bin` folder.
  - Now simply use `gh <command>` from any folder instead `python gh.py <command>`.
  
  ### Troubleshoot 
  - Change file attributes in case it's not marked as executable `chmod +x ./install.sh`
  

# Usage

python gh.py "project name"  
`python gh.py my-newproject`    

`python gh.py --all` or `-A` will list all your GitHub repositories.  

`python gh.py --help` or `-H` will display very 'detailed help'.  

`python gh.py -push` or `-P` followed by message will add all new file in the git folder to commit, attach message and push to GitHub. `github -P Commit message, no need for quotation marks.`  

`python gh.py` on it's own will do `git pull` for the Project in the current working directory.  
