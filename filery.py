import os
import time
import datetime
# os.open(path="/home/greedybad/Desktop/remo.txt",flags=os.O_CREAT)

print("Welcome to Journal File creator for Obsidian")
# time.sleep(2)


######################################################################################
# def maketh():
#     no_of_files = int(input("Enter the number of files you need : "))
#     n = no_of_files
    
#     for i in range(1, n +1):
#         pathh = f"/home/greedybad/Desktop/test/{i}.txt"
#         os.open(path=pathh,flags=os.O_CREAT)
#         print(f"Created file {i}.txt")

# if __name__ == "__main__":
#     maketh()
#############################################################################
## This is the base program... Let's see how we can build it 

# def maketh():
#     no_of_files = int(input("Enter the number of files you need : "))
#     n = no_of_files
    
#     for i in range(1, n +1):
#         pathh = f"/home/greedybad/Desktop/test/filename - {i}.txt"
#         os.open(path=pathh,flags=os.O_CREAT)
#         print(f"Created file {i}.txt")
############################################################3
time_now =  datetime.datetime.now()
month = int(time_now.strftime("%m"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day_value = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day_value = 30
##################################################### I mean.. why are these up here??
# time_now =datetime.datetime.now()
# print()
def decision(files_needed):
    decision = str(input(f"DO you wanna continue makng {files_needed} files ??\n type YES or NO : "))
    return decision

def ubuntu_filery():
    date = int(time_now.strftime("%d"))
    files_needed = max_day_value - date
    print(f"You would need {files_needed} more files to suffice for this month's journal Progress.\n") 
    choice = decision(files_needed)
    if choice.lower() =="yes":
        try:

            input_path = str(input("Enter the path you need to create the files in\n Please use '/' when seperating directories\n \nEg:home/user/Desktop/test/ \n \n Make sure you end with a slash(/) \n \n Enter your path : "))
        except FileNotFoundError:
            print("Enter correct path")
            decision(files_needed)
        for i in range(date,max_day_value+1):
            pathh = f"{input_path}filename-{i}.{month}.2024.md"
            os.open(path=pathh,flags=os.O_CREAT)
            print(f"Created the file filename-{i}.{month}.2024.md")
        print(f"All the files are stored in the path - {pathh[:-21]} ")
    elif choice.lower()=="no":
       print("Okdamone")
    else:
       
       print("Pinne enthina myre program run aakye")

def windows_filery():
    date = int(time_now.strftime("%d"))
    # Num_of_files would be the same as no_of_files variable in ubuntu_filery()
    num_of_files = max_day_value - date
    print(f"You would need {num_of_files} more files to suffice for this month's journal Progress....")
    decision = str(input("Do you want to continue making {files_needed} files\n TYPE YES OR NO : "))
    if decision.lower()=="yes":
        input_path = str(input("Enter the path you need to create the files in\n N.B : Please use '/' when seperating directories with a slash\n\ \nexampple : R:/   Enter your Path : "))
        for i in range(date,max_day_value+1):
            pathh = f"{input_path}filename.{i}.{month}.2024.md"
            os.open(path=pathh,flags=os.O_CREAT)
            print(f"Created the file filename-{i}.{month}.2024.md ")
    else:
        print("WHY BRO WHYYY")
if os.name == "nt":
    print("Detected that you're on a Windows machine, Continuing with windows compatible script")
    time.sleep(1)
    windows_filery()
else:
    print("Detected that you're on an a Unix based system, Continuing with Unix based script")
    time.sleep(1)
    ubuntu_filery()




