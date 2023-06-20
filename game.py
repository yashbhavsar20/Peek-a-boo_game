import os
import random
import time
import sys
from grid import *







def print_menu():
     print("1. Let me select two elements\n2. Uncover one element for me\n3. I give up - reveal the grid\n4. New game\n5. Exit")
def print_heading():
    print("      ----------------      ")
    print("      |  PEEK-A-Boo  |      ")
    print("      ----------------      ")
    
def main(arg1):
     x=1
     while(True):
        if(x==1):
            grid_input=arg1
            p1 = grid()
            p1.Initialize(int(arg1))
            x=2
    
        print_heading()
        p1.make_grid(int(arg1))
        print_menu()
        while(True):
            try:
                select_case=int(input("select:"))
                pass
            except:
                print("Please enter correct values")
                continue
            if(select_case>0 and select_case<=5):
                    break
            else:
                print("Please enter correct values")
        if(select_case==1):
            while(True):
                        a1=input("Enter  first Cell Coordinates: (e.g.,a0):")
                        if(len(a1)==2):
                            pass
                        else:
                            print("please enter the correct values")
                            continue
                        try:
                            check1=ord(a1[0].lower())
                            check2=int(a1[1])
                        except:
                            print("please enter correct values")
                            continue
                        if((check1>=97 and check1<=97+int(grid_input)) and (check2>=0 and check2<0+int(grid_input))):
                             pass
                        else:
                             if not ((check1>=97 and check1<=97+int(grid_input)) or (check2>=0 and check2<0+int(grid_input))):
                                 print("Input Error: Both Row and column entry is out of range for this grid! Please try again")
                             elif not (check1>=97 and check1<=97+int(grid_input)):
                                 print("Input Error: Column entry is out of range for this grid! Please try again")
                             else:
                                 print("Input Error: Row entry is out of range for this grid! Please try again")
                             continue
                        break
            while(True):
                        a2=input("Enter second Cell Coordinates: (e.g.,a0):")
                        if(len(a2)==2):
                            pass
                        else:
                            print("please enter the correct values")
                            continue
                        try:
                            check3=ord(a2[0].lower())
                            check4=int(a2[1])
                        except:
                            print("please enter correct values")
                            continue
                        if((check3>=97 and check3<=97+int(grid_input)) and (check4>=0 and check4<0+int(grid_input))):
                             pass
                        else:
                             if not ((check3>=97 and check3<=97+int(grid_input)) or (check4>=0 and check4<0+int(grid_input))):
                                 print("Input Error: Both Row and column entry is out of range for this grid! Please try again")
                             elif not (check3>=97 and check3<=97+int(grid_input)):
                                 print("Input Error: Column entry is out of range for this grid! Please try again")
                             else:
                                 print("Input Error: Row entry is out of range for this grid! Please try again")
                             continue
                        break
            if(a1==a2):
                 print("Both coordinates are same please re-try")
                 time.sleep(2)
                 
                 if(os.name=="nt"):
                    os.system("cls")
                 else:
                    os.system("clear")
                 continue
            if(os.name=="nt"):
                os.system("cls")
            else:
                os.system("clear")
            p1.values_grid(check1,check2,check3,check4)
            time.sleep(2)
            if(os.name=="nt"):
                os.system("cls")
            else:
                os.system("clear")
            

        elif(select_case==2):
                while(True):
                        a1=input("Enter Cell Coordinates: (e.g.,a0):")
                        if(len(a1)==2):
                            pass
                        else:
                            print("please enter the correct values")
                            continue
                        try:
                            check1=ord(a1[0].lower())
                            check2=int(a1[1])
                        except:
                            print("please enter correct values")
                            continue
                        if((check1>=97 and check1<=97+int(grid_input)) and (check2>=0 and check2<0+int(grid_input))):
                             pass
                        else:
                             if not ((check1>=97 and check1<=97+int(grid_input)) or (check2>=0 and check2<0+int(grid_input))):
                                 print("Input Error: Both Row and column entry is out of range for this grid! Please try again")
                             elif not (check1>=97 and check1<=97+int(grid_input)):
                                 print("Input Error: Column entry is out of range for this grid! Please try again")
                             else:
                                 print("Input Error: Row entry is out of range for this grid! Please try again")
                             continue
                        break
        
                   
                if(os.name=="nt"):
                    os.system("cls")
                else:
                    os.system("clear")
                p1.uncover_one_element(check1,check2)
                time.sleep(2)
                if(os.name=="nt"):
                    os.system("cls")
                else:
                    os.system("clear")
                continue


        elif(select_case==3):
            if(os.name=="nt"):
                print("hello")
                os.system("cls")
            else:
                os.system("clear")
            p1.give_up()
            time.sleep(2)
            
            if(os.name=="nt"):
                print("hello")
                os.system("cls")
            else:
                os.system("clear")
            
            p1 = grid()
            p1.Initialize(int(arg1))

        elif(select_case==4):
            if(os.name=="nt"):
                os.system("cls")
            else:
                os.system("clear")
            p1 = grid()
            p1.Initialize(int(arg1))
            
        else:
            print("Thank you for playing PEEK-A-BOO")
            time.sleep(1)
            if(os.name=="nt"):
                os.system("cls")
            else:
                os.system("clear")
            sys.exit()


if __name__=="__main__":
        if not len(sys.argv)==2:
            print("Arguments empty")
            sys.exit(0)
        else:
            if sys.argv[1].isdigit():
                 if(int(sys.argv[1])%2==0):
                    main(sys.argv[1])
                 else:
                    print("Invalid range")
                    sys.exit(0)
            else:
                 print("Invalid range")
                 sys.exit(0)
                 
                         
        
                 
            
            
         


