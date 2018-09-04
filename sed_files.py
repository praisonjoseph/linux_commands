"""
Stage 1

Replace the word with another word using sed.

eg, sed 's/unix/linux/' file.txt

1. use argparse to get the arguments and store it as variables.
2. the second argument will be split with '/' and the first and second index will be used.
3. use re.sub(pattern, repl, string)

"""

import argparse
import re

def argument_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('searchpattern', help='provide the search and replace pattern, eg, s/unix/linux/')
    parser.add_argument( 'filename', help= "The file that should be searched")
    return parser.parse_args()

def read_write_file(args):
    with open(args.filename,) as f:
        data = f.read()
        # f.seek(0)
        new_data = substitution(data, args)
        # f.write(new_data)
        # f.truncate()
        return new_data

def substitution(content, args):
    sub_pattern = args.searchpattern.split('/')
    search_string, replace_string = sub_pattern[1], sub_pattern[2]
    
    return re.sub(search_string, replace_string, content)

print(read_write_file(argument_parsing()))