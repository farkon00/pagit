# Pagit

Pagit is my project for exploring git and try to create git client in python. 

**WARNING**
This project is in realy early stage of development, everything may change. And not everything may be suported, git is really complex and has a lot of components and features in it, this project may not have any options for them or work not correctly, because of them. If it caused some damage to your repos, sorry.

# Usage 
`python <path_to_pagit>/pagit.py <command> <subcommand> [arguments]`

# Commands
## log
Takes from zero to one arguments. First argument is the number of commits to print, defaults to 2. 

Logs last n commits in the current repo.

## rm-all
Removes all tracked files from the repo. Doesn't take any arguments.

## object
Takes one argument, hash of the object.

Prints content of the object with a specfic hash.
