#Strong  password verification using Dictionary of boolean

password = input("Type a password:")
results = {}

#length Validation
if len(password)>=8:
    results["length-validation"] = True
else:
    results["length-validation"] = False

uppercase = False;
digit = False;
for eachchar in password:
    if eachchar.isupper():
        uppercase = True
    if eachchar.isdigit():
        digit = True

results["upper-validation"] = uppercase
results["digit-validation"] = digit

print ("Dictionary:",results)

if(all(results)== True): # check all the contents in the results list are True
    print("Strong Password")
else:
    print("Weak Password")


