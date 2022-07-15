
import argparse
from ast import arg
import string

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("file", help="runs the file", type=str)
args = parser.parse_args()
print(args.file)


with open(args.file) as f:
  s = " ".join([l.rstrip("\n") for l in f]) 

print(s)
