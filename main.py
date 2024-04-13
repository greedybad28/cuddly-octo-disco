import os
import time
import datetime
# os.open(path="/home/greedybad/Desktop/remo.txt",flags=os.O_CREAT)


# Make a loop to make 18 of those files with File names differiing

# maybe make it as a function

print("Welcome to Journal File creator for Obsidian")
# time.sleep(2)



# def maketh():
#     no_of_files = int(input("Enter the number of files you need : "))
#     n = no_of_files
    
#     for i in range(1, n +1):
#         pathh = f"/home/greedybad/Desktop/test/{i}.txt"
#         os.open(path=pathh,flags=os.O_CREAT)
#         print(f"Created file {i}.txt")

# if __name__ == "__main__":
#     maketh()
## This is the base program... Let's see how we can build it up and bring in the Date and months in...
# # Goal: create given number of files with the filename = "filename - date.month.year" example : filename.03.04.2024
# filename = "filename"
# month = str(input("Enter the Month you're currently in : "))
# year = str(input("Enter the year you're currently in"))

# def maketh():
#     no_of_files = int(input("Enter the number of files you need : "))
#     n = no_of_files
    
#     for i in range(1, n +1):
#         pathh = f"/home/greedybad/Desktop/test/filename - {i}.txt"
#         os.open(path=pathh,flags=os.O_CREAT)
#         print(f"Created file {i}.txt")
month = int(datetime.datetime.now().strftime("%m"))
print(month)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day_value = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day_value = 30


print(max_day_value)


# time_now =datetime.datetime.now()
# print()
# date = time_now.strftime("%d")


# def make_file():
#     no_of_files = int(input("Enter the number of files you need : "))
#     files_needed = 30