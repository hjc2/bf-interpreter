

def interpret(code):

    tape = [0] * 30000

    index = 0
    instruction = 0

    output = ""

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
            #print(chr(tape[index]))
            output += chr(tape[index])
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
    return(output)
