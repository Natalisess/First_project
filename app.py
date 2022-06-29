from random import *

Random = choice(["A","B","C"])

while True :
    RanDom = input("Any alphabet [ A B C ]: ")
    try :
        if Random == RanDom :
            print("Correct")
            break
        else :
            print("Return")
    except :
        print("Error [Thinking about Error]")
        
# Answer is two Error = []
