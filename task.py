from datetime import datetime
import os
import time

#handy script to clean the screen/make the program look nice
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#how each task is constructed
     #name
     #date of task
     #time taken
     #extra notes
class Task():
    def __init__(self):
        pass

    #asks the user for a task name
    def get_task_name(self):
        clearscreen()
        name = input("Task Name: ")
        if name.upper != "BACK":
            self.name = name.upper()
    #asks the user for a task time
    def get_time(self):
        clearscreen()
        self.time = False
        while self.time == False:
            try:
                time = input('How long was the task?(Only Enter Min): ')
                self.time = str(int(time))
            except ValueError:
                print('Thats not a number!')
    #asks the user for extra notes
    def get_remarks(self):
        clearscreen()
        extra = input("Additional Notes? ").upper()
        self.extra = extra
    #asks the user for a date in MM/DD/YYYY Format
    def get_date(self):
        clearscreen()
        self.date = False
        while self.date == False:
            try:
                date = input("Please enter the date of task(MM/DD/YYYY): ")
                self.date = datetime.strptime(date, '%m/%d/%Y')
            except ValueError:
                clearscreen()
                print('Oops, Please Enter In Month(08), Day(04), Year(1990) Format!')
                time.sleep(2)
    #A really clean way of printing each task all at once
    def taskprinter(self):
        print("---------------------")
        print('Task Name: ' + self.name)
        print('Task Date: ' + self.date.strftime('%m/%d/%Y'))
        print('Time Taken: ' + self.time + " Minutes")
        print('Extra: ' + self.extra)
        print("---------------------")
