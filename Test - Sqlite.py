
import sqlite3

conn = sqlite3.connect('library Management.db')

c= conn.cursor()

c.execute("""CREATE TABLE Book_database(
         bookId integer,
         bookName text,
         writer text,
         available text
         )""")

c.execute("INSERT INTO Book_database VALUES(1,'Arthashastra','Kautilya','y')")
conn.commit()

#c.execute("""DROP TABLE Book_database""")

#conn.commit()

c.execute("""CREATE TABLE Student(
         studentId integer,
         studentName text                
         )""")

#c.execute("""DROP TABLE Student""")

c.execute("INSERT INTO Student VALUES(1,'Mamta')")
conn.commit()

c.execute("""CREATE TABLE Book_Issued(
        transactionId integer,
        studentId integer,
        bookId integer
         )""")

c.execute("INSERT INTO Book_Issued VALUES(1,12,13)")

#c.execute("Select * from Book_Issued")
conn.commit()

