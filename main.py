import json
import time

try:
    with open("students.json","r") as file:
        students = json.load(file)
except:
    with open("students.json","w") as file:
        json.dump([],file,indent=4)
    with open("students.json","r") as file:
        students = json.load(file)
print("********** Welcome to our Students Management app **********\n") 
time.sleep(2)

def add_student(name,age,hobby,field):
    students.append({"name":name,"age":age,"hobby":hobby,"field":field})

def add_student_option():
        
        name = input("Enter the student's name:\n ").lower()
        while True:
            age = input("Enter the student's age:\n ")
            try:
                age = int(age)
                break
            except:
                print("Please type a number")
                time.sleep(1)
                

        hobby = input("Enter the student's hobby:\n ")
        field = input("Enter the student's field:\n ")
        add_student(name,age,hobby,field)
        with open("students.json","w") as file:
            json.dump(students,file,indent=4)
        print("Added Successfully..")
        time.sleep(1)
        continuing_choice()
        exit()
def delete_student():
        deleted_student = input("Enter the name of the student you want to delete: \n")
        student = next((p for p in students if p["name"]==deleted_student),None)
        for index,dictionary in enumerate(students):
            if student!=None and dictionary["name"] == deleted_student:
                students.pop(index)
                with open("students.json","w") as file:
                    json.dump(students,file,indent=4)
                print("Deleting..")
                time.sleep(2)
                print("Deleted Successfully")
                time.sleep(0.5)
                continuing_choice()
        if student == None:
                print("Please Enter a valid name..")
                time.sleep(1.0)
                choice = input("Press Enter to continue or type exit to exit..\n")
                if choice == "":
                    delete_student()
                elif choice.lower() == "exit":
                    print("Exiting...")
                    time.sleep(2)
                    exit()
def edit_student():
    edited_student = input("Enter the name of the student you want to edit:\n")
    student = next((p for p in students if p["name"]==edited_student),None)
    if student == None:
        print("Please enter a valid name..\n")
        time.sleep(1)
        choice = input("Press Enter to continue or type exit to exit..\n")
        if choice == "":
            edit_student()
        elif choice.lower() == "exit":
            print("Exiting...")
            time.sleep(2)
            exit()
    else:
        def choosing_property():
            key=input("Enter the property of the student you want to edit (name,age,hobby,field):\n")
            match key:
                case "name":
                    new_name = input("Enter the new name of the student:\n")
                    student["name"]=new_name
                case "age":
                    new_age = input("Enter the new age of the student:\n")
                    student["age"]=new_age
                case "hobby":
                    new_hobby = input("Enter the new hobby of the student:\n")
                    student["hobby"]=new_hobby
                case "field":
                    new_field = input("Enter the new field of the student:\n")
                    student["field"] = new_field
                case _:
                    print("Please enter a valid property..")
                    time.sleep(1)
                    choosing_property()
        choosing_property()            
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)        
    print("Edited Successfully")  
    time.sleep(1)
    continuing_choice()
def search_student():
    entered_student = input("Enter the name of the student to search:\n").lower()
    student = next((i for i in students if i["name"] == entered_student),None)
    if student == None:
        print("Student not found")
        time.sleep(2)
        choice = input("Press Enter to continue or type exit to exit..\n")
        if choice == "":
            search_student()
        elif choice.lower() == "exit":
            print("Exiting...")
            time.sleep(2)
            exit()
    else:
        for key,value in student.items():
            print(key,":",value)
        time.sleep(2)
        continuing_choice()    
def continuing_choice():
    choice = input("Do you want to continue(y/n):\n")
    if choice.lower() == "y":
        time.sleep(0.5)
        main_menu()
    elif choice.lower() == "n":
        print("Exiting...")
        time.sleep(2)
        exit()
    else:
        print("Please choose a valid option..\n")
        continuing_choice()
def delete_all():
    check = input("Are you sure (y/n):\n")
    if check.lower() == "y":
        students.clear()
        print("Deleting...")
        time.sleep(2)
        with open("students.json","w") as file:
            json.dump(students,file,indent=4)
        print("All done")
        time.sleep(2)
        continuing_choice()
    elif check.lower() == "n":
        print("Okay..")
        time.sleep(1)
        main_menu()    

def main_menu():

    choice = input("choose an option:\n"\
    "1.Add student\n"
    "2.Remove student by name\n"
    "3.Edit student by name\n"
    "4.Search for student by name\n"
    "5.Delete all students\n"
    "6.Exit\n"
    )

    if choice == "1" :
        add_student_option()

    elif choice == "2":
            delete_student()
    elif choice == "3":
            edit_student()
    elif choice == "4":
            search_student()
    elif choice == "5":
            delete_all()        
    elif choice == "6":
        print("Exiting...")
        time.sleep(2)
        exit()

    else:
        print("Please enter a valid number")
        time.sleep(1)
        main_menu()


main_menu()


