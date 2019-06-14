# GitHub-project

Small python script for starting a Project on Github.  
I was fed up with repeating the same steps every time I wanted to work on a project, so I wrote this script.

# What it does?

 - Creates a new folder in a specified Project folder. I have a `Projects` folder in my Home folder, where I keep all my coding projects. Being tidy and all.  
 - Checks your GitHub repositories.
 - If the project already exists, it will be Cloned or Pulled.
 - If the repository doesn't exist, it will be created on GitHub and Cloned.
 - Visual Studio Code will start in the new Project folder.
 - Code away. :relaxed:
 
 # Installation
 
 - You need Python, of course. I used Python 3.7
 - Two extra packages: `pip install gitpython` , `pip install PyGithub`
 - Visit https://github.com/settings/tokens and generate a new Access Token. You only need access to repositories, nothing else.  
 - Copy the token and paste it into the `github.py`. Variables for customization purposes are on the top of the file.  
 - Or simply use `pip install -r requirements.txt`
 
 ## Optional for Linux based systems users.
 
  - The script will install `github` script to your local bin folder so you can run it from anywhere  
  `./install.sh <GiTHub Access Token>`
  - Or if you don't provide Token in argument it will prompt you for it.
  - You will be asked for a sudo password to access the `/usr/local/bin` folder.
  
  ## Troubleshoot. 
  - Change file attributes in case it's not marked as executable `chmod +x ./install.sh`
  

# Usage

`python github.py --all` or `-A` will list all your GitHub repositories.  
`python github.py --help` or `-H` will display very 'detailed help'.  

python github.py "project name"  
`python github.py my-newproject`  
Or with the bash file provided  
`github new-project`

Command `github` on it's own creates a new project with current timestamp. ie. `project-1560467353`


