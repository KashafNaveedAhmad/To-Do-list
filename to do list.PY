print("WELCOME!\nTO YOUR TO-DO LIST")
task=[]
user=[]
remove=None
choice=None
import time
while choice!=4:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice=int(input("enter of your choice:"))
    if(choice==1):
        task= (input(f"PLEASE ENTER YOUR  DAILY TASKS:"))
        user.append(task)
    elif(choice==2):
        print(f"your entered tasks are:",user)
    elif(choice==3):
        rem=int(input("enter the task number you want to remove:"))
        if(rem>=0):
            user.pop()
        else:   
          print("LIST EMPTY!\nTRY ADDING TASKS!")
        
print("THANK YOU FOR USING TO-DO LIST.")
print("your to-do list is closing...")
time.sleep(3)