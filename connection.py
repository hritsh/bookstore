# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:31:58 2021

@author: sohai
"""
import sqlite3


con = sqlite3.connect('db1.db')

def insertdata(name,age,city):
    qry="insert into tb1(name,age,city) values(?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("Details Added Successfully")

def Update(ID_NO,name,age,city):
    qry="update tb1 set name =?, age = ?, city=?  where ID_NO= ? ;"
    con.execute(qry,(ID_NO,name,age,city))
    con.commit()
    print("Details Updated Successfully")
    
def Delete(ID_NO):
    qry="delete from tb1 where ID_NO=? ;"
    con.execute(qry,(ID_NO))
    con.commit()
    print("ID deleted successfully")

def selectData():
    qry="select * from tb1 ;"
    result=con.execute(qry)
    for row in result:
        print(row)
        
    
print("""
1. Insert
2. Update
3. Delete
4. Select 
""")
ch=1
while ch==1:
    c=int(input("Enter Your choice"))
    if(c==1):
        print("Add new record")
        name=input("Enter your name")
        age=int(input("Enter your age"))
        city=input("Enter your city")
        
        insertdata(name,age,city)
        
    elif(c==2):
        print("Update your record")
        print("Add new record")
        ID_NO=int(input("Enter ID"))
        name=input("Enter your name")
        age=int(input("Enter your age"))
        city=input("Enter your city")
        
        Update(ID_NO,name,age,city) 
        
    elif(c==3):
        print("Delete you record")
        ID_NO=input("Enter ID")
            
        Delete(ID_NO)

    elif(c==4):
        print("Select Record")
        
        selectData()
    else:
        print("Invalid Selector")
    ch=int(input("Enter 1 to continue"))
print("Thank you")   