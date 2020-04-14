print ("This is a productivity tracker. You are welcome.")
tasks = int(input("How many things do you want to accomplish today?"))
if tasks>0: 
    print ("That's wonderful! Let me know when you're done.")
elif tasks==0: 
    print ("Yay! A rest day! Emjoy :)")
else: 
    print("Uh... I don't think you understand what a productivity tracker is.")

things_done = int(input("How many things did you do today?"))
result = int( things_done/tasks*100)
print (result,"% is how productive you were today")
if result>=50:  
    print ("Good job!")