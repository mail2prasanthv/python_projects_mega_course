# format string using f-string
#As of Python 3.6, f-strings are a great new way to format strings. 
#Not only are they more readable, more concise, and less prone to error 
#than other ways of formatting, but they are also faster!

todos =["Clean","Trash", "Laundry"]

for index, item in enumerate(todos):
    formattedString = f"{index}--{item}"#must start with f
    print(formattedString)