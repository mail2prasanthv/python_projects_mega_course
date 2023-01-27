#Modify the list - 
#Converting string to int
#Access an item in the list based on the index.

todos = []

while True:
    user_action = input("Type show or add or edit:")
    match user_action:
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo);
        case "show":
            for item in todos:
                print(item )
        case "edit":
            posStr = input("Enter the position:")
            position = int(posStr);# converts to int
            position = position-1;# position 1 converts to index 0
            todo = input("Enter a todo:")
            todos[position]  =todo
        case "exit":
            break
        case _: #equivalent to default
            print("Unknown command:" )
            