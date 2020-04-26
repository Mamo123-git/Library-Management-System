# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:23:29 2020
@author: Rajesh_Raj
"""

import Membership
import Book_Database
import Borrow

def main():            
    
  done=False
  while done==False:
        print(""" ======LIBRARY MENU=======
              1. Membership
              2. Maintain Book database
              3. Borrow book 
              4. Exit
              """)
       
#            choice=int(input("Enter Choice:"))
        choice=input("Enter Choice:")
        if choice=='1':
            print("Maintan Membership")
            Membership.main()
            
        elif choice=='2':
            print("Maintain Book database")
            Book_Database.main()
                 
        elif choice=='3':
            print("Borrow book")
            Borrow.main()
                 
        elif choice=='4':
           print("Thank for you using the library management system")
           done = True
        else:
            print("Please select the correct option")
                  
                  
if __name__=="__main__":
    main()
    
