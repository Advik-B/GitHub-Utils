__author__ = 'Advik-B' # advik.b@gmail.com

import os
import sys
import shutil
from termcolor import cprint

try:
    cwd = sys.argv[1]
except IndexError:
    cwd = os.getcwd()

if_allowed_files = os.path.isfile(os.path.join(cwd,'allowed-ext.txt'))
if_allowed_dirs = os.path.isdir(os.path.join(cwd,'.keep'))

instructions = """
steps:
    - create a file named 'allowed-ext.txt' in the current directory you can keep all the allowed extensions here
    - (optional) create a directory named '.keep' in the current directory and keep all the files you don't want to loose
    - run this script
optional:
    - you can also pass the path of the directory as an argument to the script
"""

if if_allowed_files == False:
    cprint('allowed-ext.txt NOT found in current directory.\
        \nPlease follow the below instructions before cleanup to avoid loss of files', 'red')
    for line in instructions.split('\n'):
        cprint(line, 'yellow')
    sys.exit(2)
elif if_allowed_files== True:
    cprint('Clean-up is starting.', 'green')
    