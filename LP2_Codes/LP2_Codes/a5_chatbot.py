import random
import webbrowser
from datetime import datetime

ques=["1","2","3","4","5"]
ans=["11","22","33","44","55"]

greet=["hi","hello","hii"]
resgreet=["hello there","welcome","nice to see you"]

leave=["bye","talk to you later","bye bye","goodbye"]
resleave=["bye-bye","see you again","see you later","good bye"]

while(True):
    user=input("User: ")
    user=user.lower()
    
    now=datetime.now()
    time=now.strftime("%H:%M:%S")
    date=now.strftime("%d:%m:%y")
    
    if(user in greet):
        print("Chatbot: ",random.choice(resgreet))
    
    elif(user in ques):
        index=ques.index(user)
        print("Chatbot: ",ans[index])
    
    elif("open google" in user):
        webbrowser.open("https://www.google.com")
        print("Chatbot: Opening google")
    
    elif("open youtube" in user):
        webbrowser.open("https://www.youtube.com")
        print("Chatbot: Opening youtube")
    
    elif("time" in user):
        print("Chatbot: Current time is: ",time)
    
    elif("date" in user):
        print("Chatbot: Current date is: ",date)
    
    elif(user in leave):
        print("Chatbot: ",random.choice(resleave))
        break
    
    else:
            print("Chatbot: I'm sorry, I didn't understand. Can you please rephrase?")
    