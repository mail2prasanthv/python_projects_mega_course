#switch case equivalent

todos = []

while True:
    user_action = input("Type show or add:")
    match user_action:
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo);
        case "show":
            print(todos)
        case exit:
            break
