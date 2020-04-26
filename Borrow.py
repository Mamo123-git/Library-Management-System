
from Sqlite_connection import database_tasks

class Library(database_tasks):
    
    def lendBook(self):
        
        print("Enter your studentId: ")
        self.studentId=input()        
        print("Enter the name of book to issue:")
        self.book=input()
        
        conn = super().create_connection()
        self.studentflag = super().isStudentEnrolled(conn,self.studentId)
        
        if self.studentflag == "true":
             self.bookflag = super().isbookavailable(conn,self.book)
             
             if self.bookflag > 0:
                 
                 super().insert_bookIssued(conn,"Book_Issued", self.studentId , self.bookflag)
                 # update the availability of the book in the Book Database                 
                 super().updatebook(conn,"n", self.book)                 
                 print("The book has been issued")             
             else:
                 print("Sorry the book is not available")                 
        else:
            print ( " You have not enrolled yourself. Please enroll yourself :)" )
        super().connection_close(conn)     
        return None
    
    
    def returnbook(self):
        print("Enter the name of the Book to return:")
        self.bookname=input()        
        conn = super().create_connection()        
        super().updatebook(conn,"y", self.bookname)
        super().connection_close(conn)        
        return None
    
    # display all the books in the library
    
    def displayAvailablebooks(self):
        conn = super().create_connection()        
        super().selectavailablebooks(conn)
        super().connection_close(conn)         
        return None
    
    def listallbooksissued(self):
        conn = super().create_connection()        
        super().selectallbooksissued(conn)
        super().connection_close(conn)         
        return None

def main():            
    library= Library()
    done=False
    while done==False:
       print(""" ======BORROW MENU=======
              1. Display all available books
              2. Request a book
              3. Return a book
              4. Display all Books Issued 
              5. Exit
              """)
       
       choice=int(input("Enter Choice:"))
       if choice==1:
           library.displayAvailablebooks()
       elif choice==2:
           library.lendBook()
       elif choice==3:
           library.returnbook()
       elif choice == 4:
           library.listallbooksissued()
       elif choice==5:
           #print("Thank for you using the library management system")
           done = True
       else:
            print("Please select the correct option")
                  
                  
if __name__=="__main__":
    main()

