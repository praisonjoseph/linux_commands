import argparse

parser = argparse.ArgumentParser()
parser.add_argument("catfiles", metavar = 'cat', nargs = '+', help = "Display the output of files")
parser.add_argument("-n", "--line_number", action='store_true', help= "Displays the line number in front of each line")
args = parser.parse_args()
#print(args)
line_number = 1
for file in args.catfiles:
    with open(file) as f:
        for line in f.readlines():
            if args.line_number:
                print("\t{} \t{}".format(line_number,line), end='')
                line_number += 1
            else:
                print(line, end='')
            
