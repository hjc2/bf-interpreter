
from brainfuck import interpret

code = "++++++++++[>+++++abcd++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."

output = interpret(code)

print(output)