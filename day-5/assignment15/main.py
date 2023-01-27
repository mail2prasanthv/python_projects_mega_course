# The variables defined inside a loop are available even ouside of the loop
todos =["Clean","Trash", "Laundry"]

for index, item in enumerate(todos):
    formattedString = f"{index}--{item}"#must start with f
    print(formattedString)
print("prints outside loop:" + formattedString);