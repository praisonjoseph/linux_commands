import argparse

parser = argparse.ArgumentParser()
parser.add_argument("something")
parser.add_argument("-v", "--verbose", help="Adds verbose information", action="store_true")
parser.add_argument("-u", "--unicode", help="It takes unicode strings", action="store_true")
parser.add_argument("-w", "--write", help="Write the output to file", action="store_true")
parser.add_argument("-p", "--path", help="Add the path of the file")
parser.add_argument("-s", "--speed", help="How fast should it run", type=int)
parser.add_argument("-b", "--byte", help="The numbers of bytes processed per sec", type=int)
parser.add_argument("-n", "--no", help="The numbers of bytes processed per sec", type=int)
args = parser.parse_args()
print(args)