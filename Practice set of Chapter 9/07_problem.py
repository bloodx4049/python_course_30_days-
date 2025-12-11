
with open("log.txt") as f:
  lines = f.readlines()

lineno = 1
found = False
for line in lines:
  if "python" in line:
    print(f"yes python is present. line no:{lineno}")
    found = True
    break
  lineno += 1
   
else:
  print("no python is not present")