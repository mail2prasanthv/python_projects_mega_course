import json

#read file
with open("./assignment34/data.json","r") as file:
    content = file.read()
    
#converts to json Obj
jsonObjs = json.loads(content)#datatype of eachItem is list

print("data type of jsonObj", type(jsonObjs))# <class 'list'>

score =0
# loop through all questions
for eachItem in jsonObjs:
    #datatype of eachItem is dictionary
    question = eachItem["question_text"] #string
    options = eachItem["options"]#string
    correctanswer = eachItem["correct_answer"]#int
    
    print(question)
    #prints each option
    for index,eachOption in enumerate(options):
        print(index + 1,".",eachOption)
        
    userChoice = int(input("Enter your answer:"))
    # update the dictionary with user input
    eachItem["user_choice"] = userChoice;
    # compute score
    if userChoice== correctanswer:
        score =score+1

print("Total number of correct answer:"  , score)
    
    
    
    
    
    


