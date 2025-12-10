def main():
 try:
   a = int(input("hey, Enter a number:"))
   print(a)

 except Exception as e:
   print(e)


 finally:
   print("hey, i am in side the finally")

main()

