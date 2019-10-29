from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time
def askpin():
    global card_noandpin
    card_no = simpledialog.askinteger("Card Number", "Please Enter Your Card Number:", minvalue=1, maxvalue=100)
    print(card_no)
    pin = simpledialog.askinteger("PIN", 'Enter 4 digit PIN', minvalue=1000, maxvalue=9999)
    print(pin)
    card_noandpin = str(card_no) + str(pin)
    fh = open('pin.txt', 'r')
    data = fh.read()
    print(data)
    if card_noandpin in data:
        messagebox.showinfo('Login', "Correct")
        fh.close()
    else:
        messagebox.showinfo('Pin', 'Invalid Card Number or PIN')
        fh.close()
        askpin()


def bal():
    print('inside bal')
    global card_noandpin
    fh = open('account.txt')
    for line in fh:
        if card_noandpin in line:
            line = line.rstrip()
            a = line.split()
            messagebox.showinfo('Balance', 'Your Balance is{}:'.format(a[2]))
            fh.close()
            break


def withdrawal():
    current_amt1 = 0
    current_amt2 = 0
    global card_noandpin
    with open('account.txt') as ff:
        for line in ff:
            if line.startswith(card_noandpin):
                line = line.rstrip()
                a = line.split()
                current_amt1 = int(a[2])
                withdrawammt = simpledialog.askinteger('Withdraw',
                                                       "Enter the amount to be withdrawed(multiples 0f 100s:")
                if withdrawammt == None:
                    return
                else:
                    if withdrawammt % 100 != 0 or withdrawammt <= 0:
                        messagebox.showerror("Error", 'Plese enter only multiples of 100s')
                        withdrawal()
                    else:
                        if withdrawammt > current_amt1:
                            messagebox.showerror('Error', 'Amount exceeded')
                            withdrawal()
                        elif withdrawammt < current_amt1:
                            current_amt2 = current_amt1 - withdrawammt

    record = ""
    flag = 0
    with open('account.txt') as fh:
        fh.seek(0)
        for line in fh:
            if line.startswith(card_noandpin) and flag == 0:
                line = line.replace(str(current_amt1), str(current_amt2))
                record += line
                flag = 1
            else:
                record += line

    with open('account.txt', 'w') as ff:
        ff.writelines(record)
        messagebox.showinfo("Done", 'Successfull')


def deposits():
    current_amt1 = 0
    current_amt2 = 0
    global card_noandpin
    with open('account.txt') as ff:
        for line in ff:
            if line.startswith(card_noandpin):
                line = line.rstrip()
                a = line.split()
                current_amt1 = int(a[2])
                depositamt = simpledialog.askinteger('Deposit',
                                                     "Enter the amount to be Deposited(multiples 0f 100s:")
                if depositamt == None:
                    return
                else:
                    if depositamt % 100 != 0 or depositamt <= 0:
                        messagebox.showerror("Error", 'Plese enter only multiples of 100s')
                        deposits()
                    else:
                        current_amt2 = depositamt + current_amt1

    record = ""
    flag = 0
    with open('account.txt') as fh:
        fh.seek(0)
        for line in fh:
            if line.startswith(card_noandpin) and flag == 0:
                line = line.replace(str(current_amt1), str(current_amt2))
                record += line
                flag = 1
            else:
                record += line

    with open('account.txt', 'w') as ff:
        ff.writelines(record)
        messagebox.showinfo("Done", 'Successfull')


def trans():
    acc_no = simpledialog.askinteger('Acc_no', "Enter the account number to be transferred", minvalue=100000,
                                     maxvalue=999999)
    if acc_no==None:
        return
    acc_no = str(acc_no)
    current_amt1 = 0
    current_amt2 = 0
    depositamt = 0
    global card_noandpin
    with open('account.txt') as ff:
        for line in ff:
            if line.startswith(card_noandpin):
                line = line.rstrip()
                a = line.split()
                current_amt1 = int(a[2])
                depositamt = simpledialog.askinteger('Deposit',
                                                     "Enter the amount to be Deposited(multiples 0f 100s:")
                if depositamt == None:
                    return
                else:
                    if depositamt % 100 != 0 or depositamt <= 0:
                        messagebox.showerror("Error", 'Please enter only multiples of 100s')
                        return
                '''
                withdrawammt = simpledialog.askinteger('Withdraw',
                                                       "Enter the amount to be withdrawed(multiples 0f 100s:")
                if withdrawammt != None:
                    if withdrawammt % 100 != 0 or withdrawammt <= 0:
                        messagebox.showerror("Error", 'Plese enter only multiples of 100s')
                        withdrawal()
                    else:'''
            if depositamt!=None and current_amt1 < depositamt:
                messagebox.showerror('Error', 'Amount exceeded')
                return

            elif depositamt!=None:
                current_amt2 = current_amt1 - depositamt

    record = ""
    flag = 0
    with open('account.txt') as fh:
        fh.seek(0)
        for line in fh:
            if line.startswith(card_noandpin) and flag == 0:
                line = line.replace(str(current_amt1), str(current_amt2))
                record += line
                flag = 1
            else:
                record += line

    with open('account.txt', 'w') as ff:
        ff.writelines(record)
        messagebox.showinfo("Done", 'Successfull')

    current_amt1 = 0
    current_amt2 = 0
    # global card_noandpin
    with open('account.txt') as ff:
        for line in ff:
            if line.startswith(acc_no):
                line = line.rstrip()
                a = line.split()
                current_amt1 = int(a[2])
                '''
                depositamt = simpledialog.askinteger('Deposit',
                                                     "Enter the amount to be Deposited(multiples 0f 100s:")
                if depositamt != None:
                    if depositamt % 100 != 0 or depositamt <= 0:
                        messagebox.showerror("Error", 'Plese enter only multiples of 100s')
                        deposits()
                    else:
                    '''
                current_amt2 = depositamt + current_amt1

    record = ""
    flag = 0
    with open('account.txt') as fh:
        fh.seek(0)
        for line in fh:
            if line.startswith(acc_no) and flag == 0:
                line = line.replace(str(current_amt1), str(current_amt2))
                record += line
                flag = 1
            else:
                record += line

    with open('account.txt', 'w') as ff:
        ff.writelines(record)
        messagebox.showinfo("Done", 'Successfull')


def changepinn():
    flag=0
    global card_noandpin
    card_no = simpledialog.askinteger('card_no', 'Please enter your Card Number')
    if card_no==None:
        return
    old_pin = simpledialog.askinteger('OldPIN', 'Please enter your Old 4 Digit PIN ')
    if old_pin==None:
        return
    new_pin = simpledialog.askinteger('NewPIN', 'Please enter your NEW 4 Digit PIN ')
    if new_pin==None:
        return
    newcardnoandpin = str(card_no) + str(old_pin)
    newcardnoandnewpin=str(card_no)+str(new_pin)
    print('new pin=', newcardnoandpin)
    record = ''
    with open('account.txt') as fh:
        if card_noandpin == newcardnoandpin:
            for line in fh:
                if line.startswith(card_noandpin) and flag == 0:
                    line = line.replace(str(card_noandpin), str(newcardnoandnewpin))
                    record += line
                    print('new record',record)
                    flag = 1
                else:
                    record += line
        else:
            messagebox.showerror('PIN', 'Invalid PIN or Card Number')
            fh.close()
            return

    with open('account.txt', 'w') as ff:
        ff.writelines(record)
       # messagebox.showinfo("Done", 'Successfull')
        #card_noandpin=newcardnoandnewpin
    record=''
    flag=0
    with open('pin.txt') as fh:
        for line in fh:
            if line.startswith(card_noandpin) and flag==0:
                line=line.replace(str(card_noandpin),str(newcardnoandnewpin))
                record+=line
                flag=1
            else:
                record+=line
    with open('pin.txt', 'w') as ff:
        ff.writelines(record)
        messagebox.showinfo("Done", 'Successfull')
        card_noandpin = newcardnoandnewpin


root = Tk()
root.title("Automated Teller Machine (ATM)")
root.geometry('800x600')
root.config(bg='#134566')

askpin()

label = Label(root, text="Automated Teller Machine (ATM)",bg='#134566', fg="#987645", font=('arial', 12))
label.place(x=300, y=10)
times = time.strftime('%H:%M:%S:%p')
label2 = Label(root, text=times, bg='#134566', fg="white", font=('arial', 12))
label2.place(x=700, y=25)
balance = Button(root, text='Balance', command=bal, bg='navajo white')
balance.config(height=3, width=15)
balance.place(x=50, y=70)
exits = Button(root, text='Cancel', command=exit, bg='Red')
exits.config(height=2, width=100)
exits.place(x=50, y=550)
withdraw = Button(root, text="Withdrawal", bg="navajo white", height=3, width=15, command=withdrawal)
withdraw.place(x=650, y=70)
deposit = Button(root, text="Deposit", bg="navajo white", height=3, width=15, command=deposits)
deposit.place(x=50, y=400)
transfer = Button(root, text='Transfer', bg="navajo white", height=3, width=15, command=trans)
transfer.place(x=650, y=400)
changepin = Button(root, text='Change PIN', bg="navajo white", height=3, width=15, command=changepinn)
changepin.place(x=350, y=400)
root.mainloop()
