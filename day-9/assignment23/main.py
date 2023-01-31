#Strong  password verification using list of boolean

password = input("Type a password:")
results = []

#length Validation
if len(password)>=8:
    results.append(True)
else:
    results.append(False)

uppercase = False;
digit = False;
for eachchar in password:
    if eachchar.isupper():
        uppercase = True
    if eachchar.isdigit():
        digit = True

results.append(uppercase)
results.append(digit)

print ("Dictionary:",results)

if(all(results)== True): # check all the contents in the results list are True
    print("Strong Password")
else:
    print("Weak Password")


