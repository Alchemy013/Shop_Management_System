import mysql.connector as sql
from tabulate import tabulate
import matplotlib.pyplot as plt
conn=sql.connect(host="localhost",user="root",password="root",database="Shop")
if conn.is_connected():
    print('successfully connected')
c=conn.cursor()
print('Shop')
print('1.Login')
print('2.Take Order')
print('3.Feedback')
print('4.Exit')
choice=int(input('Enter choice:'))
if choice==1:
    user=input('enter your user name=')
    pass_=input('enter your password=')
    dope="Y"
    while user=='root' and pass_=='root' and dope=='Y'or dope=='y':
        print('You are in \n1.Customer details\n2.Product details\n3.Worker details')
        print('4.Customers\n5.Products\n6.Workers\n7.Customer details\n8.Product details')
        print('9.Worker details\n10.Stocks')
        print('11.Exit')
        choice=int(input('Enter Choice'))
        if choice==1:
            Name=input('Enter Name=')
            Phone=int(input('Enter Phone Number='))
            sql_insert="insert into Customer_details values(""'"+(Name)+"',"+(Phone)+")"
            c.execute(sql_insert)
            conn.commit()
            print('Customer Added\n')
            dope=input("DO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==2:
            Product=input('Enter Product Name=')
            Cost=float(input('Enter Cost='))
            sql_insert="insert into Product_details values(""'"+(Product)+"',"+(Cost)+")"
            c.execute(sql_insert)
            conn.commit()
            print('Product Added')
            dope=input("DO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==3:
            W_Name=input('Enter Worker Name=')
            Job=input('Enter Work=')
            w_age=int(input('Enter Age='))
            w_salary=float(input('Enter Salary='))
            ph_no =int(input('Enter Phone Number='))
            sql_insert="insert into Worker_details values(" "'"+(W_Name)+"'," "'"+(Job)+"',"+(w_age)+","+(w_salary)+","+(ph_no)+ ")"
            c.execute(sql_insert)
            conn.commit()
            print('Worker Added')
            dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==4:
            t=conn.cursor()
            t.execute('select*from Customer_details')
            record=t.fetchall()
            for i in record:
                print(i)
            dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==5:
            t=conn.cursor()
            t.execute('select*from Product_details')
            record=t.fetchall()
            for i in record:
                print(i)
            dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==6:
            t=conn.cursor()
            t.execute('select*from Worker_details')
            record=t.fetchall()
            for i in record:
                print(i)
            dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==7:
            a=input('Enter Customer name')
            t='select*from Customer_details where Name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
            dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==8:
            a=input('Enter Product Name')
            t='select*from p_d where Product=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
            dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==9:
            a=input('Enter Worker Name')
            t='select*from Worker_details where W_Name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
            dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        elif choice==10:
            print("1.Text\n2.Graph")
            choic=int(input("Enter Choice"))
            if choic==1:
                f=open('Stock.txt','r')
                data=f.read()
                print(data)
                f.close()
                dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
            elif choic==2:
                items=('r','e','h','y','ann')
                a=[100,200,153,271,126]
                colors=['red','yellow','blue','gold','green']
                plt.pie(a,labels=items,colors=colors)
                plt.title('avalibility of items in shop')
                plt.show()
                dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
            else:
                print("Wrong Choice\n")
                dope=input("\nDO YOU WISH TO RETURN TO THE MENU PRESS Y IF YES ")
        else:
                print("Wrong Password")   
elif choice==2:
    choiii="y"
    a=0
    while choiii=='Y' or choiii=="y":
        pr=input('Enter Product Name ')
        price=float(input('Enter Product Price '))
        a=a+price
        choiii=input("Add Products? press Y")

      ##  conn=sql.connect(host="localhost",user="root",password="root",database="Shop")
       ## c=conn.cursor()
        
        sql_insert="insert into Orderr values('{}','{}')".format(pr,price)
        c.execute(sql_insert)
        conn.commit()
    t='select*from Orderr'
    c.execute(t)
    v=c.fetchall()
    print(tabulate(v, headers=['Product', 'Price'], tablefmt='psql'))
    print("Total Amount=",a)
    z='f'
    z=input("do you want reciept on email? if Yes press F")



    #conn=sql.connect(host="localhost",user="root",password="root",database="Shop")
    #c=conn.cursor()
    
    
    
    
    s='DELETE FROM Orderr'
    c.execute(s)
    conn.commit()
    if z=="f" or z=="F":
        try:
            r=input("enter your email")
            import smtplib as s
            server = s.SMTP_SSL("smtp.gmail.com",465)
            server.login("dadsmail13x@gmail.com","#rs123456789")
            text='blah blah'
            server.sendmail("dadsmail13x@gmail.com",r,text)
            server.quit()
            print("Thankyou for Shopping With US")
        except:
            print("Wrong Mail")
            print("Thanks for Shopping")
    else:
            print("Thankyou for Shopping With Us")
elif choice==3:
    print("FEEDBACK FORM :-")
    print("Press 1 to give descriptive feedback")
    print("Press 2 to give ratings to our services out of 10")
    print("~~DO RATE US ON GOOGLE AS WELL~~")
    choice=int(input("~~enter your choice~~"))
    if choice==1:
        C_name=input("enter your name ")
        pro=input("enter the product u bought from our store ")
        review1=input("enter your reviews about the products of our store ")
        review2=input("review our store workers and helpers behaviour towards you ")
        suggestion=input("suggestions u our store for our betterment ")
        z= "insert into Review values(" + (C_name) + ",'" + str(pro)+ "'," + str(review1) + ",'" + str(review2) +",'" + str(suggestion) +")"
        c.execute(z)
        print("Your feedback is registered.Thank you for giving feedback have a nice day ")
        c.commit()

    if choice==2:
        a=int(input("enter the customer id"))
        b=input("enter your name")
        c=int(input("rate your overall experience from 1-10"))
        d=int(input("rate product quality from 1-10"))
        e=int(input("rate our wrokers from 1-10"))
        f=int(input("rate our helpers and cleaners from 1-10"))
        g=int(input("rate our cashiers from 1-10"))
        h=int(input("rate our helping desk from 1-10"))
        i=int(input("rate our store ambienece from 1-10"))
        j=int(input("rate our product's prices as compared to other stores from 1-10"))
        sql_insert="insert into scores values("+ (a)+ ",'" + (b) + ",'" + (c) + ",'" + (d) + ",'" + (e) + ",'" + (f) + ",'" + (g) + ",'" + (h) + ",'" + (i) + ",'" + (j) + ")" 
        c.execute(sql_insert)
        print("Your ratings are registered.Thank you for rating us have a nice day")
        c.commit()

elif choice==4:
    exit()      
