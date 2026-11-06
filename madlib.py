#string concatenation (akak hot to put strings together)
#suppose we want to creare a string that say "subscribe to_____ "
#youtuber="Kylie Yang"#some string variable
#ways to do this
#print("subscribe to "+youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"sunscribe to {youtuber}")

adj=input("Adjective: ")
verb1=input("Verb1: ")
verb2=input("Verb2: ")
famous_person=input("famous person: ")


madlib=f"Computer programming is so {adj}! It makes me so excited all the time because\
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)  
