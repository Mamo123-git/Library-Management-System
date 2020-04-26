
import sqlite3
from sqlite3 import Error

class database_tasks:
    
    def __init__(self, bookId=0 , studentId=0, transactionId = 0,Id = 0):
        self.bookId=bookId
        self.studentId=studentId
        self.transactionId = transactionId
        self.Id = Id
       
    def create_connection(self):
        try:
            conn = sqlite3.connect('library Management.db')
            return conn
        except Error as e:
            print(e)             
    
    # method insert
    def maximum(self,conn,dbname):
        
        c = conn.cursor()
        
        if dbname == "Book_database":
           c.execute ("Select Max(bookId) from Book_database")
            
        elif dbname == "Student":
            c.execute ("Select Max(studentId) from Student")
        
        elif dbname == "Book_Issued":
            c.execute ("Select Max(transactionId) from Book_Issued")           
        result = c.fetchone()
               
        if len(result) > 0:
            self.Id = result[0]
        else:
            self.Id = 0        
                
                
        return None
        
        
    def insert(self, conn,dbname, name, writer='none'):
        c = conn.cursor()
        self.maximum(conn,dbname)
        
        if dbname == "Book_database":            
            if self.Id == 0:
                self.bookId = 1                                  
            else:
                self.bookId = int(self.Id)
                self.bookId += 1
            c.execute ("INSERT INTO Book_database VALUES(?,?,?,'y')",(self.bookId, name, writer))
            
        elif dbname == "Student":
           if self.Id == 0:
               self.studentId = 1                                            
           else: 
               self.studentId = int(self.Id) + 1
               #.studentId += 1            
           c.execute ("INSERT INTO Student VALUES(?,?)",(self.studentId, name))
            
        conn.commit()        
        return None 
    
    # Insert data into Book_Issued Table 
    
    def insert_bookIssued(self, conn,dbname, studentId, bookId):
        c=conn.cursor()
        
        self.maximum(conn,dbname)
             
        self.transactionId = self.Id +1            
          
        c.execute ("INSERT INTO Book_Issued VALUES(?,?,?)",(self.transactionId, studentId, bookId))
        conn.commit()
        return None
    
    def connection_close(self,conn):
        conn.close()
        return None
        
        #  method delete  
     
    def delete(self, conn, dbname, name):
        c=conn.cursor()
        
        if dbname == "Book_database":
            sql = 'DELETE FROM Book_database WHERE bookName=?'
            c.execute(sql, (name,))
   
        else:
            sql = 'DELETE FROM Student WHERE studentName=?'
            c.execute(sql, (name,))
            
        conn.commit()
        return None
    
    # method to check whether the student is a member of the library 
    
    def isStudentEnrolled (self, conn, studentId):
        c=conn.cursor()
        
        sql= 'SELECT * FROM Student where studentId = ?'
        c.execute(sql,(studentId,))
        
        rows = c.fetchall()
        
        if bool(rows):
            return "true"
        else:
            return "false"
        
    # update the book database 

    def updatebook (self, conn , avail , bookname):
        c=conn.cursor()
        
        sql = "update Book_database set available =? where bookName = ?"
        c.execute(sql, (avail, bookname,))
        conn.commit()
        return None  
       
    # method to check whether the book available or not 
        
    def isbookavailable (self, conn, bookname):
        c=conn.cursor()        
        sql= "SELECT bookId FROM Book_database where bookName = ? and available = 'y'"
        c.execute(sql,(bookname,))
        
        rows = c.fetchall()
        
        if bool(rows):
            return rows[0][0]
        else:
            return 0
        
    
     #  method select all records
    
    def selectall(self, conn , dbname):
        c=conn.cursor()
        
        if dbname == "Book_database":
            sql= "SELECT * FROM Book_database"
        
        else:
            sql= "SELECT * FROM Student"
                    
        c.execute(sql)
        rows = c.fetchall()
 
        for row in rows:
            print(row)
        return None
            
    # method to check the available books that can be issued by the students 
            
    def selectavailablebooks(self, conn):
        c= conn.cursor()
        
        sql= "SELECT * FROM Book_database where available = 'y'"
        c.execute(sql)
        
        rows = c.fetchall()
        for row in rows:
            print(row)
        return None
            
    # method to check books issued 
            
    def selectallbooksissued(self, conn):
       c= conn.cursor()
        
       sql= "SELECT * from Book_Issued"
       c.execute(sql)
        
       rows = c.fetchall()     
       for row in rows:
            print(row)
            
       return None