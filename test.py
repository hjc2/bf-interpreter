
from brainfuck import interpret
import argparse

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("file", help="file", type=str)
args = parser.parse_args()
print(args.file)

with open(args.file) as f:
  code = " ".join([l.rstrip("\n") for l in f]) 

output = interpret(code)

print(output)