f = open("names.txt", "rt")

name = input("Enter search name:")
found = False
while True:
     line = f.readline()
     if line == "":  # EOF
         break
     if line.strip() == name:
         print("Found!")
         found = True
         break

if not found:
    print("Sorry! Name not found!")

f.close()
