import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",password="root",database="Shop")
if conn.is_connected():
    print('successfully connected')
c=conn.cursor()
def Show(): 
    c.execute("SHOW TABLES")
    record=c.fetchall()
    for i in record:
        print(i)
try:
    c.execute("CREATE TABLE Customer_details (Name VARCHAR(255),Phone int)")
    c.execute("CREATE TABLE Product_details (Product VARCHAR(255),Cost int)")
    c.execute("CREATE TABLE Worker_details (W_Name VARCHAR(255),job VARCHAR(255),w_age int,W_salary int,ph_no int)")
    c.execute("CREATE TABLE Orderr (Product VARCHAR(255),Price int)")
    c.execute("CREATE TABLE Review1 (C_name VARCHAR(255),pro VARCHAR(255),review1 VARCHAR(255),review2 VARCHAR(255),suggestion VARCHAR(255))")
    c.execute("CREATE TABLE Review2 (a int,b int,c int,d int,e int,f int,g int,h int,i int,j int)")
    c.execute("SHOW TABLES")
    record=c.fetchall()
    for i in record:
        print(i)
except:
    Show()

