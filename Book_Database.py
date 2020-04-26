#import Sqlite_connection

from Sqlite_connection import database_tasks
            
class Maintain_Database(database_tasks):
    
    def addBook(self):
        print("Enter the name of Book:")
        self.bookname=input()
        print("Enter the name of writer:")
        self.writer=input()
        conn = super().create_connection()
        super().insert(conn,"Book_database", self.bookname , self.writer)
        super().connection_close(conn) 
        return
    
    def deleteBook(self):
        print("Enter the name of delete Book:")
        self.bookname=input()
        conn = super().create_connection()
        super().delete(conn,"Book_database", self.bookname)
        super().connection_close(conn) 
        return self.bookname
    
    def listBook(self):
        conn = super().create_connection()
        super().selectall(conn,"Book_database")
        super().connection_close(conn) 
        return None

def main():            
    Database= Maintain_Database()
    done=False
    while done==False:
        print(""" ======BOOK DATABASE MENU=======
              1. Add Book to Database
              2. Delete Book
              3. List Book
              4. Exit
              """)
        
        choice=int(input("Enter Choice:"))
        
        if choice==1:
            Database.addBook()
        elif choice==2:
            Database.deleteBook()
        elif choice==3:
            Database.listBook()
        elif choice==4:
             # print("Thank for you using the library management system")
            done = True
        else:
            print("Please select the correct option")
                  
if __name__=="__main__":
    main()
    
