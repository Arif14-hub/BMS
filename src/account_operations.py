from db_config import connect

def create_account():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email Id: ")
    phone = input("Enter Your Phone Number: ")
    balance = float(input("Enter Your Opening Balance: "))
    db =connect()
    cursor=db.cursor()
    sql="INSERT INTO accounts (name, email, phone, balance) VALUES (%s,%s ,%s, %s)"
    values = (name, email, phone, balance)
    cursor.execute(sql,values)
    db. commit()
    print ("Account Created successfully!")
    db.close()
    
    
def view_account():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM accounts")  
    accounts = cursor.fetchall()
    print(" All Accounts: ")
    for acc in accounts:
        print(f"\n Account Id: {acc[0]}\n Name:       {acc[1]}\n Email:      {acc[2]}\n Phone:      {acc[3]}\n Balance:    {acc[4]}")
    db.close()


def deposit_money():  
    account_id = int(input("Enter Your Account ID: "))
    amount = float(input("Enter Deposit Amount: "))
    db=connect()
    cursor =db.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id))
    db.commit()
    print ("Money Deposited successfully.")
    db.close()
    
    
def withdraw_money():
    account_id = int(input("Enter Your Account ID: "))
    amount = float(input("Enter Amount to Wthdraw: "))
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()
    if result and result[0]>=amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", (amount, account_id))
        db.commit()
        print("Money Withdrawn successfully.")
    else:
        print("Insufficient balance or account not found.")

    db.close()   
    

def check_balance():
    account_id = int(input("Enter Your Account ID: "))
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT name, balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()
    if result:
     print(f"\n Account Holder : {result[0]}\n Balance        : {result[1]}")
    else:
     print ("Account not found")
    db.close()  
             