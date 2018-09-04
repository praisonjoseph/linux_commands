# Implement some of the features of find.
import argparse
from pathlib import Path
import sys
import subprocess

def find_type(dir, args):
    if not args.type in ['f', 'd']:
        print("Invalid argument for type. Use f for file and d for directory")
        sys.exit()
    for path in dir.rglob(args.name or '*'):
        if args.type == 'f' and path.is_file():
            print(path)
        elif args.type == 'd' and path.is_dir():
            print(path)

def find_name(dir, args):
    for path in dir.rglob(args.name):
        print(path)

def exec_find(dir, args):
    dir = dir / args.name
    obj = subprocess.run([args.exec, "dir + / + "], stdout=subprocess.PIPE)
    print(obj.stdout)

def arg_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", nargs='+', type=str, help="The directory that should be searched for")
    parser.add_argument("-name", type=str, help="The name of the file or files that should be searched")
    parser.add_argument("-type", type=str, help="Provide the type of data searched, f for file, d for directory")
    parser.add_argument("-exec", type=str)
    return parser.parse_args()

def find_file(args):
    dir = Path(args.dir[0])
    if args.name and args.exec:
        exec_find(dir, args)
        #print("I am in")
    if args.name and not args.type:
        find_name(dir, args)
    elif args.type:
        find_type(dir, args)
    else:
        print('You have to provide either of -name or -type')
        sys.exit()

find_file(arg_parsing())