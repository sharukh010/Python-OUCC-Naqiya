name = input("Name: ")

if name.replace(" ","").isalpha(): 
    print("Valid")
else: 
    print("Invalid")