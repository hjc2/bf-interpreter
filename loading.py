
with open('helloWorld.b') as f:
  s = " ".join([l.rstrip("\n") for l in f]) 

print(s)
