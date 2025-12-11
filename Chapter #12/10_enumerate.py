l = [3, 45, 58, 455]

# index = 0

# for item in l:
  
#     print(f"the item number at index {index} is {item}")
#     index += 1

#this can be simplified using enumerate funcation 

for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")