#declare Variables

hold = 0 # just a hold for anykey
run_main_menu = 0 # variable for while loop main menu
run_client_menu = 0 # variable for while loop Client menu
user_name = str("")
password = str("")
main_menu_choice = str("") #main menu choice
account_array = [] # array to get the frist two letters from the business name

#import
import os 
import getpass
import sys

#Define Classes

class Person():

  def __init__(self,user_name,password,pin,full_name,address,dob,business_name,stakeholders,type_of_acc):

    self.user_name = user_name
    self.password = password
    self.pin = pin
    self.full_name = full_name
    self.address = address
    self.dob = dob
    self.business_name = business_name
    self.stakeholders = stakeholders
    self.type_of_acc = type_of_acc

    
#Display menu topper
def top_menu():

  print("===============Welcome to===================")
  print("=============GEO Investments================")

  # Display Main Menu
def main_menu():
  
  print("1 - Login                2 create an Account")
  print("=============Type q to Exit=================")
  print("============================================")
   
# Dsiplay Setting Menu
def client_menu():
  
  top_menu()
  print("===============Client Menu==================")
  print("1 - View profile         2 - Change Username")
  print("3 - Change password           4 - Change pin")
  print("5 - Deactivate account                      ")
  print("=======Type q to   return to main menu======")
  print("============================================")
  
def exit_program():

  top_menu()
  print("============================================")
  print("==============Have a great day==============")
  
#display login menu
def login_menu():
  
  top_menu()

  #display Account creation menu
def account_creation_menu():

  top_menu()
  print("============================================")
  print("=====Please enter all infomation============")

  username = input("Plesae enter a User Name                ")
  password = input("Please input your desired password      ")
  pin = input("Please enter a pin number               ")
  full_name = input("Please enter full name                  ")
  address = input("please enter address                    ")
  dob = input("Please enter date of birth mm/dd/yyyy   ")
  business_name = input("Please enter Business name              ")
  stakeholders = input("Please enter stakeholders\nex. name, 50%, name, 30%,               ")
  print("1 - Small Business Class 2 - Medium Business Class")
  print("3 - Large Business Class 4 - Enterprise Business")
  type_of_acc = input("Please enter a choice")
  
  try: #checking for execeptions
        
    file = open("profile.txt","a")
    file.write(username)
    file.write(", ")
    file.write(password)
    file.write(", ")
    file.write(pin)
    file.write(", ")
    file.write(full_name)
    file.write(", ")
    file.write(address)
    file.write(", ")
    file.write(dob)
    file.write(", ")
    file.write(business_name)
    file.write(", ")
    file.write(type_of_acc)
    file.write(", ")
    file.write(stakeholders)
    file.write(", ")
    file.write("\n")
    file.close()
    
  except IOError:
        
    print("\nFile does not exist")
    hold = input("\nPress Enter to countiue")
    os.system('clear') #clear
  
  except: #other errors ocurred
        
    print("\nan execption occurred")
    hold = input("\nPress Enter to countiue")
    os.system('clear') #clear
    
  finally:
    print("info entered")
    hold = input("\nPress Enter to return to main menu")
    os.system('clear')
      
  
def login():
  username = input("Please enter your username ")
  password = input("Please enter your password ") 
  pin = input("Please enter a pin number ")
  
  for line in open("profile.txt","r").readlines(): # Read the lines
    login_info = line.split(", ") # Split the results in a list of two strings
    
    if username == login_info[0] and password == login_info[1]: #check user,pass,pin
    
      if pin == login_info[2]:
        print("Correct credentials!")
        return True
        print("Incorrect credentials.")
        return False

# Main program loops
while (run_main_menu == 0): # Main Menu loop
  
  top_menu()
  main_menu()
  main_menu_choice = str(input("Please Enter a choice ")) #main menu choice
  os.system('clear') #clear
  
  if (main_menu_choice == "1"): 
    
    login_menu() #login menu
    
    if login():
      print("logged in")
      hold = input("\nPress Enter to contiune to Client menu") # press enter to coutinue
      
      while (run_client_menu == 0): #client menu

        client_menu()
        client_menu_choice = str(input("Please Enter a choice "))

        if (client_menu_choice == 1):
          
                    
      
    else:
      print("Login Failed try Again")
      hold = input("\nPress Enter to return to main menu")
      os.system('clear')
    
  if (main_menu_choice == "2"):
    account_creation_menu()
  
  if (main_menu_choice == "q"):
    run_var = 1

exit_program()

 
