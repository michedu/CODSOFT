# to -do list
list = []

# view list
def view():
    print(f"{list}\n")

# create/add
def add():
    info = input("Please type down your task.   ")
    list.append(info)
    print(f"{info} 'has been noted'\n")
    more = input("Would you like to add more tasks? \n").lower()
    if more == "yes":
        info = input("Please type down your task.   ")
        list.append(info)
        print(f"{info} 'has been noted'\n")

# remove
def remove():
    text = input("Which task? ")
    for item in list:
        if item == text :
            list.remove()
        print(f"{text} 'has been removed'\n")
    delete= input("Would you like to remove anymore tasks? ").lower()
    if delete == "yes":
        if item == text :
            list.remove()
        print(f"{text} 'has been removed'\n")
        
#main
def menu():
    listing = True
   
    while listing is True:
        print("1.View TO-DO LIST")
        print("2.Add tasks")
        print("3.Remove tasks")
        print("4.Exit")
        cho = input("What would you like to choose: \n")
        if cho == "1":
            view()
        elif cho == "2":
            add()
        elif cho == "3":
            remove()
        else:
            listing = False
menu()

