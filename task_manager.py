#=====importing libraries===========
# i am using the import function to import the date and time to use for adding tasks and checking if they are overdue

# I did not know how to do this so i googled it and found the following website to tell me how to import the current date ands time
# https://www.programiz.com/python-programming/datetime/current-datetime

import datetime
from datetime import *

#======= Functions =========

# this is where i will create all of my functions for the menu options that the user chooses - it has one parameter which is their menu selection choice

# function to register a user if 'r' is chosen:
def register_user(menu_selection):

    if menu_selection.lower() == "r":

        new_user_account = str(input("Please enter a new Username: \n"))

        # check to see if username already exists in usernames_list below
        while new_user_account in usernames_list:

            print("This account name is already taken")

            new_user_account = str(input("Please enter a new Username: \n"))

        # if the entered username doesnt exist, this block of code will run
        if new_user_account not in usernames_list:

            # adds the entered username to the usernames list below
            usernames_list.append(new_user_account)

            # adds the list to the user_details dictionary i created below.
            user_details["Usernames"] = usernames_list

        # prompts user to enter a new password for said username
        new_password = input("Please enter a new password for the user account: \n")

        # asks user to confirm new password to make sure it is correct
        password_confirmation = input("Please confirm the password: \n")

        # while loop to prompy user if passwords do not match
        while new_password != password_confirmation:
            print("The passwords do not match")
            new_password = input("Please enter a new password for the user account: \n")
            password_confirmation = input("Please confirm the password: \n")

        # if passwords match, a message will be displayed and then the new password will be added to the password_list list i created below
        if new_password == password_confirmation:

            # message to let user know the passwords match
            print("The passwords match!\n")

            # adds the new password created to the list for the passwords below
            passwords_list.append(new_password)

            # adds the password list to the user_details dictionary created below
            user_details["Passwords"] = passwords_list

            # opens user.txt file to write the new user details to it, so it is recognised by the task manager
            with open('user.txt', 'r+') as f:

                # for statement that prints username and password on seperate lines
                # no. of lines = no. of items in the usernames_list i created
                for i in range(len(usernames_list)):

                    # this line writes from my created dictionary and adds it in the correct format - username, password
                    f.write(user_details["Usernames"][i] + ", " + user_details["Passwords"][i] + "\n")

        # return a message when function has sucessfully ran
        return("Your new User Details have sucessfully been stored!")


# declaring a function for adding a task if 'a' is chosen: - it has one parameter which is their menu selection choice
def add_task(menu_selection):

    # if the user selects a when the menu pops up:
    if menu_selection.lower() == "a":

        # imports date into this function to check when task is due and if it is overdue
        import datetime
        from datetime import date

        # asking user to input the user they want to assign the task to and storing it as a variable
        assigned_person = str(input("\nPlease enter the username you would like to assign the task to: \n"))

        # asking user to input the title of the task and storing it as a variable
        task_title = str(input("\nPlease enter the title of the task: \n"))

        # asking for description of the task and storing it as a variable 
        description = str(input("\n Please enter a description of the task you would like completing: \n"))

        # using the function i imported above (datetime) to get todays date and storing it as a variable
        todays_date = datetime.date.today()

        # creating a variable called assigned_date which will change the above variable of todays date into a string so it can be used as the assigned date
        # I didn't know how to convert dates to strings with the correct formatting so i did some research and found this website to help me - https://stackabuse.com/how-to-format-dates-in-python/
        # %d - day of the month
        # %b - first 3 chars of the month
        # %Y - the year in 4 digit format
        assigned_date = todays_date.strftime('%d %b %Y')

        # variable that stores the user input for due_date
        due_date_input = input("\nPlease enter the due date of the task (dd-mm-yyyy): \n")

        # creating a var named date_list for the date to split between the - entered by the user
        date_as_list = due_date_input.split("-")

        # creates a list called date_as_numbers which stores the numbers the user entered above
        date_as_numbers = [int(x) for x in date_as_list]

        # creates a variable called due date that formats it according to the indexing of the list i created
        due_date = date(date_as_numbers[2], date_as_numbers[1], date_as_numbers[0]).strftime('%d %b %Y')

        # sets the task completion to be automattically 'no' as it will not have been completed yet
        is_task_completed = "No"

        # adds all of the info inputted by the user into a list for the tasks so i can put it into my tasks_dictionary i created below
        list_of_tasks = [assigned_person, task_title, description, assigned_date, due_date, is_task_completed]

        # adding list of tasks to my created tasks_dictionary - it will tell you details on the task depending on what the count variable is set too
        tasks_dictionary[f"Task {count} details:"] = list_of_tasks

        # i will now open tasks.txt to write the new task information to it.

        with open('tasks.txt', 'r+') as f3:

            # printing the values from the list for each key inside the dictionary i created - to a new line
            for key in tasks_dictionary:
                
                # casting my task dictionary to a string so it can be added to the text file
                lines_as_string = str(tasks_dictionary[key])

                # creating a list of bad characters so when i view the task i can remove them so it just shows up as a string
                banned_characters = ["[", "]", "\'",]

                # for loop that replaces the banned characters from the above list from the list/dictionary formatting - this is so these characters dont show up when it is printed
                for i in banned_characters:

                    lines_as_string = lines_as_string.replace(i, "")
                
                # this line of code writes each string line in the correct format to the tasks.txt file
                f3.write(lines_as_string + "\n")

        # message that will print once function has sucessfully ran
        return("\n Your tasks have been added sucessfully! \n")

# function for if the user wants to view all tasks 'va' - it takes one parameter which is their menu selection choice
# all of the tasks will be stored in the tasks_dictionary i created so i will use this to show the user the tasks
def view_all_tasks(menu_selection):

    # if the menu selection is 'va' then the task counter will be set to 0
    if menu_selection.lower() == 'va':

        tasks_counter = 0

        # for every task in the dictionary, the counter will add 1
        for key in tasks_dictionary:

            tasks_counter +=1

            # displaying the tasks in an easy to read format
            print(f"""=====================================================

            Task {str(tasks_counter)}:          \t{str(tasks_dictionary[key][1])}
            Assigned to:                        {str(tasks_dictionary[key][0])}
            Date assigned:                      {str(tasks_dictionary[key][3])}
            Due date:                           {str(tasks_dictionary[key][4])}
            Is the Task complete?               {str(tasks_dictionary[key][5])}
            Task description:

            {str(tasks_dictionary[key][2])}
            ================================================================""")
    # message to print once function has run
    return("\nThat is all of the tasks\n")


# function for if the user wants to view their tasks and select 'vm' - this function takes two paramaters, their selection choice and their username (this is to show only their tasks)
def view_my_tasks(menu_selection, username):

    # this will only run if they select 'vm' and their username is correct
    if menu_selection == "vm":

        # this var sets the count for the number of tasks and starts it off with a value of 0
        task_counter = 0

        for key in tasks_dictionary:

            # this calculates the total number of tasks by increasing the count of the task_counter throughout the task dictionary
            task_counter += 1

            # if the username of the user is equal to index of 0 in the task dictionary then they can view their tasks
            if username == (tasks_dictionary[key][0]):

                # displaying the tasks in an easy to read format
                print(f"""=====================================================

            Task {str(task_counter)}:          \t{str(tasks_dictionary[key][1])}
            Assigned to:                        {str(tasks_dictionary[key][0])}
            Date assigned:                      {str(tasks_dictionary[key][3])}
            Due date:                           {str(tasks_dictionary[key][4])}
            Is the Task complete?               {str(tasks_dictionary[key][5])}
            Task description:

            {str(tasks_dictionary[key][2])}
            ================================================================""")
    
    # i will now give the user an option to edit their task - by allowing them to mark it as complete or edit

    # var that allows the user to input a task number to edit
    task_selector = input("\n Please select the task you would like to edit (Task 1 = 0, Task 2 = 1, etc...) or Enter '-1' to return to the main menu!\n")

    # if the user enterd '-1' they will return to the main menu
    if task_selector == '-1':
        return(menu)
    
    # if user doesnt return to menu and enters a task number then they will get these prompts
    else:

        # user gets option to either edit or mark as complete
        option = input("Would you like to mark the task as complete or edit the task? (e.g. mark OR edit) \n")

        # if they choose to mark as complete then it changes the no to a yes in the dictionary
        if option.lower() == 'mark':
            
            tasks_dictionary[-1] = 'Yes'

            # tells user task has been marked as complete
            return("\nYour task has sucessfully been marked as complete! \n")

        # if the user chooses to edit the task and it is still incomplete then they can edit 
        elif option.lower() == 'edit' and tasks_dictionary[key][5] == 'No':

            edit_choice = input("What would you like to edit, task username or due date? (Type 'U' or 'D')\n")

            if edit_choice.lower() == 'u':
                
                # if they choose to edit the username it creates a new var to let them input a new username
                name_editor = input("Please enter a new username for the task: \n")
                
                # changes the name value in the task dictionary to the new inputted username
                tasks_dictionary[0] = name_editor

                # return message to let them know its sucessful
                return("The task username has been updated sucessfully! \n")

            # code block for if user chooses d
            elif edit_choice.lower() == 'd':

                # new var that assigns the new due date
                change_due_date = input("Please enter a new due date (for example - 17 Dec 2022) \n")

                # changes the due date in the dictionary to new inputted one
                tasks_dictionary[key][4] = change_due_date

                return("The due date has successfully been changed!\n")

            # if the useer wants to edit but the task has been completed it will print this message
            elif option == 'edit' and tasks_dictionary[key][5] == 'No':
                return("You can only edit tasks that are not already complete")

    return("\n That is all of your tasks!\n")

# function to check if a task is overdue
def over_due_task_check(due_date):

    # sets overdue as false to start
    over_due = False

    import datetime # import datetime and date to check if overdue
    from datetime import date

    # as my dates in the tasks are fomratted as dd mmm yyyy as a string they need to be ints to comapre dates 
    # split var into a list
    date_list = due_date.split()

    day = int(date_list[0]) # casts first index to int and stores it in day variable
    year = int(date_list[2])

    # a new dict for months to calculate string month into an int
    months_dictionary = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    # The corresponding value of the key in months_dictionary which is equal to date_list[1] (i.e. 'Dec', 'Oct' etc.) is stored in 'month'.
    # This will be a number value from the appropriate key in months_dictionary.
    month = months_dictionary[date_list[1][0:3]]

    # gettitng current date and putting it in the correct format
    todays_date = datetime.date.today().strftime('%d %b %Y')

    # same process as above for current date - split into a list
    todays_date_list = todays_date.split()

    day_1 = int(todays_date_list[0])  # The first item is stored as an integer in day_1.
    year_1 = int(todays_date_list[2])  # Second item is stored as an integer in year_1.
    month_1 = months_dictionary[todays_date_list[1]]  # The  integer value from months_dictionary at the appropriate key is stored in month_1.

    # now i have integers for year, day and month i can now compare the 2 dates
    # due date - date1
    date1 = date(year, month, day)
    # current date
    date2 = date(year_1, month_1, day_1)

    # if current date is greater than the due date then over_due is True
    if date2 > date1:
        over_due = True
        return(over_due)
    
    elif date1 > date2 or date1 == date2: # if due date is greater or equal to current date then overdue is false
        over_due = False
        return(over_due)

# function for display statistics that will be used to display statistics and generate reports!
def display_statistics():

    # for this function to work i need to generate 2 txt files - task summary and user summary to summarise all of the data
    # i will create variables for these two items and set them as empty strings so i can store data in them later on
    task_summary = " "
    user_summary = " "

    # to get the total number of tasks it is equal to the length of the key count in my tasks_dictionary i created
    total_tasks = len(tasks_dictionary)

    # i will not put a string with the total task numbers into the task summary var i created
    task_summary += f"\nThe total number of tasks in this task manager is {str(len(tasks_dictionary))}!\n"

    # setting variables to correspond to - complete, incomplete, and overdue tasks 
    c = 0
    i = 0
    o = 0

    for key in tasks_dictionary:

        if tasks_dictionary[key][5] == 'Yes': # check for completed tasks
            c += 1 # if task is complete then 1 is added to the complete task var c above
        
        elif tasks_dictionary[key][5] == 'No':
            i += 1

            if over_due_task_check(tasks_dictionary[key][4]): # if overdue task func returns True then a task is overdue
                o += 1

    # All of the numbers calculated above are now added into sentences in the task_summary string.
    # Percentages are also calculated within the f-strings added, with the results being rounded to 2 decimal places and cast into strings into sentences.
    task_summary += (f"\nThe total number of completed tasks is {str(c)}. \n The total number of incomplete tasks is {str(i)}.")
    task_summary += (f"\nThe total number of incomplete and overdue tasks is {str(o)}.")
    task_summary += (f"\nThe percentage of incomplete tasks is {str(round((i / len(tasks_dictionary)) * 100, 2))}%.")
    task_summary += (f"\nThe percentage of tasks that are overdue is {str(round((o / len(tasks_dictionary)) * 100, 2))}%.")

    # now i need to create the task summary file
    with open('task_summary.txt', 'w') as f4:

        # writing the total number of tasks and all other info to this new file
        f4.write(task_summary)

    # setting the variables for total users, complete tasks for users, incomplete tasks for the user, incomplete and overdue tasks for the user
    t_u = 0
    c_u = 0
    i_u = 0
    i_o_u = 0

    for key in tasks_dictionary:

        if tasks_dictionary[key][0] == username: # checks number of tasks assigned to the user
            t_u += 1
        
        elif tasks_dictionary[key][0] == username and tasks_dictionary[key][5] == 'Yes': # checks if task for that user is complete
            c_u += 1

        elif tasks_dictionary[key][0] == username and tasks_dictionary[key][5] == 'No': # checking if user task is incomplete
            i_u += 1

            if over_due_task_check(tasks_dictionary[key][4]): # if task is incomplete and overdue
                i_o_u += 1

    # writing all the calculated data into strings which will be held in user_summary variable
    user_summary += (f"\nThe total number of users registered is {str(len(user_details))}!\n")
    user_summary += (f"\nThe total number of tasks in the task manager is {str(len(tasks_dictionary))}.")
    user_summary += (f"\nThe total number of tasks assigned to {username} is {str(t_u)}.")
    user_summary += (f"\nThe percentage of the total number of tasks assigned to {username} is {str(round((t_u / len(tasks_dictionary)) * 100, 2))}%.")
    user_summary += (f"\nThe percentage of tasks assigned to {username} that have been completed is {str(round((c_u / t_u) * 100, 2))}%.")
    user_summary += (f"\nThe percentage of tasks that still need to be completed by {username} is {str(round((i_u / t_u) * 100, 2))}%.")
    user_summary += (f"\nThe percentage of incomplete and overdue tasks assigned to {username} is {str(round((i_o_u / t_u) * 100, 2))}%.")

    # I now need to generate a user_summary.txt file and write the total number of users to it
    with open('user_summary.txt', 'w') as f5:

        # writing the total number of users to this file
        f5.write(user_summary)

#====Login Section====

# I will be using dictionaries to store my info - this is a dictionary called user_details

# I used section 5.5 of this website to learn more about dictionaries and how to use them:
# https://docs.python.org/3/tutorial/datastructures.html

user_details = {}

# these two lists will help me build my dictionary to store the username and password
usernames_list = []
passwords_list = []

# dictionary called tasks_dictionary that will store the tasks
tasks_dictionary = {}

# this opens the user.txt file to read and write. 
with open('user.txt', 'r+') as f1:

# i will be adding info into the user.txt file below
    for line in f1:

# this strips the newline characters from the line
        newline = line.rstrip('\n') 

# this splits my new line above into a list
        split_line = newline.split(", ") 

        # i will now assign the items from the list into the empty lists i created above
        usernames_list.append(split_line[0])
        passwords_list.append(split_line[1])
        

        #I have now stored my lists as values for keys in my user_details dictionary i created above
        user_details["Usernames"] = usernames_list
        user_details["Passwords"] = passwords_list

# creating a variable called count used to keep track of no. of lines in tasks.txt file
count = 1

# opening tasks.txt to read and write
with open('tasks.txt', 'r+') as f2:

    for line in f2:

        # stripping newline character from the line
        newline = line.rstrip("\n")

        # splitting line into a list
        split_line = newline.split(", ")

        # assigning the list of items to a key in my tasks_dictionary
        tasks_dictionary[f"Task {count} details:"] = split_line

        # count will +1 every time to change the key value for each list of information i created
        count += 1

# getting user input for their login details - username and password and storing them as variables
    username = input("\nPlease enter your username: \n")
    password = input("\nPlease enter your password: \n")

# while loop to determine what to do if username and password is right or wrong
    while(username not in usernames_list) or (password not in passwords_list):

# if username is not in the username list and password is correct it will display error and make them re-enter
        if (username not in usernames_list) and (password in passwords_list):

            print("\nInvalid Username!")

            username = input("\nPlease re-enter your username: \n")

            password = input("\nPlease re-enter your password: \n")
        
        # if password is incorrect but username is it will display the relevant message and ask the user to re-enter
        elif (password not in passwords_list) and (username in usernames_list):

            print("\nYour password is incorrect!")

            username = input("\nPlease re-enter your username: \n")

            password = input("\nPlease re-enter your password: \n")

# if username and password incorrect it will print this message and make the user re-enter their details
        elif (username not in usernames_list) and (password not in passwords_list):

            print("\nYour Username and Password is incorrect!")

            username = input("\nPlease re-enter your username: \n")

            password = input("\nPlease re-enter your password: \n")

    # if the username and password is correct , it will sucessfully login
    if (username in usernames_list) and (password in passwords_list):
        print("\nYou are Sucessfully Logged in!\n")

# whiile the username and password is correct this block of code will run
while True:

# if the username is admin then they will get this extra menu to register a user and display statistics - .lower() used so any case can be entered
    if username == "admin":

        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - generate reports
        ds - display statistics
        e - Exit

        : ''').lower()

# if it is any other user logged in, then they get the menu without the statistics or registering user
    else :

        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

# writing the code that will determine what comes up next once user has chosen an option from the menu

    # displays choices for admin user
    if username == 'admin':

        # if admin chooses option 'r' it will run the function i creaated above for this option
        if menu.lower() == 'r':

            # the register_user function i created will run
            print(register_user(menu))


        # code block for if user chooses option 'a'
        elif menu.lower() == 'a':

            # the add_task function i created will run
            print(add_task(menu))

        # code block for if the user chooses 'va'
        elif menu.lower() == 'va':

            # my function i created to view all tasks will run
            print(view_all_tasks(menu))

        # code block that executes if user chooses 'vm'
        elif menu.lower() == 'vm':

            # if they choose 'vm' it will run the view_my_tasks function i created above.
            print(view_my_tasks(menu, username))

        elif menu.lower() == 'gr': # this causes user_summary and task_summary text files to be generated
            print(display_statistics()) # calls function to generate the report files

        # code block that executes if admin chooses 'ds'
        elif menu.lower() == 'ds':

            # if ds is chosen it will execute my display statistics function i created above to generate the files incase they do not yet exist
            print(display_statistics())

            # it also prints the summary
            print("""\n============================================================
            Please see below for summary:
            =======================================================================\n
            TASK SUMMARY: 
            ========================================================================\n""")

            # opens task_summary text file and prints every line in it
            with open('task_summary.txt', 'r+') as f4:

                for line in f4:
                    print(line)

            print("""\n============================================================
            USER SUMMARY: 
            ========================================================================\n""")

            # opens the user_summary txt file i created and prints every line in it.
            with open('user_summary.txt', 'r+') as f5:

                for line in f5:

                    print(line)
        
            print("""\n============================================================
            End of Statistics Report: 
            ========================================================================\n""")

        # code block that executes if user chooses 'e'
        elif menu.lower() == 'e':
            print('Goodbye!!!')
            exit()

        # if user doesn't choose a valid option from the menu this will print
        else:
            break

    # displays choices for non admin userrs
    if username != 'admin':
        
        # code block for if user chooses option 'a'
        if menu.lower() == 'a':

            # the add_task function i created will run
            print(add_task(menu))

        # code block for if the user chooses 'va'
        elif menu.lower() == 'va':

            # my function i created to view all tasks will run
            print(view_all_tasks(menu))

        # code block that executes if user chooses 'vm'
        elif menu.lower() == 'vm':

            # if they choose 'vm' it will run the view_my_tasks function i created above.
            print(view_my_tasks(menu, username))

        elif menu.lower() == 'r':
            print("\nOnly an admin can register a user, Please select a choice off your menu!\n")

        elif menu.lower() == 'gr':
            print("\nOnly an admin can generate reports, Please select a choice off your menu!\n")

        elif menu.lower() == 'ds':
            print("\nOnly an admin can display statistics, Please select a choice off your menu!\n")

        elif menu.lower() == 'e':
            print('\nGoodbye!!!\n')
            exit()

        # if user doesn't choose a valid option from the menu this will print
        else:
            break