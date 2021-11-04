__author__ = 'Advik-B' # advik.b@gmail.com

import os
import sys
from send2trash import send2trash as delete
from termcolor import cprint
from fnmatch import fnmatch

DEL = False

try:
    cwd = sys.argv[1]
except IndexError:
    cwd = os.getcwd()

if_allowed_files = os.path.isfile(os.path.join(cwd,'allowed-ext.txt'))
if_allowed_dirs = os.path.isdir(os.path.join(cwd,'.keep'))

instructions = """
steps:
    - create a file named 'allowed-ext.txt' in the current directory you can keep all the allowed extensions here
    - run this script
optional:
    - you can also pass the path of the directory as an argument to the script
"""

endmsg = """
if I deleted some important files, you can find them in the trash-folder/bin.
also next time make sure you have the 'allowed-ext.txt' file in the current directory. and all the white-listed extensions in it.
"""

if if_allowed_files == False:
    cprint('allowed-ext.txt NOT found in current directory.\
        \nPlease follow the below instructions before cleanup to avoid loss of files', 'red')
    for line in instructions.split('\n'):
        cprint(line, 'yellow')
    sys.exit(2)
elif if_allowed_files== True:
    cprint('Clean-up is starting.', 'green')
    allowed_ext = ['*.md', '*.txt'] # list of allowed extensions
    allowed_fil = []
    
    with open(os.path.join(cwd,'allowed-ext.txt'), 'r') as f:
        for line in f:
            allowed_ext.append(line.strip())
        for path, subdirs, files in os.walk(cwd):
            for name in files:
                for pattern in allowed_ext:
                    if fnmatch(name.casefold(), pattern) or '.git' in os.path.join(path, name) or '.vscode' in os.path.join(path, name):
                        allowed_fil.append(os.path.join(path, name))

    for path, subdirs, files in os.walk(cwd):
        for name in files:
            if fnmatch(name, '*.*') and os.path.join(path, name) not in allowed_fil:
                pth = os.path.join(path, name)
                cprint('Deleting: '+pth, color='cyan')
                delete(pth)
                DEL = True
    cprint('Clean-up is done.', 'green')
    if DEL == True:
        for line in endmsg.split('\n'):
            cprint(line, 'yellow')