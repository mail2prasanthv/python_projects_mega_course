#doc string (help) for a method 

def printGreetings(msg = "Good Morning"):
    """
    Prints Greeting message
    """
    print ("Hi", msg)

def printGreetingsNew(msg1, msg2 = "Good Morning"): # default should be at en d
    print (msg1, msg2)

printGreetings()
printGreetings("Good Evening")
print("-----------Testing one mandatory and one default argument-----------")
printGreetingsNew("hello")#one arg mandatory
printGreetingsNew("hello", "good Evening")#one arg mandatory
