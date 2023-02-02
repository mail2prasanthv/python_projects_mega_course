#exeption handling
#continue statement
# exiting application

data = "data";

while True:
    user_input = input("Enter an option(1-indexOf, 2- conversion, 3 - exit):")
    if "1" in user_input:
        try:
            data[5]# produces IndexError
        except IndexError:
            print("Invalid usecase")
            continue
    if "2" in user_input:
        try:
            data[int("a")]# produces ValueError
        except ValueError:
            print("Invalid usecase")
            continue
    else:
        exit("Invalid option. Exiting the application.")
        
        
        