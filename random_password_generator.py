import random
import sys
display_coder="This file is made by RJ a low level programer."

list_numeric=list("1234567890")
list_alphabetic=list("abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ")    
list_alphanumeric=list("1234567890"+"abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
list_strong=list("1234567890"+"abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"!@#$%^&*()_+-={}[]|\\:;\'\",.<>/?")
def generate(num_max,list_):
    count=0
    la_st=""
    while count<num_max:
        
            print(random.choice(list_),end=la_st)
            count=count+1

while True:
         
    num_max=0
    usr_inp=5
    
    if __name__ == '__main__':
        print(display_coder)
        print()
        
        print("choose your option")
        
        print()
        print("-------------------------")
        print("1.numeric")
        print("2.alphabhetic")
        print("3.alphanumeric")
        print("4.strong")
        print("5.quit")
        print("-------------------------")
        print()
        
        usr_inp=int(input("enter your option:- "))
        
        if usr_inp==5:
            
            sys.exit()
        
        print()
        num_max=int(input("enter max digit"))
        print()
        
        if usr_inp==1:
            
            generate(num_max,list_numeric)
            print()
            print("")
            
        elif usr_inp==2:
            
            generate(num_max,list_alphabetic)
            print()
            print("")
            
        elif usr_inp==3:
            
            generate(num_max,list_alphanumeric)
            print()
            print("")
            
        elif usr_inp==4:
            
            generate(num_max,list_strong)
            print()
            print("")
            
        elif usr_inp!=1 or usr_inp!=2 or usr_inp!=3 or usr_inp!=4 or usr_inp!=5:
            
            print()
            print("user not define")
            print()
            
        else:
            
            print()
            print("ERROR!")
            print()
                
       
    
            
