import argparse
'''
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", help= "increase output verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.square**2
print(args)
if args.verbose >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:  
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)


parser = argparse.ArgumentParser()
parser.add_argument('filenames', nargs = '+')
args = parser.parse_args()
print(args)
with open(args.filenames) as f:
    for line in f:
        print(line, end ='')

'''

parser = argparse.ArgumentParser()
parser.add_argument("--foo")
args = parser.parse_args()
print(args)
