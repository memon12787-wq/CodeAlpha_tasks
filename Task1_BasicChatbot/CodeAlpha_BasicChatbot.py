from datetime import datetime

counter=0
print("WELCOME TO THIS BASIC CHATBOT")
def hello():
  print("Hi!")

def how_are_you():
  print("I'm fine! Thanks") 
    
def who_are_you():
  print("I'm a basic chatbot")

def what_is_your_name():
  print("I'm a basic chatbot")

def good_morning():
  print("Good morning!")
 
def good_afternoon():
  print("Good afternoon!")

def good_evening():
  print("Good evening!")

def thankyou():
  print("You're welcome!")

def thanks(): 
   print("Happy to help!")

def show_time():
  print(datetime.now())

def show_count():
  print(f"Message count: {counter}")    

def show_help():
  print("Available commands: hello, how are you, who are you, what is your name, good morning, good afternoon, good evening, thankyou, thanks, bye")

def bye():
  print("Goodbye!")

while True:  
  inp=input("Ask Anything\n").lower()
  counter=counter+1
  if inp=="hello":
        hello()
  elif inp=="how are you":
        how_are_you()
  elif inp=="who are you":
        who_are_you()
  elif inp=="what is your name":
        what_is_your_name()
  elif inp=="good morning":
        good_morning()
  elif inp=="good afternoon":
        good_afternoon()
  elif inp=="good evening":
        good_evening()
  elif inp=="thankyou":
    thankyou()
  elif inp=="thanks":
    thanks()
  elif inp=="time":
    show_time()
  elif inp=="count":
    show_count()
  elif inp=="help":
     show_help()
  elif inp=="bye":
     bye()
     break
  else:
    print("Sorry, I don't understand that.")
    
    
