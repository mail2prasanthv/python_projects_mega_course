
while True:
    userInput = input("Enter your option (read or write)")
    
    match userInput:
        case "read":
            fileread = open("test.txt","r")
            contents = fileread.readlines();
            fileread.close()
            print("contents:",contents)
            
        case "write":
            data = input("Enter text to be written:")
            fileWrite = open("test.txt","w")
            contents = fileWrite.writelines(data)
            fileWrite.close()
            