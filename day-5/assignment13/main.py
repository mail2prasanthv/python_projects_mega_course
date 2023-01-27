#enumerate in for loop
#It is the option to get both index and item at the same time.

todos =["Clean","Trash", "Laundry"]

for index, item in enumerate(todos):
    print(index,"-", item)