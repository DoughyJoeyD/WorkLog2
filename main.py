import time
import sys
import csv

from task import Task, clearscreen

#allows the user to create multiple task entries each time they run the program
tasks = []

def menu():
    clearscreen()
    choices = ["1: New Task", "2: Search Existing Tasks", "3: Quit"]
    runner = True
    while runner == True:
        clearscreen()
        print("#----WorkLog2----#")
        for key in choices:
            print(key)
        choice = input('Choose a Number: ')
        try:
            if int(choice) <= 4:
                if int(choice) == 1:
                    get_task()
                    runner = False
                if int(choice) == 2:
                    search()
                    runner = False
                if int(choice) == 3:
                    clearscreen()
                    print('Okay, Goodbye!')
                    time.sleep(1)
                    sys.exit()
                    runner = False

            if int(choice) >= 4:
                print('Quit Cheating')
                time.sleep(1)

        except ValueError:
            print('Oops Select 1, 2 or 3...')
            time.sleep(2)

def get_task():
    """This function gets the users task and stores it as an instance that
        can be used to search for specific parts of each task"""
    #This calls the Class Task to get a user input
    #also temorary assigns it to instance before adding it to tasks list
    instance = Task()
    #Grabs the name of task
    instance.get_task_name()
    #Grabs the date
    instance.get_date()
    #grabs the time
    instance.get_time()
    #Grabs extra notes the user name want to include
    instance.get_remarks()
    #clears the screen
    clearscreen()
    #prints the task in a neat way
    instance.taskprinter()
    save = False
    clearscreen()
    while save is False:
        choices = ['Y', 'N']
        yes = ['Y']
        no = ['N']
        instance.taskprinter()
        correct = input('Does Everything Look Correct? (Y/N): ')
        #....if it is correct
        if correct.upper() in yes:
            clearscreen()
            print('Task has been Added')
            time.sleep(1)
            save = True

        #...if its not correct
        if correct.upper() in no:
            clearscreen()
            time3 = instance.time
            name = instance.name
            date = instance.date.strftime('%m/%d/%Y')
            extra = instance.extra
            #asks the user whats wrong
            print("1:Name:{}".format(name), "2:Date:{}".format(date), "3:Time:{}".format(time3), "4:Extra:{}".format(extra))
            options = [1, 2, 3, 4]
            fixed = False
            while fixed == False:
                wrong = input('Whats Wrong?: ')
                #if the dont enter what were looking for send them an error
                #run it again
                if wrong not in options:
                    print("Not an Option- Enter 1-4")
                #if the name is selected
                if wrong == '1':
                    #calls the name part of the instance to edit it
                    instance.get_task_name()
                    fixed = True
                    clearscreen()
                #if date is selected
                if wrong == '2':
                    #calls the date part of the instance to edit it
                    instance.get_date()
                    fixed = True
                    clearscreen()
                #if time is selected
                if wrong == '3':
                    #calls the time part of the instance to edit it
                    instance.get_time()
                    fixed = True
                    clearscreen()
                #if notes or extra is selected
                if wrong == '4':
                    #calls the notes part of the task entry to edit it
                    instance.get_remarks()
                    fixed = True
                    clearscreen()
        #if the user doesnt give a Y or N this message shows
        if correct.upper() not in choices:
            clearscreen()
            print('Not an option Buddy')

    #adds the fully finished task instance to the tasks list
    with open('tasks.csv', 'a') as csvfile:
        writer1 = csv.writer(csvfile, delimiter=',')
        writer1.writerow([instance.name] + [instance.date.strftime('%m/%d/%Y')] + [instance.time] + [instance.extra])

def search():
    clearscreen()
    print("Choose a Search Method")
    choices = ['A: By Name or Extra', 'B: By Date', 'C: By Time Taken', 'D: By Pattern ']
    runner = true
    while runner == True:
        



def again():
    clearscreen()
    """Asks the user if they want to preform another task, only bypassed when quit is called"""
    #asks for a user response
    print("Would you like to prefrom another task? ")
    response = input("Yes-1 - No-2 ")
    #if they give a vaild response
    try:
        if int(response) < 3:
            if int(response) == 1:
                menu()
            if int(response) == 2:
                pass
        if int(response) >= 3:
            print("1 or 2... not another number")
            time.sleep(1)
            again()
    #if they give us trouble
    except ValueError:
        print("Ooops Select 1 or 2...")
        time.sleep(1)
        again()

def __init__():
    menu()
    again()
    clearscreen()
    print('Thanks for Using WorkLog2')
    time.sleep(1)
    print('Goodbye!')
    time.sleep(1)
    clearscreen()

__init__()
