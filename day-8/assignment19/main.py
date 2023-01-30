#read and write file using context Manager
while True:
    userInput = input("Enter your option (read or write)")
    
    match userInput:
        case "read":
            #fileread = open("test.txt","r")  --old approach
            #contents = fileread.readlines(); --old approach
            #fileread.close()                 --old approach
            #new approach below - no need of close()
            with open("test.txt","r") as file:
                contents = file.readlines()
                
            print("contents:",contents)
            
        case "write":
            data = input("Enter text to be written:")
            #fileWrite = open("test.txt","w")--old approach
            #contents = fileWrite.writelines(data)--old approach
            #fileWrite.close()--old approach
            with open("test.txt","w") as file:
                file.writelines(data)