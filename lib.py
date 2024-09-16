import mysql.connector as mysql
from datetime import date, datetime
import math
import random as r

pwd=input("MySQL Pass: ")
dat=input("Databae name: ")
print()
print('--------------------------------------SACRED-KNOWLEDGE---------------------------------------')
# connect python to mysql database
db = mysql.connect(
    host="localhost",
    username="root",
    password=pwd,
    database=dat)
  
# get cursor object
cursor1 = db.cursor('books')
cursor2 = db.cursor('req')
cursor3 = db.cursor('issued')
cursor4 = db.cursor('returned')
cursor5 = db.cursor()
cursor6 = db.cursor()
cursor7 = db.cursor()

# execute query and fetch all the matching rows
cursor1.execute("SELECT * FROM books order by SrNo")
res1 = cursor1.fetchall()

cursor2.execute("SELECT * FROM req order by SrNo")
res2 = cursor2.fetchall()

cursor3.execute("SELECT * FROM issued order by SrNo")
res3 = cursor3.fetchall()

cursor4.execute("SELECT * FROM returned order by SrNo")
res4 = cursor4.fetchall()

'''
# loop through the rows
for row in res1:
    print(row, '\n')
print()

for row in res2:
    print(row,'\n')
print()

for row in res3:
    print(row,'\n')
print()

for row in res4:
    print(row,'\n')
print()
'''

run=True
while run:
    print("-------MAIN-MENU--------")
    print("1. Show Available Books")
    print("2. Request a book to order")
    print("3. Issue a Book")
    print("4. Return a Book")
    print("5. Exit")

    choice=int(input("Choose an option: "))
    if choice==1:
        #print('%10s'%'SrNo','%40s'%'Book Name','%40s'%'Genre','%40s'%'ISBN No.','%40s'%'Status')
        print("1.  View Books")
        print("2. Search")
        ch=int(input("Option: "))
        print()
        if ch==1:
            for row in res1:
                print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n','==========================')
            print('==========================')

        elif ch==2:
            sear=True
            while sear:
                print('Search:','\n','1. By Name','\n','2. By Genre')
                print('3. Add Books')
                print('4. Delete a book')
                print('5. Exit')
                choice1=int(input("Option: "))
                if choice1==1:
                    name=input("Book Name: ")
                    print('==========================','\n')
                    cursor1.execute("select * from books where Book_name like (%s)",['%'+name+'%'])
                    found_books=cursor1.fetchall()
                    if found_books!=[]:
                        for row in found_books:
                            print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n','==========================')
                    else:
                        print("Book Not available.")
                elif choice1==2:
                    name=input("Genre Name: ")
                    print('==========================','\n')
                    cursor1.execute("select * from books where Genre like (%s)",['%'+name+'%'])
                    found_books=cursor1.fetchall()
                    if found_books!=[]:
                        for row in found_books:
                            print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n','==========================')
                    else:
                        print("Book Not available.")
        
                elif choice1==3:
                    book_name=input('Enter Book Name: ')
                    genre=input('Enter Genre: ')
                    isb=True
                    while isb:
                        isbn=input("Enter ISBN No.: ")
                        if len(isbn)!=13 or isbn.isdigit()==False:
                            print("Invalid ISBN. Try Again.")
                        else:
                            isb=False
                    cursor1.execute('insert into books(Book_Name,Genre,ISBN_No) values (%s,%s,%s);',(book_name,genre,isbn))
                    print("Added Book successfully.",'\n','Name:',book_name,'\n','Genre:',genre,'\n','ISBN No.:',isbn)
                    res1=cursor1.fetchall()
                    db.commit()
                    
                elif choice1==4:
                    name=input("Enter Book Name:  ")
                    cursor1.execute('delete from books where books.Book_Name =(%s) ;',[name])
                    print("Deleted",name)
                    db.commit()
                    
                elif choice1==5:
                    ex=input("Are you sure you want to exit search?(y/n): ")
                    if ex.lower()=='y':
                        print("Exiting Search...")
                        sear=False
                    elif ex.lower=='n':
                        print("Taking you back to search")
                    else:
                        print("Invalid. Taking you back to search")
                else:
                    print("Invalid Choice")
                    break
        else:
            print("Invalid Choice")
            break
        print()
    elif choice==2:
        for row in res2:
            print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n','==========================')
        print('==========================')
        book_name=input('Enter Book Name: ')
        genre=input('Enter Genre: ')
        cursor5.execute('SELECT YEAR(CURDATE());')
        year = cursor5.fetchall()
        cursor6.execute('select MONTH(CURDATE());')
        month = cursor6.fetchall()
        cursor7.execute('SELECT DAY(CURDATE());')
        day = cursor7.fetchall()
        date_of_arrival=date(year[0][0],month[0][0],day[0][0])
        cursor2.execute('insert into req(Book_Name,Genre,Date_of_arrival) values(%s,%s,%s);',(book_name,genre,date_of_arrival))
        db.commit()
        print('==========================')
        print('==========================')
        for row in res2:
            print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n','==========================')

    elif choice==3:
        for row in res1:
            print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n','==========================')
        print('==========================')
        name=input("Book Name: ")
        for row in res1:
            if name.lower() == row[1].lower() and row[4]=='Not Issued':
                genre=row[2]
                cursor1.execute('update books set books.Status="Issued" where books.Book_Name =(%s) ;',[name])
                db.commit()
                print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n','==========================')
                issuer_name=input("Enter your name: ")
                issuer_id=r.randint(100000,999999)
                issuer_id=str(issuer_id)
                cursor5.execute('SELECT YEAR(CURDATE());')
                year = cursor5.fetchall()
                cursor6.execute('select MONTH(CURDATE());')
                month = cursor6.fetchall()
                cursor7.execute('SELECT DAY(CURDATE());')
                day = cursor7.fetchall()
                date_of_issue=date(year[0][0],month[0][0],day[0][0])
                cursor3.execute('insert into issued(Book_Name,Genre,Issuer_Name,Issuer_ID,Date_of_issue) values(%s,%s,%s,%s,%s)',(name,genre,issuer_name,issuer_id,date_of_issue))
                db.commit()
                
            elif name == row[1] and row[4]=='Issued':
                print('Book Already Issued')
                
        print("Issued book",name,"on",year[0][0],'-',month[0][0],'-',day[0][0])
        print("Your Issue ID is",issuer_id)
        cursor1.execute("SELECT * FROM books ORDER BY SrNo;")
        res1=cursor1.fetchall()
        print('==========================')
        print('==========================')
        #for row in res1:
        #    print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n','==========================')
    elif choice==4:
        for row in res1:
            print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n','==========================')
        print('==========================')
        iss=True
        while iss==True:
            issuer_id=input("Issuer Id: ")
            issuer_name=input("Enter your name: ")
            if len(issuer_id) < 6 or issuer_id.isdigit() == False:
                print("Wrong ID or Name. Input Again.")
            else:
                iss=False
        for row in res3:
            if issuer_id == row[4] and issuer_name==row[3]:
                genre=row[2]
                name=row[1]
                cursor1.execute('update books set books.Status="Not Issued" where books.Book_Name =(%s) ;',[name])
                db.commit()
                print('%5s'%row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n',row[5],'\n','==========================')
                
        cursor5.execute('SELECT YEAR(CURDATE());')
        year = cursor5.fetchall()
        cursor6.execute('select MONTH(CURDATE());')
        month = cursor6.fetchall()
        cursor7.execute('SELECT DAY(CURDATE());')
        day = cursor7.fetchall()
        date_of_return=date(year[0][0],month[0][0],day[0][0])
        cursor3.execute('insert into returned(Book_Name,Genre,Issuer_Name,Issuer_ID,Date_of_return) values(%s,%s,%s,%s,%s)',(name,genre,issuer_name,issuer_id,date_of_return))
        db.commit()
        print('==========================')
        print("Returned",name,"on",year[0][0],'-',month[0][0],'-',day[0][0])
        print('==========================')

    elif choice==5:
        ext=input("Are you sure you want to exit? (y/n) ")
        if ext=="y" or ext=="Y":
            print("Thank you for visiting Sacred Knowledge.")
            run=False            
        elif ext=="n" or ext=="N":
            print("Taking you back to library.")
            run=True
        else:
            print("Invalid Choice. Taking You back to library.")
    else:
        print("Invalid Choice.")


