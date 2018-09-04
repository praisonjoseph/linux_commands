'''
Todo
1. Two positional arguments
    a. string to be search. This will be passwed to regex search function
    b. The location it should be searched. This will be a directory, list of files or glob of files

Initial implementation
1. grep help *.text 
    position arguments help and searchloc
2. Rearrange to function groups
3. Implement grep help *
    Loop through each location elements for each file.

4. Implement -r for recursive directories and change the input location as a directory.
    a. Implement grep -r help <directory>

    b. Implement grep -r help <file>
5. Implement-i for case sensitive search.# Need to figure out how to use flags with conditions
'''
import argparse
from pathlib import Path
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("search", metavar = "searchstring", type=str)
    parser.add_argument("location", type=str, nargs = '+')
    parser.add_argument("-r", "--recursive", action= 'store_true')
    #parser.add_argument("-i", "--case", action='store_true')
    return parser.parse_args()

def search_string_in_file(path, args):
    with open(path) as fo:
        for line in fo.readlines():
            searchstring = re.search(args.search, line)
            if searchstring:
                print(f"{path}:\t{line}", end='')

def path_traverse(args):
    print(args)
    p = Path(args.location[0])
    dir = p if p.is_dir() else Path('.') 
    glob = dir.rglob if args.recursive else dir.glob
    for file in args.location:
        for path in dir.glob(file):
            if path.is_file():
                search_string_in_file(path, args)
path_traverse(parse_args())




