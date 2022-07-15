
import codeop
from multiprocessing import parent_process
from re import I
import argparse

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("file", help="runs the file", type=str)
args = parser.parse_args()
print(args.file)


tape = [0] * 10

with open(args.file) as f:
  code = " ".join([l.rstrip("\n") for l in f]) 

index = 0
instruction = 0

print(tape)

while instruction < len(code):
    if(code[instruction] == "+"):
        tape[index] = tape[index] + 1
        instruction += 1
    
    elif(code[instruction] == "-"):
        tape[index] = tape[index] - 1
        instruction += 1

    elif(code[instruction] == ">"):
        index += 1
        instruction += 1

    elif(code[instruction] == "<"):
        index -= 1
        instruction += 1

    elif(code[instruction] == "."):
        print(chr(tape[index]))
        instruction += 1

    elif(code[instruction] == ","):
        tape[index] = int(input())
        instruction += 1

    elif(code[instruction] == "["):
        if(tape[index] == 0):
            paren = 1
            while paren > 0:
                instruction += 1
                if(code[instruction] == "]"):
                    paren -= 1
                elif(code[instruction] == "["):
                    paren += 1
            instruction += 1
        else:
            instruction += 1
    
    elif(code[instruction] == "]"):
        if(tape[index] != 0):
            paren = 1
            while paren > 0:
                instruction -= 1
                if(code[instruction] == "["):
                    paren -= 1
                if(code[instruction] == "]"):
                    paren += 1
        else:
            instruction += 1
            
    else:
        instruction += 1

print(tape)