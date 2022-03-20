def clean():
    import os
    import time
    time.sleep(0.1)
    os.system('cls')


def clean_2():
    import os
    import time
    Enter = input("\n\nPress enter key to continue ..........")
    time.sleep(0.1)
    os.system('cls')


def main():
    clean()
    print("Welcome User to the program")
    speak("Welcome User to the program \n opening login menu")
    clean()
    try_except_EDMSDF_1()
    try_except_file_uid_pass()
    work_on_choice_0()


def start_program():
    clean()
    all_try_except()
    cache()
    clean()
    work_on_choice_1()


def speak(str):
    from win32com.client import Dispatch
    Dispatch(("SAPI.Spvoice")).Speak(str)


def login_menu():
    print("****************** Login Menu ******************")
    print("1 : Login In User Account")
    print("2 : Creat New User Account")
    print("3 : Change User Account Password")
    print("4 : Forgot User Account Password")
    print("5 : Delete User Account ")
    print("6 : Close Program")
    login_menu_input = (input("Enter your choice [Number] :"))
    return (login_menu_input)


def work_on_choice_0():
    import sys
    woc = login_menu()
    woc_int = woc.isdigit()
    woc_space = woc.isspace()
    woc_len = len(woc)
    if(woc_int == True):
        woc = int(woc)
        if (woc == 1):
            clean()
            login()
        elif (woc == 2):
            clean()
            speak("opening creat account menu")
            print("************Creat Account Menu************")
            Creat_account()
        elif (woc == 3):
            clean()
            speak("opening Change Password menu")
            print("************Change Password Menu************")
            Change_pass()
        elif (woc == 4):
            clean()
            speak("opening Forgot Password menu")
            print("************Forgot Password Menu************")
            for_pass()
        elif(woc==5):
            clean()
            speak("opening delete user account menu")
            print("************Delete User Account Menu************")
            delete_user_account()
        elif (woc == 6):
            clean()
            print("Closing the program......")
            clean()
            sys.exit()
        else:
            speak("Please, Enter a valid choice")
            clean_2()
            work_on_choice_0()
    elif(woc_space == True):
        speak("You enter a space which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_0()
    elif(woc_len == 0):
        speak("You does not enter anything which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_0()
    else:
        speak("You enter an alphabet or special symbol which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_0()


def first_menu():
    print("*************** Main Menu***************")
    print("1 : Add Employee Detail")
    print("2 : Update or Delete Employee detail")
    print("3 : Print Detail")
    print("4 : Salary Management System")
    print("5 : Recycle Bin")
    print("6 : Logout Account ")
    add_cache2()
    first_menu_input = (input("Enter your choice [Number] :"))
    return (first_menu_input)


def work_on_choice_1():
    import time
    global Employee_name, Employee_post, Employee_id, Employee_address, Employee_gmail, Employee_Phone, Employee_salary, recycle_Employee_name, recycle_Employee_post, recycle_Employee_id, recycle_Employee_address, recycle_Employee_gmail, recycle_Employee_Phone, recycle_Employee_salary, cache_list, Date, Amount, Time
    woc = first_menu()
    woc_int = woc.isdigit()
    woc_space = woc.isspace()
    woc_len = len(woc)
    if(woc_int == True):
        woc = int(woc)
        if (woc == 1):
            clean()
            speak("opening add employee details menu")
            add_employee()
            speak("Employee Details Added Succesfully ....")
            store_data()
            clean_2()
            work_on_choice_1()
        elif (woc == 2):
            clean()
            speak("opening update or delete employee details menu")
            work_on_choice_2()
        elif (woc == 3):
            clean()
            speak("opening print employee details menu")
            work_on_choice_3()
        elif(woc == 4):
            clean()
            speak("opening salary management system menu")
            work_on_choice_5()
        elif (woc == 5):
            clean()
            speak("opening recycle bin menu")
            work_on_choice_4()
        elif(woc == 6):
            clean()
            Employee_name.clear()
            Employee_post.clear()
            Employee_id.clear()
            Employee_address.clear()
            Employee_gmail.clear()
            Employee_Phone.clear()
            Employee_salary.clear()
            recycle_Employee_name.clear()
            recycle_Employee_post.clear()
            recycle_Employee_id.clear()
            recycle_Employee_address.clear()
            recycle_Employee_gmail.clear()
            recycle_Employee_Phone.clear()
            recycle_Employee_salary.clear()
            cache_list.clear()
            Date.clear()
            Amount.clear()
            Time.clear()
            speak("User Account Log ing out")
            clean()
            work_on_choice_0()
        else:
            speak("Please, Enter a valid choice")
            clean_2()
            work_on_choice_1()
    elif(woc_space == True):
        speak("You enter a space which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_1()
    elif(woc_len == 0):
        speak("You does not enter anything which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_1()
    else:
        speak("You enter an alphabet or special symbol which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_1()


def update_menu():
    print("***********Update or Delete Employee Details Menu***********")
    print("1 : Update Employee Name")
    print("2 : Update Employee Address")
    print("3 : Update Employee Mobile No.")
    print("4 : Update Employee Salary")
    print("5 : Update Employee Post")
    print("6 : Update Employee Gmail")
    print("7 : Delete Employee Detail")
    print("8 : Delete All Data")
    print("9 : Go Back To Previous Menu")
    update_menu_input = (input("Enter your choice [Number] :"))
    return (update_menu_input)


def work_on_choice_2():
    global cache_list
    woc = update_menu()
    woc_int = woc.isdigit()
    woc_space = woc.isspace()
    woc_len = len(woc)
    if(woc_int == True):
        woc = int(woc)
        if (woc == 1):
            clean()
            speak("opening Update Employee Name menu")
            print("***********Update Employee Details Menu***********")
            update_name()
            store_data()
            clean_2()
            work_on_choice_2()
        elif (woc == 2):
            clean()
            speak("opening Update Employee adderss menu")
            print("***********Update Employee Details Menu***********")
            update_address()
            store_data()
            clean_2()
            work_on_choice_2()
        elif(woc == 3):
            clean()
            speak("opening Update Employee mobile number menu")
            print("***********Update Employee Details Menu***********")
            update_Phone()
            store_data()
            clean_2()
            work_on_choice_2()
        elif (woc == 4):
            clean()
            speak("opening Update Employee salary menu")
            print("***********Update Employee Details Menu***********")
            update_salary()
            store_data()
            clean_2()
            work_on_choice_2()
        elif (woc == 5):
            clean()
            speak("opening Update Employee post menu")
            print("***********Update Employee Details Menu***********")
            update_post()
            store_data()
            clean_2()
            work_on_choice_2()
        elif (woc == 6):
            clean()
            speak("opening Update Employee gmail menu")
            print("***********Update Employee Details Menu***********")
            update_gmail()
            store_data()
            clean_2()
            work_on_choice_2()
        elif(woc == 7):
            clean()
            speak("opening delete Employee details menu")
            print("***********Update Employee Details Menu***********")
            delete_employee_detail()
            store_data()
            clean_2()
            work_on_choice_2()
        elif (woc == 8):
            clean()
            speak("opening delete all data menu")
            print("***********Delete All Data Menu***********")
            print("\nYou really want to delete all data ?")
            print("If Yes type Yes/yes/Y/y or If No type anything or press enter")
            a = input("Enter your choice :")
            if (a == "Yes" or a == "Y" or a == "yes" or a == "y"):
                clean()
                delete()
            else:
                print("Detail delitation canceled...")
                clean()
                work_on_choice_2()
        elif (woc == 9):
            clean()
            work_on_choice_1()
        else:
            speak("Please, Enter a valid choice")
            clean_2()
            work_on_choice_2()
    elif(woc_space == True):
        speak("You enter a space which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_2()
    elif(woc_len == 0):
        speak("You does not enter anything which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_2()
    else:
        speak("You enter an alphabet or special symbol which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_2()


def print_data_menu():
    print("1:Print All Employee Detail")
    print("2:Print Employee Detail By ID")
    print("3:Go Back To The Previous Menu")
    print_data_menu_input = (input("Enter your choice [Number] :"))
    return (print_data_menu_input)


def work_on_choice_3():
    woc = print_data_menu()
    woc_int = woc.isdigit()
    woc_space = woc.isspace()
    woc_len = len(woc)
    if(woc_int == True):
        woc = int(woc)
        if (woc == 1):
            clean()
            print_data()
            clean_2()
            work_on_choice_3()
        elif(woc == 2):
            clean()
            print_data_by_id()
            clean_2()
            work_on_choice_3()
        elif(woc == 3):
            clean()
            work_on_choice_1()
        else:
            speak("Please, Enter a valid choice")
            clean_2()
            work_on_choice_3()
    elif(woc_space == True):
        speak("You enter a space which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_3()
    elif(woc_len == 0):
        speak("You does not enter anything which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_3()
    else:
        speak("You enter an alphabet or special symbol which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_3()


def recycle_bin_menu():
    print("*****************Recycle Bin Menu*****************")
    print("1:Print data in recycle bin")
    print("2:Recover Data")
    print("3:Empty Bin")
    print("4:Go Back To The Previous Menu")
    recycle_bin_menu_input = (input("Enter number of your choice:"))
    return (recycle_bin_menu_input)


def work_on_choice_4():
    woc = recycle_bin_menu()
    woc_int = woc.isdigit()
    woc_space = woc.isspace()
    woc_len = len(woc)
    if(woc_int == True):
        woc = int(woc)
        if (woc == 1):
            clean()
            print_recycle_bin_data()
            clean_2()
            work_on_choice_4()
        elif(woc == 2):
            clean()
            recover_data()
            store_data()
            clean_2()
            work_on_choice_4()
        elif(woc == 3):
            clean()
            empty_bin()
            store_data()
            work_on_choice_4()
        elif(woc == 4):
            clean()
            work_on_choice_1()
        else:
            speak("Please, Enter a valid choice")
            clean_2()
            work_on_choice_4()
    elif(woc_space == True):
        speak("You enter a space which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_4()
    elif(woc_len == 0):
        speak("You does not enter anything which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_4()
    else:
        speak("You enter an alphabet or special symbol which is not acceptable")
        speak("Please, Enter a valid choice")
        clean_2()
        work_on_choice_4()


def salary_management_system_menu():
    print("*****************Salary Management System Menu*****************")
    print("1:Add Transaction")
    print("2:Print Transaction ")
    print("3:Delete Transaction ")
    print("4:Update Transaction ")
    print("5:Go Back To The Previous Menu")
    salary_management_system_menu_input = (
        input("Enter your choice [Number] :"))
    return (salary_management_system_menu_input)


def work_on_choice_5():
    woc = salary_management_system_menu()
    woc_int = woc.isdigit()
    woc_space = woc.isspace()
    woc_len = len(woc)
    if(woc_int == True):
        woc = int(woc)
        if (woc == 1):
            clean()
            speak("opening add transaction menu")
            add_transaction()
            clean_2()
            work_on_choice_5()
        elif(woc == 2):
            clean()
            speak("opening print transaction menu")
            print_transaction()
            clean_2()
            work_on_choice_5()
        elif(woc == 3):
            clean()
            speak("opening delete transaction menu")
            delete_transaction()
            clean_2()
            work_on_choice_5()
        elif(woc == 4):
            clean()
            speak("opening update transaction menu")
            update_transaction()
            clean_2()
            work_on_choice_5()
        elif(woc == 5):
            clean()
            work_on_choice_1()
        else:
            speak("Please, Enter a valid choice")
            clean_2()
            work_on_choice_5()
    elif(woc_space == True):
        speak("You enter a space which is not acceptable")
        speak("Please, Enter a valid choice")
        clean()
        work_on_choice_1()
    elif(woc_len == 0):
        speak("You does not enter anything which is not acceptable")
        speak("Please, Enter a valid choice")
        clean()
        work_on_choice_1()
    else:
        speak("You enter an alphabet or special symbol which is not acceptable")
        speak("Please, Enter a valid choice")
        clean()
        work_on_choice_1()


def login():
    global user
    User_id = input("Enter Your User Id :")
    for i in range(0, len(user_id)):
        if (User_id == user_id[i]):
            temp = 1
            while(temp < 4):
                User_pass = input("Enter Your Password :")
                if (User_pass == user_pass[i]):
                    clean()
                    print("Login succesfully")
                    speak("Login succesfully")
                    user = User_id
                    start_program()
                else:
                    speak("Password not match")
                temp += 1
            else:
                speak("Maximuum limit of login exceeded")
                clean_2()
                work_on_choice_0()
            break
    else:
        speak("User Id Not Found")
        clean_2()
        work_on_choice_0()


def Creat_account():
    global user_pass, user_id, sec_que1_list, sec_que2_list, user
    print("Your ID must contain some Alphabet (UPPERCASE) and Number (Optional)")
    print("For Ex: Correct method: ABC123 , ABCD ,12ABC12 etc.\n        Incorrect method: Abc123 , abC123 , 123456")
    User_id = input("Enter Your New User Id :")
    dig = User_id.isdigit()
    lower = User_id.isupper()
    if(dig == False and lower == True):
        count = user_id.count(User_id)
        if(count == 0):
            User_pass1 = input("Enter Your Password :")
            temp = 1
            while(temp < 4):
                User_pass2 = input("Renter Your Password :")
                if (User_pass2 == User_pass1):
                    print("Secrity Questions ")
                    sec_que1 = input(
                        "What is your favourite teacher name name :")
                    sec_que1_list.append(sec_que1)
                    sec_que2 = input(
                        "What is your favourite mobile company name :")
                    sec_que2_list.append(sec_que2)
                    user_id.append(User_id)
                    user_pass.append(User_pass1)
                    clean()
                    print("Account created succesfully")
                    speak("Account created succesfully")
                    user = User_id
                    clean()
                    print("Log In To Account")
                    speak("log in to account")
                    store_uid_pass()
                    try_except_EDMSDF_1()
                    try_except_file_uid_pass()
                    start_program()
                else:
                    speak("Rentered Password Not Match")
                temp += 1
            else:
                speak("Entering limit exceeded")
                clean_2()
                work_on_choice_0()
        else:
            speak("Id Already Exist")
            clean_2()
            work_on_choice_0()
    elif(dig == True):
        print("Please enter a combination of alphabet(Uppercase) and number,Only Number not allowed")
        speak("Account creation cancelled")
        clean_2()
        work_on_choice_0()
    else:
        print("Please enter a alphabet in Uppercase ,Lowercase not allowed")
        speak("Account creation cancelled")
        clean_2()
        work_on_choice_0()


def Change_pass():
    global user_pass
    User_id = input("Enter Your User Id :")
    for i in range(0, len(user_id)):
        if (User_id == user_id[i]):
            te = 1
            while(te < 4):
                User_pass1 = input("Enter Your Password :")
                if (User_pass1 == user_pass[i]):
                    tem = 1
                    while(tem < 4):
                        User_pass2 = input("Enter Your New Password :")
                        temp = 1
                        while(temp < 4):
                            User_pass3 = input("Renter Your New Password :")
                            if (User_pass2 == User_pass3):
                                user_pass[i] = User_pass3
                                speak("Password change succesfully")
                                clean()
                                work_on_choice_0()
                            else:
                                speak("Rentered Password not match")
                            temp += 1
                        else:
                            speak("Entering limit exceeded")
                            clean_2()
                            work_on_choice_0()
                    else:
                        speak("Password not match")
                    tem += 1
                else:
                    speak("Password Not Match")
                te += 1
            else:
                speak("Entering limit exceeded")
                clean_2()
                work_on_choice_0()
            break
    else:
        speak("Id not found")
        clean_2()
        work_on_choice_0()


def for_pass():
    global user_pass
    User_id = input("Enter Your User Id :")
    for i in range(0, len(user_id)):
        if (User_id == user_id[i]):
            print("Secrity Questions ")
            temp = 1
            while(temp < 4):
                sec_que1 = input("What is your favourite teacher name name :")
                if(sec_que1 == sec_que1_list[i]):
                    tem = 1
                    while(tem < 4):
                        sec_que2 = input(
                            "What is your favourite mobile company name :")
                        if(sec_que2 == sec_que2_list[i]):
                            User_pass_new = input("Enter New Password :")
                            te = 1
                            while(te < 4):
                                User_pass_new2 = input("Renter New Password :")
                                if(User_pass_new == User_pass_new2):
                                    user_pass[i] = User_pass_new
                                    speak("New Password created succesfully")
                                    clean_2()
                                    work_on_choice_0()
                                else:
                                    speak("Rentered Password Not Match")
                                te += 1
                            else:
                                speak(
                                    "Entering limit exceeded\npassword not change")
                                clean_2()
                                work_on_choice_0()
                        else:
                            speak("Your answer is incorrect")
                        tem += 1
                    else:
                        speak("Entering limit exceeded")
                        clean_2()
                        work_on_choice_0()
                else:
                    speak("Your answer is incorrect")
                temp += 1
            else:
                speak("Entering limit exceeded")
                clean_2()
                work_on_choice_0()
            break
    else:
        speak("Id not found")
        clean_2()
        work_on_choice_0()


def delete_user_account():
    import shutil
    global user_id, user_pass, sec_que2_list, sec_que1_list
    User_id = input("Enter Your User Id :")
    for i in range(0, len(user_id)):
        if (User_id == user_id[i]):
            temp = 1
            while(temp < 4):
                User_pass = input("Enter Your Password :")
                if (User_pass == user_pass[i]):
                    shutil.rmtree("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+User_id)
                    user_id.pop(i)
                    user_pass.pop(i)
                    sec_que1_list.pop(i)
                    sec_que2_list.pop(i)
                    print("Account Deleted Succesfully")
                    speak("Account Deleted Succesfully")
                    store_uid_pass()
                    clean()
                    work_on_choice_0()
                else:
                    speak("Password not match")
                temp += 1
            else:
                speak("Maximuum limit of login exceeded")
                clean_2()
                work_on_choice_0()
            break
    else:
        speak("Id not found")
        clean_2()
        work_on_choice_0()


def add_employee():
    global Employee_name, Employee_id, Employee_address, Employee_Phone, Employee_salary, Employee_gmail, em_id2
    print("*****************Add Employee Details Menu*****************")
    em_name = input("Enter Employee name :")
    Employee_name.append(em_name)
    id_verification()
    em_post = input("Enter Employee post :")
    Employee_post.append(em_post)
    em_address = input("Enter Employee address :")
    Employee_address.append(em_address)
    gmail()
    phone_no()
    em_salary = input("Enter Employee Per month salary:")
    Employee_salary.append(em_salary)
    creat_file2(em_id2)


def id_verification():
    global Employee_id, em_id2
    t = len(Employee_id)
    t2 = len(recycle_Employee_id)
    em_id2 = input("Enter Employee id :")
    if(t == 0 and t2 == 0):
        dig = em_id2.isdigit()
        upper = em_id2.isupper()
        if(dig == False and upper == True):
            Employee_id.append(em_id2)
        elif(dig == True):
            Employee_id.append(em_id2)
        else:
            print("Please,Only enter combination of alphabet(Uppercase) and number")
            speak("Please, Enter a valid choice")
            id_verification()
    else:
        dig = em_id2.isdigit()
        upper = em_id2.isupper()
        if(dig == False and upper == True):
            check = Employee_id.count(em_id2)
            check_2 = recycle_Employee_id.count(em_id2)
            if(check == 0 and check_2 == 0):
                Employee_id.append(em_id2)
            else:
                if(check != 0):
                    i = Employee_id.index(em_id2)
                    a = ("This id is already given to "+ Employee_name[i])
                    speak(a)
                    id_verification()
                elif(check_2 != 0):
                    i = recycle_Employee_id.index(em_id2)
                    b = ("This id is already given to ",
                         recycle_Employee_name[i]+ "whom data is present in recycle bin")
                    speak(b)
                    id_verification()
        elif(dig == True):
            check = Employee_id.count(em_id2)
            check_2 = recycle_Employee_id.count(em_id2)
            if(check == 0 and check_2 == 0):
                Employee_id.append(em_id2)
            else:
                if(check != 0):
                    i = Employee_id.index(em_id2)
                    a = ("This id is already given to "+ Employee_name[i])
                    speak(a)
                    id_verification()
                elif(check_2 != 0):
                    i = recycle_Employee_id.index(em_id2)
                    b = ("This id is already given to "+
                         recycle_Employee_name[i], "whom data is present in recycle bin")
                    speak(b)
                    id_verification()
        else:
            print("Please,Only enter combination of alphabet(Uppercase) and number")
            speak("Please, Enter a valid choice")
            id_verification()


def gmail():
    global Employee_gmail
    em_mail = input("Enter Employee Gmail-id :")
    check = em_mail.find("@gmail.com")
    if(check != -1):
        Employee_gmail.append(em_mail)
    else:
        a = em_mail+"@gmail.com"
        Employee_gmail.append(a)


def phone_no():
    global Employee_Phone
    em_phone = (input("Enter Employee Mobile No. :"))
    em_phone3 = em_phone.isdigit()
    if (em_phone3 == True):
        em_phone2 = int(em_phone)
        if (em_phone2 > 999999999) and (em_phone2 < 10000000000):
            Employee_Phone.append(em_phone)
        elif(len(em_phone) == 10 and em_phone2 <= 999999999):
            speak("Phone no can't be exixt")
            phone_no()
        else:
            print("Mobile no. is not a 10 digit no. you enter a "+
                  len(str(em_phone)), "digit no")
            speak("Please, Enter a valid Number")
            phone_no()
    else:
        speak("Please, Enter only Numeric value")
        phone_no()


def print_data():
    global Employee_name, Employee_id, Employee_address, Employee_Phone, Employee_salary, Employee_post, Employee_gmail
    l = len(Employee_id)
    print("Employee Name--->Post--->I.D.--->Address--->Phone-no.--->Salary")
    if (l == 0):
        print("\nThere is nothing to print......................................")
        speak("There is nothing to print......................................")
    else:
        speak("printing all Employee details")
        for i in range(0, len(Employee_id)):
            print(Employee_name[i], "--->", Employee_post[i], "--->", Employee_id[i], "--->",
                  Employee_address[i], "--->", Employee_gmail[i], "--->", Employee_Phone[i], "--->", Employee_salary[i])


def print_data_by_id():
    global Employee_name, Employee_id, Employee_address, Employee_Phone, Employee_salary, Employee_post, Employee_gmail
    pdbid = input("Enter the ID of Employee whom details you want to print :")
    t = len(Employee_id)
    for i in range(0, t, 1):
        if (pdbid == Employee_id[i]):
            a = "printing all details of ", Employee_name[i]
            speak(a)
            print("Name of Employee            :", Employee_name[i])
            print("Post of Employee            :", Employee_post[i])
            print("ID of Employee              :", Employee_id[i])
            print("Gmail id of Employee        :", Employee_gmail[i])
            print("Phone no. of Employee       :", Employee_Phone[i])
            print("Address of Employee         :", Employee_address[i])
            print("Per Month salary of Employee:", Employee_salary[i])
            break
    else:
        speak("Id not found")


def print_recycle_bin_data():
    global recycle_Employee_name, recycle_Employee_id, recycle_Employee_address, recycle_Employee_Phone, recycle_Employee_salary, recycle_Employee_post, recycle_Employee_gmail
    l = len(recycle_Employee_id)
    print("Employee Name--->Post--->I.D.--->Address--->Phone-no.--->Salary")
    if (l == 0):
        print("\nRecycle bin is empty...........................................")
        speak("Recycle bin is empty...........................................")
    else:
        for i in range(0, len(recycle_Employee_id)):
            print(recycle_Employee_name[i], "--->", recycle_Employee_post[i], "--->", recycle_Employee_id[i], "--->",
                  recycle_Employee_address[i], "--->", recycle_Employee_gmail[i], "--->", recycle_Employee_Phone[i], "--->", recycle_Employee_salary[i])


def update_name():
    global Employee_id, Employee_name
    i_d = input("Enter The Employee ID :")
    for i in range(0, len(Employee_id)):
        if (i_d == Employee_id[i]):
            print("The Employee present name is :", Employee_name[i])
            name_new = input("Enter The Employee New Name :")
            Employee_name[i] = name_new
            speak("Detail updated successfully....")
            break
    else:
        speak("Id not found")


def update_post():
    global Employee_id, Employee_post
    i_d = input("Enter The Employee ID :")
    for i in range(0, len(Employee_id)):
        if (i_d == Employee_id[i]):
            print("You want to update post of ", Employee_name[i])
            print("The Employee present post is :", Employee_post[i])
            post_new = input("Enter the Employee new post :")
            Employee_post[i] = post_new
            speak("Detail updated successfully")
            break
    else:
        speak("Id not found")


def update_address():
    global Employee_id, Employee_address
    i_d = input("Enter The Employee ID :")
    for i in range(0, len(Employee_id)):
        if (i_d == Employee_id[i]):
            print("You want to update address of ", Employee_name[i])
            print("The Employee present address is :", Employee_address[i])
            address_new = input("Enter The Employee New address :")
            Employee_address[i] = address_new
            speak("Detail updated successfully")
            break
    else:
        speak("Id not found")


def update_salary():
    global Employee_id, Employee_salary, Employee_name
    i_d = input("Enter The Employee ID :")
    for i in range(0, len(Employee_id)):
        if (i_d == Employee_id[i]):
            print("You want to update salary of ", Employee_name[i])
            print("The Employee present salary is :", Employee_salary[i])
            salary_new = input("Enter The Employee New salary :")
            Employee_salary[i] = salary_new
            speak("Detail updated successfully")
            break
    else:
        speak("Id not found")


def update_gmail():
    global Employee_gmail, Employee_id, Employee_name
    i_d = input("Enter The Employee ID :")
    for i in range(0, len(Employee_id)):
        if (i_d == Employee_id[i]):
            print("You want to update gmail of ", Employee_name[i])
            print("The Employee present gmail is :", Employee_gmail[i])
            em_mail_new = input("Enter new gmail id :")
            check = em_mail_new.find("@gmail.com")
            if(check != -1):
                Employee_gmail[i] = em_mail_new
                speak("Detail updated successfully")
            else:
                a = em_mail_new+"@gmail.com"
                Employee_gmail[i] = a
                speak("Detail updated successfully")
            break
    else:
        speak("Id not found")


def update_Phone():
    global Employee_Phone, Employee_id
    i_d = input("Enter The Employee ID :")
    for i in range(0, len(Employee_id)):
        if (i_d == Employee_id[i]):
            print("You want to update Phone No. of ", Employee_name[i])
            print("The Employee present name is :", Employee_name[i])
            em_phone3 = (input("Enter New employee phone no.:"))
            check = em_phone3.isdigit()
            if (check == True):
                em_phone4 = int(em_phone3)
                if (em_phone4 > 999999999) and (em_phone4 < 10000000000):
                    Employee_Phone[i] = em_phone3
                    speak("Detail updated successfully")
                else:
                    print("\nPhone no not updated because it does not contain 10 digit it is ",
                          len(str(em_phone3)), "digit no")
                    update_Phone()
            else:
                speak("Please, Enter only Numeric value")
                update_Phone()
            break
    else:
        speak("Id not found")


def recover_data():
    global Employee_name, Employee_id, Employee_address, Employee_Phone, Employee_salary, Employee_post, Employee_gmail, recycle_Employee_name, recycle_Employee_id, recycle_Employee_address, recycle_Employee_Phone, recycle_Employee_salary, recycle_Employee_post, recycle_Employee_gmail
    a = input("Enter the Id of Employee whom data you want to recover :")
    for i in range(0, len(recycle_Employee_id)):
        if (a == recycle_Employee_id[i]):
            Employee_Phone.append(recycle_Employee_Phone[i])
            Employee_name.append(recycle_Employee_name[i])
            Employee_post.append(recycle_Employee_post[i])
            Employee_id.append(recycle_Employee_id[i])
            Employee_gmail.append(recycle_Employee_gmail[i])
            Employee_address.append(recycle_Employee_address[i])
            Employee_salary.append(recycle_Employee_salary[i])
            recycle_Employee_Phone.pop(i)
            recycle_Employee_name.pop(i)
            recycle_Employee_post.pop(i)
            recycle_Employee_id.pop(i)
            recycle_Employee_gmail.pop(i)
            recycle_Employee_address.pop(i)
            recycle_Employee_salary.pop(i)
            speak("Data recovered")
            break
    else:
        speak("Id not found")


def empty_bin():
    global recycle_Employee_name, recycle_Employee_id, recycle_Employee_address, recycle_Employee_Phone, recycle_Employee_salary, recycle_Employee_post, recycle_Employee_gmail
    count = len(recycle_Employee_id)
    import os
    if (count != 0):
        print("You really want to delete all data in recycle bin ?")
        print("If Yes type Yes/yes/Y/y or If No type No/no/N/n")
        verify = input("Enter You choice to continue process:")
        if (verify == "Yes" or verify == "Y" or verify == "yes" or verify == "y"):
            while(len(recycle_Employee_id) > 0):
                try:
                    os.remove(
                        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+recycle_Employee_id[0]+"0.dat")
                except:
                    pass
                try:
                    os.remove(
                        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+recycle_Employee_id[0]+"1.dat")
                except:
                    pass
                try:
                    os.remove(
                        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+recycle_Employee_id[0]+"2.dat")
                except:
                    pass
                recycle_Employee_id.pop(0)
            recycle_Employee_Phone.clear()
            recycle_Employee_name.clear()
            recycle_Employee_post.clear()
            recycle_Employee_gmail.clear()
            recycle_Employee_address.clear()
            recycle_Employee_salary.clear()
            speak("Recycle bin empty successfully...")
            clean_2()
        elif (verify == "No" or verify == "N" or verify == "no" or verify == "n"):
            speak("Proccess canceled...")
            clean_2()
            work_on_choice_4()
        else:
            clean()
            speak("Invalid input")
            empty_bin()
    else:
        print("\nRecycle bin is already empty............")
        speak("Recycle bin is already empty............")
        clean_2()


def delete():
    import shutil
    import time
    speak("Deleting all data")
    shutil.rmtree(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user)
    clean()
    speak("log out")
    clean()
    all_try_except()
    try_except_file()
    cache_list.append("0100001101100001011000110110100001100101")
    write_cache()
    speak("Please, Relogin account")
    clean()
    work_on_choice_0()


def delete_employee_detail():
    global Employee_name, Employee_id, Employee_address, Employee_Phone, Employee_salary, Employee_post, Employee_gmail, recycle_Employee_name, recycle_Employee_id, recycle_Employee_address, recycle_Employee_Phone, recycle_Employee_salary, recycle_Employee_post, recycle_Employee_gmail
    i_d = input("Enter the Employee ID whose detail you want to delete :")
    for i in range(0, len(Employee_id)):
        if (i_d == Employee_id[i]):
            print("\nYou really want to delete detail of ",
                  Employee_name[i], " ?")
            print("If Yes type Yes/yes/Y/y or If No type No/no/N/n")
            verify = input("Enter You choice to continue process:")
            if (verify == "Yes" or verify == "Y" or verify == "yes" or verify == "y"):
                clean()
                print("\nDetails of ",
                      Employee_name[i], " deleted successfully...")
                print("\nIn any case of recovery you can recover it from recycle bin.")
                speak("Detail deleted successfully")
                # recycle bin
                recycle_Employee_Phone.append(Employee_Phone[i])
                recycle_Employee_name.append(Employee_name[i])
                recycle_Employee_post.append(Employee_post[i])
                recycle_Employee_id.append(Employee_id[i])
                recycle_Employee_gmail.append(Employee_gmail[i])
                recycle_Employee_address.append(Employee_address[i])
                recycle_Employee_salary.append(Employee_salary[i])
                # removing employee data
                Employee_Phone.pop(i)
                Employee_name.pop(i)
                Employee_post.pop(i)
                Employee_id.pop(i)
                Employee_gmail.pop(i)
                Employee_address.pop(i)
                Employee_salary.pop(i)
                break
            elif (verify == "No" or verify == "N" or verify == "no" or verify == "n"):
                speak("Detail delitation canceled")
                clean_2()
                work_on_choice_2()
            else:
                speak("Invalid input")
                work_on_choice_2()
    else:
        speak("Id not found")

# Salary management system


def print_transaction():
    global Employee_id, Employee_name, Date, Time, Amount
    i_d = input(
        "Enter the ID of Employee whom transaction details you want to print :")
    for i in range(0, len(Employee_id)):
        if i_d == Employee_id[i]:
            try:
                read_file2(i_d)
            except:
                speak("No data found..")
                break
            speak("printing transaction of "+Employee_name[i])
            print("All transaction of ", Employee_name[i])
            print("Name :", Employee_name[i])
            print("Date       ---> Time         ---> Amount Transfered")
            if (len(Date) != 0):
                for i in range(0, len(Date)):
                    print(Date[i], "--->", Time[i], " --->", Amount[i])
            else:
                speak("No Transaction found")
            break
    else:
        speak("Id not found")
        clean_2()
        work_on_choice_5()
    Date.clear()
    Amount.clear()
    Time.clear()


def add_transaction():
    import datetime
    global Employee_id, Date, Amount, Time
    i_d = input(
        "Enter the ID of Employee whom transaction details you want to add :")
    for i in range(0, len(Employee_id)):
        if i_d == Employee_id[i]:
            speak("You want to add transaction of "+Employee_name[i])
            try:
                read_file2(i_d)
            except:
                pass
            x = datetime.datetime.now()
            hour = x.strftime("%I")
            minut = x.strftime("%M")
            sec = x.strftime("%S")
            am_pm = x.strftime("%p")
            date_ = x.strftime("%d")
            month = x.strftime("%m")
            year = x.strftime("%Y")
            date = date_+"/"+month+"/"+year
            time = hour+":"+minut+":"+sec+" "+am_pm
            print("Date : ", date)
            Date.append(date)
            print("Time : ", time)
            Time.append(time)
            amount = input("Enter Amount transfered:")
            Amount.append(amount)
            store_data2(i_d)
            speak("Detail added Succesfully")
            break
    else:
        speak("Id not found")
        clean_2()
        work_on_choice_5()
    Date.clear()
    Amount.clear()
    Time.clear()


def update_transaction():
    global Employee_id, Date, Amount, Time
    i_d = input(
        "Enter the ID of Employee whom transaction details you want to update :")
    for i in range(0, len(Employee_id)):
        if i_d == Employee_id[i]:
            try:
                read_file2(i_d)
            except:
                speak("No data found for delete")
                break
            if (len(Date) != 0):
                speak("You want to update transaction of "+
                      Employee_name[i])
                clean()
                print("Date       ---> Time         ---> Amount Transfered")
                for i in range(0, len(Date)):
                    print(Date[i], "--->", Time[i], " --->", Amount[i])
            else:
                speak("No Transaction found")
                break
            date = input("Enter The Date of transaction you want to delete :")
            time = input("Emter The Time of transaction you want to delete :")
            for i in range(0, len(Date)):
                if (date == Date[i] and time == Time[i]):
                    amount = input("Enter new Transaction")
                    Amount[i] = amount
                    speak("Detail update Succesfully")
                    break
            else:
                speak("Date or time not found")
            store_data2(i_d)
            break
    else:
        speak("Id not found")
        clean_2()
        work_on_choice_5()
    Date.clear()
    Amount.clear()
    Time.clear()


def delete_transaction():
    import pickle
    global Employee_id, Date, Amount, Time
    i_d = input(
        "Enter the ID of Employee whom transaction details you want to delete :")
    for i in range(0, len(Employee_id)):
        if i_d == Employee_id[i]:
            read_file2(i_d)
            if (len(Date) != 0):
                print("Name :", Employee_name[i])
                print("Date       ---> Time         ---> Amount Transfered")
                speak("You want to update transaction of " +
                      Employee_name[i])
                for i in range(0, len(Date)):
                    print(Date[i], "--->", Time[i], " --->", Amount[i])
            else:
                speak("No Transaction found")
                break
            date = input("Enter The Date of transaction you want to delete :")
            time = input("Emter The Time of transaction you want to delete :")
            for i in range(0, len(Date)):
                if (date == Date[i] and time == Time[i]):
                    Date.pop(i)
                    Time.pop(i)
                    Amount.pop(i)
                    speak("Detail deleted ")
                    break
            else:
                speak("Date or time not found")
            store_data2(i_d)
            break
    else:
        speak("Id not found")
        clean_2()
        work_on_choice_5()
    Date.clear()
    Amount.clear()
    Time.clear()


# ------------------------
def add_cache2():
    try:
        read_cache()
    except:
        speak("Enter number present in front of option of your choice ")
        cache_list.append("0100001101100001011000110110100001100101")
        write_cache()


def read_cache():
    import pickle
    global cache_list
    f = open(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Important-folder\\data_file.dat", "rb")
    cache_list = pickle.load(f)
    f.close()


def write_cache():
    import pickle
    global cache_list
    f = open(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Important-folder\\data_file.dat", "wb")
    pickle.dump(cache_list, f)
    f.close()


def create_cache():
    global cache
    f = open(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Important-folder\\data_file.dat", "a")
    f.close()


def create_folder_EDMSDF():
    import os
    os.makedirs(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1")


def create_folder_EDMSDF_1():
    import os
    os.makedirs(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1")


def create_folder_RDMSDF():
    import os
    os.makedirs(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2")


def create_folder_SDMSDF():
    import os
    os.makedirs(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3")


def create_folder_cache():
    import os
    os.makedirs(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Important-folder")


def cache():
    import time
    try:
        read_cache()
        clean()
        print("Welcome User to The Account")
        speak("Welcome User to The Account")
        try:
            check_EMSDB_file_present()
        except:
            speak("Error occours")
        speak("Opening program interface")
    except:
        clean()
        print("Welcome User to The Account")
        speak("Welcome User to The Account")
        speak("my self adiutor and i am always with you as a assistant while you are using this program ")
        speak("Opening program interface")
        try_except_file()
        create_cache()


def check_EMSDB_file_present():
    import os
    import shutil
    global Employee_id, recycle_Employee_id
    a1 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1\\employee_name.dat")
    a2 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1\\employee_gmail.dat")
    a3 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1\\employee_post.dat")
    a4 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1\\employee_id.dat")
    a5 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1\\employee_address.dat")
    a6 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1\\employee_phone_no.dat")
    a7 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-1\\employee_salary.dat")
    if (a1 == True and a2 == True and a3 == True and a4 == True and a5 == True and a6 == True and a7 == True):
        pass
    else:
        print("Warning: You delete some nessasary file which caussing error \nTo start program type yes.If you type yes all data deleted ,else you enter anything then data not delete but program may be crash any time or data may be lost")
        a = input("Enter you input :")
        if (a == "Yes" or a == "Y" or a == "yes" or a == "y"):
            shutil.rmtree(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user)
            create_folder_EDMSDF()
            create_folder_SDMSDF()
            create_folder_RDMSDF()
            create_folder_cache()
            creat_file()
        else:
            pass
    # recycle bin data
    r1 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2\\recycle_employee_name.dat")
    r2 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2\\recycle_employee_gmail.dat")
    r3 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2\\recycle_employee_post.dat")
    r4 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2\\recycle_employee_id.dat")
    r5 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2\\recycle_employee_address.dat")
    r6 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2\\recycle_employee_phone_no.dat")
    r7 = os.path.exists(
        "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2\\recycle_employee_salary.dat")
    if (r1 == True and r2 == True and r3 == True and r4 == True and r5 == True and r6 == True and r7 == True):
        try_except_file()
        pass
    else:
        print("Warning: You delete some nessasary file of Recycle bin which caussing error \nTo start program type yes.If you type yes all data in recycle bin deleted ,else you enter anything then data not delete but program may be crash any time or data may be lost")
        a = input("Enter you input :")
        if (a == "Yes" or a == "Y" or a == "yes" or a == "y"):
            shutil.rmtree(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-2")
            create_folder_RDMSDF()
            creat_file()
        else:
            pass
    if (len(Employee_id) != 0):
        for j in range(0, len(Employee_id)):
            i = Employee_id[j]
            d11 = os.path.exists(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+str(i)+"0.dat")
            d21 = os.path.exists(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+str(i)+"1.dat")
            d31 = os.path.exists(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+str(i)+"2.dat")
            if (d11 == True and d21 == True and d31 == True):
                pass
            else:
                print("Warning:You delete some nessasary file of salary transaction of "+Employee_id[j]+" which caussing error \nTo start program type yes.If you type yes all transaction of " +
                      Employee_id[j]+" deleted ,else you enter anything then data not delete but program may be crash any time or data may be lost")
                a = input("Enter you input :")
                if (a == "Yes" or a == "Y" or a == "yes" or a == "y"):
                    try:
                        os.remove(d11)
                    except:
                        pass
                    try:
                        os.remove(d21)
                    except:
                        pass
                    try:
                        os.remove(d31)
                    except:
                        pass
                    creat_file2(i)
                else:
                    pass
    else:
        pass
    if(len(recycle_Employee_id) != 0):
        for j in range(0, len(recycle_Employee_id)):
            i = recycle_Employee_id[j]
            s11 = os.path.exists(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+str(i)+"0.dat")
            s21 = os.path.exists(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+str(i)+"1.dat")
            s31 = os.path.exists(
                "C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-"+user+"\\Data-File-3\\"+str(i)+"2.dat")
            if (s11 == True and s21 == True and s31 == True):
                pass
            else:
                print("Warning:You delete some nessasary file of salary transaction of "+Employee_id[j]+" of recycle bin which caussing error \nTo start program type yes.If you type yes all transaction of " +
                      Employee_id[j]+" deleted ,else you enter anything then data not delete but program may be crash any time or data may be lost")
                if (a == "Yes" or a == "Y" or a == "yes" or a == "y"):
                    try:
                        os.remove(s11)
                    except:
                        pass
                    try:
                        os.remove(s21)
                    except:
                        pass
                    try:
                        os.remove(s31)
                    except:
                        pass
                    creat_file2(i)
                else:
                    pass
    else:
        pass


def read_file2(i_d):
    import pickle
    global Date, Amount, Time
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"0.dat", "rb")
    Date = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"1.dat", "rb")
    Amount = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"2.dat", "rb")
    Time = pickle.load(f)
    f.close()


def store_data2(i_d):
    import pickle
    global Date, Amount, Time
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"0.dat", "wb")
    pickle.dump(Date, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"1.dat", "wb")
    pickle.dump(Amount, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"2.dat", "wb")
    pickle.dump(Time, f)
    f.close()


def creat_file2(i_d):
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"0.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"1.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-3\\"+i_d+"2.dat", "a")
    f.close()


def creat_file():
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_name.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_gmail.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_post.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_id.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_address.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_phone_no.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_salary.dat", "a")
    f.close()
    # recycle_bin
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_name.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_gmail.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_post.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_id.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_address.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_phone_no.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_salary.dat", "a")
    f.close()


def read_file():
    import pickle
    global Employee_name, Employee_id, Employee_address, Employee_Phone, Employee_salary, Employee_post, Employee_gmail, recycle_Employee_name, recycle_Employee_id, recycle_Employee_address, recycle_Employee_Phone, recycle_Employee_salary, recycle_Employee_post, recycle_Employee_gmail
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_name.dat", "rb")
    Employee_name = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_gmail.dat", "rb")
    Employee_gmail = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_post.dat", "rb")
    Employee_post = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_id.dat", "rb")
    Employee_id = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_address.dat", "rb")
    Employee_address = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_phone_no.dat", "rb")
    Employee_Phone = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_salary.dat", "rb")
    Employee_salary = pickle.load(f)
    f.close()
    # recycle_bin
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_name.dat", "rb")
    recycle_Employee_name = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_gmail.dat", "rb")
    recycle_Employee_gmail = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_post.dat", "rb")
    recycle_Employee_post = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_id.dat", "rb")
    recycle_Employee_id = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_address.dat", "rb")
    recycle_Employee_address = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_phone_no.dat", "rb")
    recycle_Employee_Phone = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_salary.dat", "rb")
    recycle_Employee_salary = pickle.load(f)
    f.close()


def store_data():
    import pickle
    global Employee_name, Employee_id, Employee_address, Employee_Phone, Employee_salary, Employee_post, Employee_gmail, recycle_Employee_name, recycle_Employee_id, recycle_Employee_address, recycle_Employee_Phone, recycle_Employee_salary, recycle_Employee_post, recycle_Employee_gmail
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_name.dat", "wb")
    pickle.dump(Employee_name, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_gmail.dat", "wb")
    pickle.dump(Employee_gmail, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_post.dat", "wb")
    pickle.dump(Employee_post, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_id.dat", "wb")
    pickle.dump(Employee_id, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_address.dat", "wb")
    pickle.dump(Employee_address, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_phone_no.dat", "wb")
    pickle.dump(Employee_Phone, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-1\\employee_salary.dat", "wb")
    pickle.dump(Employee_salary, f)
    f.close()
    # recycle_bin
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_name.dat", "wb")
    pickle.dump(recycle_Employee_name, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_gmail.dat", "wb")
    pickle.dump(recycle_Employee_gmail, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_post.dat", "wb")
    pickle.dump(recycle_Employee_post, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_id.dat", "wb")
    pickle.dump(recycle_Employee_id, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_address.dat", "wb")
    pickle.dump(recycle_Employee_address, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_phone_no.dat", "wb")
    pickle.dump(recycle_Employee_Phone, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-" +
             user+"\\Data-File-2\\recycle_employee_salary.dat", "wb")
    pickle.dump(recycle_Employee_salary, f)
    f.close()


# Exeption handaling for "EOFError: Ran out of input"
def all_try_except():
    try_except_EDMSDF()
    try_except_SDMSDF()
    try_except_RDMSDF()
    try_except_cache()


def creat_uid_pass():
    import pickle
    global user_id, user_pass, sec_que1_list, sec_que2_list
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_a.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_b.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_c.dat", "a")
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_d.dat", "a")
    f.close()


def read_uid_pass():
    import pickle
    global user_id, user_pass, sec_que1_list, sec_que2_list
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_a.dat", "rb")
    user_id = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_b.dat", "rb")
    user_pass = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_c.dat", "rb")
    sec_que1_list = pickle.load(f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_d.dat", "rb")
    sec_que2_list = pickle.load(f)
    f.close()


def store_uid_pass():
    import pickle
    global user_id, user_pass, sec_que1_list, sec_que2_list
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_a.dat", "wb")
    pickle.dump(user_id, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_b.dat", "wb")
    pickle.dump(user_pass, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_c.dat", "wb")
    pickle.dump(sec_que1_list, f)
    f.close()
    f = open("C:\\Employee-management-system-data-base-main-folder\\Employee-management-system-data-base-main-folder-1\\data_file_d.dat", "wb")
    pickle.dump(sec_que2_list, f)
    f.close()


def try_except_file():
    try:
        read_file()
    except:
        creat_file()


def try_except_file_uid_pass():
    try:
        read_uid_pass()
    except:
        creat_uid_pass()


def try_except_EDMSDF():
    try:
        create_folder_EDMSDF()
    except:
        pass


def try_except_EDMSDF_1():
    try:
        create_folder_EDMSDF_1()
    except:
        pass


def try_except_SDMSDF():
    try:
        create_folder_SDMSDF()
    except:
        pass


def try_except_RDMSDF():
    try:
        create_folder_RDMSDF()
    except:
        pass


def try_except_cache():
    try:
        create_folder_cache()
    except:
        pass


# All list to be us in this program
Employee_name = []
Employee_post = []
Employee_id = []
Employee_address = []
Employee_gmail = []
Employee_Phone = []
Employee_salary = []
recycle_Employee_name = []
recycle_Employee_post = []
recycle_Employee_id = []
recycle_Employee_address = []
recycle_Employee_gmail = []
recycle_Employee_Phone = []
recycle_Employee_salary = []
cache_list = []
Date = []
Amount = []
Time = []
user_id = []
user_pass = []
sec_que1_list = []
sec_que2_list = []
em_id2 = None
user = None
try:
    main()
except Exception as excep:
    print(f"Error:-{excep}")
    speak("Due to some error the program is terminated .we are ashamed for it .you may report the error to developing team ")
    clean_2()