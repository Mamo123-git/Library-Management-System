
from Sqlite_connection import database_tasks

class Student(database_tasks):
    
      def addmember(self):
            print("Enter the name of Student:")
            self.name=input()
            conn = super().create_connection()
            super().insert(conn,"Student", self.name)
            super().connection_close(conn)
            return
            
      def deletemember(self):
            print("Give your name to delete:")
            self.name=input()
            conn = super().create_connection()
            super().delete(conn,"Student", self.name)
            super().connection_close(conn) 
            return self.name
    
      def listmember(self):
            conn = super().create_connection()
            super().selectall(conn,"Student")
            super().connection_close(conn) 
            return None
            
def main():            
      student=Student()
      done=False
      while done==False:
            print(""" ======MEMBERSHIP MENU=======
                  1. Add New Member
                  2. Delete Member
                  3. List Member
                  4. Exit
                  """
                    )
            
            choice=int(input("Enter Choice:"))
            if choice==1:
                 student.addmember()
            elif choice==2:
                  student.deletemember()
            elif choice==3:
                  student.listmember()                    
            elif choice==4:
                 # print("Thank for you using the library management system")
                  done = True
            else:
                print("Please select the correct option")
                 
                  
if __name__=="__main__":
    main()