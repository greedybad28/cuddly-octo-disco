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
time_now =  datetime.datetime.now()
month = int(time_now.strftime("%m"))
print(month)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day_value = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day_value = 30


print(max_day_value)


# time_now =datetime.datetime.now()
# print()


def ubuntu_filery():
    date = time_now.strftime("%d")
    no_of_files = int(input("Enter the number of files you need : "))
    files_needed = max_day_value - date
    print(f"You would need {files_needed} more files to suffice for this month's journal Progress.\n") 
    decision = str(input(f"DO you wanna continue makng {files_needed} files ??\n type YES or NO"))
    if decision== "YES" or "yes" or "Yes":
        for i in range(date,max_day_value+1):
            pathh = f"home/greedybad/Desktop/test/filename-{date}.{month}.2024.md"
            os.open(path=pathh,flags=os.O_CREAT)
            print(f"Created the file ")
    else:
       print("Pinne enthina myre program run aakye")

def windows_filery():
    date = int(time_now.strftime("%d"))
    # Num_of_files would be the same as no_of_files variable in ubuntu_filery()
    num_of_files = max_day_value - date
    print(f"You would need {num_of_files} more files to suffice for this month's journal Progress....")
    decision = str(input("Do you want to continue making {files_needed} files\n TYPE YES OR NO : "))
    if decision == "YES" or "Yes" or "yes":
        input_path = str(input("Enter the path you need to create the files in\n N.B : Please use '/' when seperating directories with a slash :  "))
        for i in range(date,max_day_value+1):
            pathh = f"filename.{i}.{month}.2024.md"
            os.open(path=pathh,flags=os.O_CREAT)
            print(f"Created the file {pathh[10:]} ")
    else:
        print("WHY BRO WHYYY")
if os.name == "nt":
    print("Detected that you're on a Windows machine, Continuing with windows compatible script")
    time.sleep(1)
    windows_filery()
else:
    ubuntu_filery()




