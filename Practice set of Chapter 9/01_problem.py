f = open("poem.txt")
c = f.read()

if "No man is an island" in c:

    print("the sentence is in the file... No man is an island")

else:
    
    print("the sentence is not in the file... ")

f.close()





