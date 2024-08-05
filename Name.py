class ATM:
    def __init__(self):
        import sys
        import os
        self.__Official_account="00000000000"
        Authentication_Key=("h9hj@hjd!jwg3sd@fj#bdjkghz*s7kdg","X9hG@hjD!jwg3s7@fj#B0jkghz*s7kdA","o9hj@hpd!jw63sd@fj@bdjerg&s7k*g")
        import random
        self.__Authentication_Key=random.choice(Authentication_Key)
        print('''
              ________________________________________________________________
              |~~~~~~~~~~~~~~~~~~~~~: WELCOME TO THE ATM :~~~~~~~~~~~~~~~~~~~|
              |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
              |            Don't Have Account?-Create An Account-[PRESS -> 1]|
              |                                                              |
              |       Already Have Account?-Cardless Transaction-[PRESS -> 2]|
              |                                                              |
              |                                             EXIT-[PRESS -> 0]|
              |______________________________________________________________|
              ''')
        x=int(input("Enter The Choice: "))
        if x==2:
            os.system("cls")
            Accn=input("Enter The 11 Digit Account Number: ")
            if Accn==self.__Official_account:
                self.__Accn=self.__Official_account
                os.system("cls")
                self.__menu()
            else:
                self.__last_deposite = None
                self.__deposit_history=None
                if len(Accn)!=11 or Accn.isdigit()==False:
                    print("Please Enter A Valid Account Number!")
                    sys.exit()
                else:
                    self.__Accn=self.__get_binary(Accn)
                    with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r") as file:
                        data=file.readlines()
                    if len(data)==0:
                        os.system("cls")
                        print("You Don't Have any Account! Please Create an Account...")
                        self.__Account_details()
                    else:
                        for i in data:
                            i=i.strip()
                            if i.startswith("Account Number: "):
                                i=i[len("Account Number: "):]
                                Account,Details=i.split(";Customer Name: ")
                                if Account == self.__Accn:
                                    self.__menu()
                                    break
                        if Account != self.__Accn:
                            os.system("cls")
                            print("You Don't Have any Account! Please Create an Account...")
                            self.__Account_details()  
        if x==1:
            self.__Account_details()  
        if x==0:
            sys.exit()
    
    def __menu(self):
        import sys
        import os
        import time
        os.system("cls")
        end_time=time.time()+15
        from datetime import datetime
        DATE=datetime.today().strftime("%Y-%m-%d %H:%M")
        if time.time()<=end_time:
            print(f'''
                     ___________________________________________________________
                     |~~~~~~~~~~~~~~~~~~~~~~: OPERATIONS :~~~~~~~~~~~~~~~~~~~~~|
                     |<><><><><><><><><><<><><><><><><><><><><><><><><><><><><>|
                     |                             |  Cash Withdraw -[PRESS->2]|
                     |[PRESS->1]- Balance Inquiry  |                           |
                     |                             |     Change Pin -[PRESS->4]|
                     |[PRESS->3]- Cash Deposit     |                           |
                     |                             |           Exit -[PRESS->0]|
                     |[PRESS->5]- Forget Pin       |                           |
                     |                             |          More -[PRESS->10]|  
                     |                     {DATE}                    |
                     |_________________________________________________________|
            ''')
            ch=input("Enter The Choice: ")
            if ch=="1" and time.time()<=end_time:
                self.__Available_balance()
            elif ch=="2" and time.time()<=end_time:
                self.__Withdraw()
            elif ch=="3" and time.time()<=end_time:
                self.__Deposit()
            elif ch=="4" and time.time()<=end_time:
                self.__Change_Pin()
            elif ch=="5" and time.time()<=end_time:
                self.__get_pin()
            elif ch=="0" and time.time()<=end_time:
                os.system("cls")
                sys.exit()
            elif ch=="10" and time.time()<=end_time and self.__Accn==self.__Official_account:
                os.system("cls")
                print("Get Authentication key- [Press->1]               Exit- [Press->0]")
                ch=int(input("Enter The Choice: "))
                if ch==1:
                    os.system("cls")
                    print("Please Copy The Authentication Key for Farther Use:",self.__Authentication_Key)
                elif ch==0:
                    os.system("cls")
                    sys.exit()
                else:
                    print("Inavalid Choice...")
                print(f'''
                          ____________________________________________________________
                          |~~~~~~~~~~~~~~~~~~: SPECIAL OPERATIONS :~~~~~~~~~~~~~~~~~~|
                          |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
                          |[PRESS->11]- Get Details     |                            |
                          |                             |  Total Deposit- [PRESS->12]|
                          |[PRESS->13]- Advantages      |                            |
                          |                             |Total Withdrawl- [PRESS->14]|
                          |[PRESS->15]- Limitations     |                            |
                          |                             |     Amount Sum- [PRESS->16]|
                          |[PRESS->17]- Atm Deposit     |                            |
                          |                             |           Exit- [PRESS-> 0]|
                          |                     {DATE}                     |
                          |__________________________________________________________|
                          ''')
                ch=int(input("Enter The Choice: "))
                if ch==11:
                    self.__get_details()
                elif ch==12:
                    self.__Total_Deposit()
                elif ch==13:
                    self.__Advantages()
                elif ch==14:
                    self.__Total_Withdrawl()
                elif ch==15:
                    self.__Limitations()
                elif ch==16:
                    self.__Amount_Sum()
                elif ch==17:
                    self.__Atm_Deposit()
                elif ch==0:
                    os.system("cls")
                    sys.exit()
            elif ch not in ["0","1","2","3","4","5","10"]:
                os.system("cls")
                print("Invalid Input...")
            elif ch=="10" and time.time()<=end_time and self.__Accn!=self.__Official_account:
                os.system("cls")
                print("Wrong Account Number or You Are Not An Official...")
            else:
                os.system("cls")
                print("Session Time-out...")
        # else:
        #     os.system("cls")
        #     print("Session Time-out...")
        # # if time.time()==end_time and len(ch)==0:
        #     os.system("cls")
        #     print("Operation Time out....")
        #     sys.exit()
    def __get_details(self):
        import sys
        import os
        os.system("cls")
        accn=input("Enter The Account Number of Any Customer: ")
        accn=self.__get_binary(accn)
        with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r") as f:
            data=f.readlines()
            key=input("Enter The Authentication Key: ")
            if key==self.__Authentication_Key:
                for i in data:
                    if i.startswith("Account Number: "+accn):
                        i=i[len("Account Number: "):]
                        a,b=i.split(";Customer Name: ")
                        a=self.__decode(a)
                        b,c=b.split(";Age: ")
                        b=self.__decode(b)
                        c,d=c.split(";Balance: ")
                        d,e=d.split(";")
                        d=self.__decode(d)
                        os.system("cls")
                        print(f"Account Number: {a};Customer Name: {b};Balance: {d}")
            else:
                os.system("cls")
                print("Wrong Authentication Key!!!")
                sys.exit()                    
    def __Total_Deposit(self):
        import sys
        import os
        from datetime import datetime
        os.system("cls")
        key=input("Enter The Authentication Key: ")
        today = datetime.today().strftime("%Y-%m-%d")
        if key==self.__Authentication_Key:
            s=0
            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r") as f:
                data=f.readlines()
                for i in data:
                    if i.startswith("CDEPOSIT"):
                        a,b,c,d=i.split("|")
                        x,y=c.split()
                        if x==today:
                            d=int(d)
                            s=s+d
                if x==today:
                    print(f"Date: {c} Total Amount Deposited in ATM {s}")
                else:
                    # os.system("cls")
                    print("No Amount Deposited Today...")
                    sys.exit()
    def __Total_Withdrawl(self):
        import sys
        import os
        from datetime import datetime
        os.system("cls")
        key=input("Enter The Authentication Key: ")
        today = datetime.today().strftime("%Y-%m-%d")
        w=0
        if key==self.__Authentication_Key:
            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r") as f:
                data=f.readlines()
                for i in data:
                    if i.startswith("WITHDRAW"):
                        a,b,c,d=i.split("|")
                        x,y=c.split()
                        if x==today:
                            d=int(d)
                            w=w+d
                if x==today:
                    print(f"Date: {c} Total Amount Withdrawl in ATM {w}")
                else:
                    os.system("cls")
                    print("No Amount Withdrawan Today...")
                    sys.exit()    
    def __Atm_Deposit(self):
        import sys
        import os
        from datetime import datetime
        os.system("cls")
        key=input("Enter The Authentication Key: ")
        today = datetime.today().strftime("%Y-%m-%d %H:%M")
        self.__Official_account=self.__get_binary(self.__Official_account)
        if key==self.__Authentication_Key:
            os.system("cls")
            print("Authentication Successful...")
            cash=input("Enter Deposit Amount: ")
            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","a") as f:
                f.write(f"ADEPOSIT|{self.__Official_account}|{today}|{cash}\n")
                os.system("cls")
                print("Cash Deposit Successful...")
        else:
            os.system("cls")
            print("Authentication Failed....")
            sys.exit()
    def __Amount_Sum(self):
        import sys
        import os
        from datetime import datetime
        os.system("cls")
        key=input("Enter The Authentication Key: ")
        today = datetime.today().strftime("%Y-%m-%d")
        if key==self.__Authentication_Key:
            os.system("cls")
            print("Authentication Successful...")
            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r") as file:
                data=file.readlines()
                x=0
                y=0
                z=0
                for i in data:
                    if i.startswith("ADEPOSIT"):
                        a,b,c,d=i.split("|")
                        d=int(d)
                        x=x+d
                    elif i.startswith("CDEPOSIT"):
                        e,f,g,h=i.split("|")
                        h=int(h)
                        y=y+h
                    elif i.startswith("WITHDRAW"):
                        j,k,l,m=i.split("|")
                        m=int(m)
                        z=z+m
                sum=(x+y)-z
                print(f"ATM Balance: {sum}")
    def __Account_details(self):
        import sys
        import os
        os.system("cls")
        print('''
              __________________________________________________________________________________________
              |~~~~~~~~~~~~~~~~~~~~~~~~~~: Here Few Steps to Create Account :~~~~~~~~~~~~~~~~~~~~~~~~~~|
              |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
              |     STEP:1    |      STEP:2      |     STEP:3     |     STEP:4     |      STEP:5       |
              | Create Number | Personal Details |  Pin Creation  |  Base-Deposit  |  Account Created  |
              |<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>|
              |________________________________________________________________________________________|
              ''')
        New_Account=input("Set an Account Number of 11 Digits: ")
        if len(New_Account)!=11 or New_Account.isdigit()==False:
            print("Account Number Should Contain 11 Numeric Digits!")
        else:
            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r") as file:
                data=file.readlines()
                if len(data)==0:
                    os.system("cls")
                    Name=input("Enter The First-Name: ")
                    if Name.isalpha()==False:
                        print("First-Name Should Contain Characters Only!")
                    else:
                        Sur_name=input("Enter The Sur-Name: ")
                        if Sur_name.isalpha()==False:
                            print("Sur-Name Should Contain Characters Only!")
                        else:
                            gender=input("Enter Gender: ")
                            if gender.startswith("m") or gender.startswith("M"):
                                self.__gender="Male"
                            elif gender.startswith("f") or gender.startswith("F"):
                                self.__gender="Female"
                            else:
                                self.__gender=gender
                            self.__New_Account=New_Account
                            self.__Name=Name+" "+Sur_name
                            self.__Age=self.__DOB()
                            if self.__Age<18:
                                self.__Mage="(Minor Account)"
                            else:
                                self.__Mage=""
                                self.__Pin=self.__RPin()
                                self.__Balance=self.__Amount()
                                self.__Add_Account()
                else:
                    New_Account=self.__get_binary(New_Account)
                    x=[]
                    for i in data:
                        i=i.strip()
                        if i.startswith("Account Number: "):
                            i=i[len("Account Number: "):]
                            account,extra=i.split(";Customer Name: ")
                            x.append(account)
                    if New_Account not in x:
                        os.system("cls")
                        Name=input("Enter The First-Name: ")
                        if Name.isalpha()==False:
                            print("First-Name Should Contain Characters Only!")
                        else:
                            Sur_name=input("Enter The Sur-Name: ")
                            if Sur_name.isalpha()==False:
                                print("Sur-Name Should Contain Characters Only!")
                            else:
                                gender=input("Enter Gender: ")
                                if gender.startswith("m") or gender.startswith("M"):
                                    self.__gender="Male"
                                elif gender.startswith("f") or gender.startswith("F"):
                                    self.__gender="Female"
                                else:
                                    self.__gender=gender
                                New_Account=self.__decode(New_Account)
                                self.__New_Account=New_Account
                                self.__Name=Name+" "+Sur_name
                                self.__Age=self.__DOB()
                                if self.__Age<18:
                                    self.__Mage="(Minor Account)"
                                else:
                                    self.__Mage=""
                                self.__Pin=self.__RPin()
                                self.__Balance=self.__Amount()
                                self.__Add_Account()
                    else:
                        print("This Account Number is Already Present!\nTry With a Different Account Number....")        
    def __DOB(self):
        import sys
        import os
        os.system("cls")
        print(f"Hello! {self.__Name} \nPlease Enter Your Date Of Birth in (dd-mm-yyyy) Format:")
        Date=input("Enter The Date Only in (dd) Format: ")
        if len(Date)==1:
            Date="0"+Date
        D=int(Date)
        if D>31:
            print("Date Should be Less than or Equal to 31")
        else:
            Month=input("Enter The Month only in (mm) Format: ")
            if len(Month)==1:
                Month="0"+Month
            M=int(Month)
            if M>12:
                print("Month Should be Less than or Equal to 12!")
            elif M==2 and D>29:
                print("In February Month Date Should be Less than or Equal to 29!")
            else:
                Year=input("Enter The Year of Birth only in (yyyy) Format: ")
        dob=Year+"-"+Month+"-"+Date
        from datetime import datetime
        birthday=datetime.strptime(dob,"%Y-%m-%d")
        today=datetime.now()
        age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
        return age
    
    def __RPin(self):
        import sys
        import os
        os.system("cls")
        print(f"Hello! {self.__Name} \nPlease Enter Your PIN Preference:")
        import random
        Pin=()
        for i in range(3):
            x=input(f"Enter 4 digit Pin Choice {i+1}: ")
            if len(x)==4 and x.isdigit()==True:
                Pin=Pin+(x,)
            else:
                print("PIN Should Consist of 4 Digits Only")
                sys.exit()
        Random_pin=random.choice(Pin)
        return Random_pin
    
    def __Amount(self):
        import sys
        import os
        os.system("cls")
        if self.__Age<18:
            return 0
        else:
            balance=int(input("Enter The Amount(= or > Rs-2000) to Deposit: "))
            if balance<2000:
                print("Deposit Amount Should be Gretter than or Equal to Rs-2000")
            else:
                return balance
    
    def __Add_Account(self):
        import sys
        import os
        self.data=f"Account Number: {self.__New_Account};Customer Name: {self.__Name};Age: {self.__Age};Gender: {self.__gender};Pin: {self.__Pin};Balance: {self.__Balance};{self.__Mage}"
        self.__New_Account=self.__get_binary(self.__New_Account)
        self.__Name=self.__get_binary(self.__Name)
        self.__Age=str(self.__Age)
        self.__Age=self.__get_binary(self.__Age)
        self.__Pin=self.__get_binary(self.__Pin)
        self.__Balance=str(self.__Balance)
        self.__Balance=self.__get_binary(self.__Balance)
        f=open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","a")
        f.write(f"Account Number: {self.__New_Account};Customer Name: {self.__Name};Age: {self.__Age};Gender: {self.__gender};Pin: {self.__Pin};Balance: {self.__Balance};{self.__Mage}\n")
        os.system("cls")
        import time
        print("Account Created Successfully.....")
        print(self.data)
        f.close()
        time.sleep(10)
        os.system("cls")
        
    def __Deposit(self):
        import sys
        import os
        import time
        accn=input("Enter Your Account Number: ")
        accn=self.__get_binary(accn)
        if accn==self.__Accn:
            deposit=int(input("Enter The Amount to Deposit: "))
            if deposit and deposit<=50000:
                from datetime import datetime
                today = datetime.today().strftime("%Y-%m-%d %H:%M")
                self.__last_deposite=today
                self.__deposit_history=deposit
                with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","a") as f:
                    f.write(f"CDEPOSIT|{accn}|{self.__last_deposite}|{self.__deposit_history}\n")
                with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r") as f:
                    history=f.readlines()
                    element=[]
                    for i in history:
                        if i.startswith("CDEPOSIT|"+accn):
                            w,x,y,z=i.split("|")
                            z=int(z)
                            element.append(z)
                    a=sum(element)
                    if a>50000 and y==today:
                        print("Your Maximum Deposit Limit Exceed for Today!\nPlease Try After 24 Hours of The Last Deposit")
                        with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r+") as f:
                            history=f.readlines()
                            f.seek(0)
                            f.truncate()
                            f.writelines(history[:-1])
                    if x==self.__Accn and y==today and a<=50000:
                        with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r+") as file:
                            data=file.readlines()
                            file.seek(0)#It moves the cursor to the starting Position of the txt file
                            for i in data:
                                if i.startswith("Account Number: "+accn):
                                    details,balance=i.split(";Balance: ")
                                    balance,extra=balance.split(";")
                                    balance=self.__decode(balance)
                                    int_balance=int(balance)
                                    int_balance=int_balance+deposit
                                    balance=str(int_balance)
                                    balance=self.__get_binary(balance)
                                    i=details+";Balance: "+balance+";"+extra
                                file.write(i)
                                os.system("cls")
                                print("Deposit Successful...")
                time.sleep(2)
                print("Go to MENU -[PRESS-> 1]                 EXIT -[PRESS->0]")
                ch=int(input("Enter The Choice: "))
                if ch==1:
                    self.__menu()
                elif ch==0:
                    os.system("cls")
                    sys.exit()
                else:
                    os.system("cls")
                    print("Invalid Choice...")                
                                        
            else: 
                print("You Can Deposit upto Rs-50000 per day")
        else:
            print("Sorry!\nWrong Account Number !")
    
    def __Available_balance(self):
        import sys
        import os
        with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r") as f:
            data=f.readlines()
            for i in data:
                i=i.strip()
                if i.startswith("Account Number: "+self.__Accn):
                    x,y=i.split("Balance: ")
                    y,extra=y.split(";")
                    y=self.__decode(y)
                    os.system("cls")
                    import time
                    print("Available Balance:",y)
                    time.sleep(2)
                    print("Go to MENU -[PRESS-> 1]                 EXIT -[PRESS->0]")
                    ch=int(input("Enter The Choice: "))
                    if ch==1:
                        self.__menu()
                    elif ch==0:
                        os.system("cls")
                        sys.exit()
                    else:
                        os.system("cls")
                        print("Invalid Choice...")
    
    def __Change_Pin(self):
        import sys
        import os
        accn=input("Enter The Account Number: ")
        accn=self.__get_binary(accn)
        if self.__Accn==accn:
            System_Pin=input("Enter The Old PIN: ")
            System_Pin=self.__get_binary(System_Pin)
            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r+") as f:
                data=f.readlines()
                f.seek(0)
                for i in data:
                    if i.startswith("Account Number: "+accn):
                        x,y=i.split("Pin: ")
                        y,z,extra=y.split(";")
                        if y==System_Pin:
                            New_Pin=input("Set New-Pin: ")
                            if len(New_Pin)==4 and New_Pin.isdigit()==True:
                                New_Pin=self.__get_binary(New_Pin)
                                Re_New_Pin=input("Re-Enter New Pin: ")
                                Re_New_Pin=self.__get_binary(Re_New_Pin)
                                if New_Pin==Re_New_Pin:
                                    i=x+"Pin: "+New_Pin+";"+z+";"+extra
                                    os.system("cls")
                                    import time
                                    print("PIN Changed Successfully...")
                                    time.sleep(2)
                                    print("Go to MENU -[PRESS-> 1]                 EXIT -[PRESS->0]")
                                    ch=int(input("Enter The Choice: "))
                                    if ch==1:
                                        self.__menu()
                                    elif ch==0:
                                        os.system("cls")
                                        sys.exit()
                                    else:
                                        os.system("cls")
                                        print("Invalid Choice...")
                            else:
                                print("PIN Should Consist of 4 Digits Only")
                    f.write(i)
    
    def __Withdraw(self):
        import sys
        import os
        import time
        Withdraw_amount=int(input("Enter The Withdraw Amount: "))
        if Withdraw_amount and Withdraw_amount<=50000:
                from datetime import datetime
                today = datetime.today().strftime("%Y-%m-%d %H:%M")
                self.__last_withdraw=today
                self.__withdraw_history=Withdraw_amount
                with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","a") as f:
                    f.write(f"WITHDRAW|{self.__Accn}|{self.__last_withdraw}|{self.__withdraw_history}\n")
                with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r") as f:
                    history=f.readlines()
                    element=[]
                    for i in history:
                        if i.startswith("WITHDRAW|"+self.__Accn):
                            w,x,y,z=i.split("|")
                            z=int(z)
                            element.append(z)
                    a=sum(element)
                    if a>50000 and y==today:
                        print("Your Maximum Withdrawl Limit Exceed for Today!\nPlease Try After 24 Hours of The Last Withdrawl")
                        with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r+") as f:
                            history=f.readlines()
                            f.seek(0)
                            f.truncate()
                            f.writelines(history[:-1])
                    if x==self.__Accn and y==today and a<=50000:
                        with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r+") as f:
                            data=f.readlines()
                            f.seek(0)
                            for i in data:
                                if i.startswith("Account Number: "+self.__Accn):
                                    x,y=i.split(";Balance: ")
                                    y,extra=y.split(";")
                                    y=self.__decode(y)
                                    int_y=int(y)
                                    if Withdraw_amount<=int_y:
                                        z,pin=x.split(";Pin: ")
                                        pin=self.__decode(pin)
                                        Pin=self.__get_password()
                                        if Pin==pin:
                                            int_y=int_y-Withdraw_amount
                                            y=str(int_y)
                                            y=self.__get_binary(y)
                                            i=x+";Balance: "+y+";"+extra
                                            os.system("cls")
                                            print("Withdrawl Successful.....")
                                        else:
                                            print("Wrong Pin!")
                                            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\History.txt","r+") as f:
                                                history=f.readlines()
                                                f.seek(0)
                                                f.truncate()
                                                f.writelines(history[:-1])
                                                sys.exit()
                                    else:
                                        print("You Don't Have Sufficient Balance in Your Accout...")
                                f.write(i)
                        time.sleep(2)
                        print("Go to MENU -[PRESS-> 1]                 EXIT -[PRESS->0]")
                        ch=int(input("Enter The Choice: "))
                        if ch==1:
                            self.__menu()
                        elif ch==0:
                            os.system("cls")
                            sys.exit()
                        else:
                            os.system("cls")
                            print("Invalid Choice...")        
                            
    def __get_password(self):
        import msvcrt
        prompt="Enter your PIN: "
        print(prompt, end='', flush=True)
        password = ''
        while True:
            char = msvcrt.getch()
            char = char.decode('utf-8')
            if char == '\r' or char == '\n':
                print()
                return password
            elif char == '\b':
                if password:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            else:
                password =password+ char 
                print('*', end='', flush=True)
    
    def __get_binary(self,x):
        binary_value="".join(format(ord(i),"08b") for i in x)
        return binary_value

    def __decode(self,x):
        original_data=" ".join(x[i:i+8] for i in range(0,len(x),8))
        data=original_data.split()
        decimal_value= ''.join(chr(int(i, 2)) for i in data)
        return decimal_value
    
    def __get_pin(self):
        import sys
        import os
        import random
        import time
        os.system("cls")
        accn=input("Enter The Account Number: ")
        accn=self.__get_binary(accn)
        if accn==self.__Accn:
            os.system("cls")
            name=input("Enter Full-Name (add space before surname): ")
            name,surname=name.split()
            name=name.capitalize()
            surname=surname.capitalize()
            name=name+" "+surname
            name=self.__get_binary(name)
            with open("C:\\Users\\abise\\OneDrive\\Documents\\Python Tutorials\\.vscode\\Atm.txt","r") as f:
                data=f.readlines()
                for i in data:
                    i=i.strip()
                    if i.startswith("Account Number: "+accn):
                        x,y=i.split("Customer Name: ")
                        y,z=y.split(";Age: ")
                        if y==name:
                            os.system("cls")
                            otp="{:06d}".format(random.randint(0,999999))
                            end_time=time.time()+30
                            print(f"OTP Generated Successfully...\n{otp} is your One Time Password (OTP) valid upto 30 seconds")
                            votp=input("Enter OTP: ")
                            if otp == votp and time.time()<=end_time:
                                os.system("cls")
                                print("OTP Authentication Successful....")
                                a,b=z.split(";Pin: ")
                                b,c=b.split(";Balance: ")
                                b=self.__decode(b)
                                y=self.__decode(y)
                                g,gender=a.split("Gender: ")
                                if gender.startswith("M"):
                                    print(f"{y} Sir; your Pin is: {b}")
                                    time.sleep(2)
                                    print("Go to MENU -[PRESS-> 1]                 EXIT -[PRESS->0]")
                                    ch=int(input("Enter The Choice: "))
                                    if ch==1:
                                        self.__menu()
                                    elif ch==0:
                                        os.system("cls")
                                        sys.exit()
                                    else:
                                        os.system("cls")
                                        print("Invalid Choice...")
                                elif gender.startswith("F"):
                                    print(f"{y} Mam; your Pin is: {b}")
                                    time.sleep(2)
                                    print("Go to MENU -[PRESS-> 1]                 EXIT -[PRESS->0]")
                                    ch=int(input("Enter The Choice: "))
                                    if ch==1:
                                        self.__menu()
                                    elif ch==0:
                                        os.system("cls")
                                        sys.exit()
                                    else:
                                        os.system("cls")
                                        print("Invalid Choice...")
                                else:
                                    print(f"{y} your Pin is: {b}")
                                    time.sleep(2)
                                    print("Go to MENU -[PRESS-> 1]                 EXIT -[PRESS->0]")
                                    ch=int(input("Enter The Choice: "))
                                    if ch==1:
                                        self.__menu()
                                    elif ch==0:
                                        os.system("cls")
                                        sys.exit()
                                    else:
                                        os.system("cls")
                                        print("Invalid Choice...")
                            elif otp != votp:
                                os.system("cls")
                                print("Wrong One Time Password (OTP)...")
                            elif time.time()>end_time:
                                os.system("cls")
                                print("OTP Expired....")
                        else:
                            print("Wrong Name! Authentication Failed....")
        else:
            print("Wrong Account Number! Please Check The Account Number...")

    def __Advantages(self):
        pass
    def __Limitations(self):
        pass                    

s=ATM()

class Student:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
