"""
STORE MANAGEMENT SYSTEM

Customer  ( CID , Cname , Caddress , CMobile )
Product   ( PID , Pname , Price , Pdesc)
Order     ( CID , PID , Qty )

1- Add Customer
2- View All Customer
3- Delete A Customer
4- Add Product
5- View All Product
6- Update A Product
7- Place An Order
8- View All Orders
9- View Orders By CID
0- Exit


"""
# REQUIRED LIBRARIES
import pickle
import os

# A METHOD TO ADD A CUSTOMER INFORMATION
def addCustomer():
    file = open('customer.bin','ab')
    cid = input("\n\t Enter Customer ID : ")
    cname = input("\t Enter Customer Name : ")
    cadd = input("\t Enter Customer Address : ")
    cmob = input("\t Enter Customer Mobile : ")
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    print("\n\t Customer Added Sucessfully!")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO VIEW ALL CUSTOMER'S INFORMATION
def viewAllCustomer():
    file = open('customer.bin','rb')
    try:
        while True:
            print("\n\t Customer ID :",pickle.load(file))
            print("\t Customer Name :",pickle.load(file))
            print("\t Customer Address :",pickle.load(file))
            print("\t Customer Mobile :",pickle.load(file))
            print("\t ----------------------------")
    except:
        print("\n\t Here is your all customers..")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO DELETE A CUSTOMER'S INFORMATION
def deleteCustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')
    cid = input("\t Enter Customer ID To Delete : ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data==cid:
                print("\t Customer Name :",pickle.load(file1))
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\t Customer Deleted Successfully!")
        else:
            print("\n\t Customer Not Found!")
    file1.close()
    file2.close()
    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')
    input("\t Press Enter To Continue...")

# A METHOD TO ADD A PRODUCT INFO
def addProduct():
    file = open('product.bin','ab')
    pid = input("\n\t Create Product ID : ")
    pname = input("\t Enter Product Name : ")
    price = input("\t Enter Product Price : ")
    pdesc = input("\t Write About The Product : ")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    pickle.dump(pdesc,file)
    print("\n\t Product Added Succesfully!")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO VIEW ALL PRODUCT's INFO
def viewAllProducts():
    file = open('product.bin','rb')
    try:
        while True:
            print("\n\t Product ID :",pickle.load(file))
            print("\t Product Name :",pickle.load(file))
            print("\t Product Price :",pickle.load(file))
            print("\t About Product :",pickle.load(file))
    except:
        print("\n\t Here is your all products..")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO UPDATE PRODUCT PRICE
def updateProduct():
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','ab')
    pid = input("\n\t Enter Product ID To Update : ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data==pid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\t Product Name :",name)
                print("\t Old Price :",pickle.load(file1))
                price = input("\t Enter New Price : ")
                pickle.dump(price,file2)
                pickle.dump(pickle.load(file1),file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\t Price Updated Successfully!")
        else:
            print("\t Product Not Found!")
    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')
    input("\t Press Enter To Continue...")

# A METHOD TO GET A CUSTOMER INFORMATION
def getCustomer(cid):
    cus = []
    file = open('customer.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==cid:
                cus.append(data)
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
    except:
        pass
    file.close()
    return cus

# A METHOD TO GET A PRODUCT INFORMATION
def getProduct(pid):
    pro = []
    file = open('product.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==pid:
                pro.append(data)
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
    except:
        pass
    file.close()
    return pro

# A METHOD TO PLACE AN ORDER
def placeAnOrder():
    cid = input("\n\t Enter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)!=0:
        print("\t Customer Name :",cus[1])
        print("\t Customer Address :",cus[2])
        pid = input("\t Enter Product ID : ")
        pro = getProduct(pid)
        if len(pro)!=0:
            print("\t Product Name :",pro[1])
            print("\t Product Price :",pro[2])
            qty = input("\t Enter Quantity : ")
            file = open('orders.bin','ab')
            pickle.dump(cid,file)
            pickle.dump(pid,file)
            pickle.dump(qty,file)
            file.close()
            print("\n\t Order Placed Successfully!")
            print("\t Bill Amount :",int(qty)*int(pro[2]))
        else:
            print("\t Product Not Found!")
    else:
        print("\n\t Customer Not Found!")
    input("\t Press Enter To Continue...")

# A METHOD TO VIEW ALL ORDERS
def ViewOrder():
    file = open('orders.bin','rb')
    try:
        n = 1001
        while True:
            cus = getCustomer(pickle.load(file))
            pro = getProduct(pickle.load(file))
            qty = pickle.load(file)
            print("\n\t Order No.",n)
            print("\t Customer Name :",cus[1])
            print("\t Customer Address :",cus[2])
            print("\t Product Name :",pro[1])
            print("\t Product Price :",pro[2])
            print("\t About Product :",pro[3])
            print("\t Total Bill :",int(pro[2])*int(qty))
            n=n+1
            print("\t ---------------------------")
    except:
        print("\n\t Here is you all orders...")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO VIEW ALL ORDERS INFORMATION BY CID
def viewOrderByCID():
    cid = input("\n\t Enter Customer ID : ")
    cus = getCustomer(cid)
    print("\n\t Customer Name :",cus[1])
    print("\t Customer Address :",cus[2])
    print("\t Customer Mobile :",cus[3])
    file = open("orders.bin",'rb')
    n = 1001
    try:
        while True:
            data = pickle.load(file)
            if data==cid:
                pro = getProduct(pickle.load(file))
                qty = pickle.load(file)
                print("\n\t Order No.",n)
                print("\t Product Name :",pro[1])
                print("\t Product Price :",pro[2])
                print("\t Product Desc :",pro[3])
                print("\t Quantity :",qty)
                print("\t Total Bill :",int(pro[2])*int(qty))
                n=n+1
    except:
        print("\t Here is your all orders for cid",cid)
    file.close()
    input("\t Press Enter To Continue...")

# DASHBOARD
while True:
    print("\n\t **** STORE MANAGEMENT SYSTEM ****")
    print('''
            1- Add Customer
            2- View All Customer
            3- Delete A Customer
            4- Add Product
            5- View All Product
            6- Update A Product
            7- Place An Order
            8- View All Orders
            9- View Orders By CID
            0- Exit
    ''')
    ch = int(input("\t Enter Your Choice : "))
    if ch==0:
        print("\n\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addCustomer()
    elif ch==2:
        viewAllCustomer()
    elif ch==3:
        deleteCustomer()
    elif ch==4:
        addProduct()
    elif ch==5:
        viewAllProducts()
    elif ch==6:
        updateProduct()
    elif ch==7:
        placeAnOrder()
    elif ch==8:
        ViewOrder()
    elif ch==9:
        viewOrderByCID()
    else:
        input("\n\t Wrong Entered\n\t Try Again!")
