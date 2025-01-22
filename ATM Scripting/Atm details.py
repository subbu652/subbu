import datetime
current_date = datetime.date.today()

def menu():
    print('Press 1 for Balance Enquiry')
    print('Press 2 for Cash With-Draw')
    print('Press 3 changing Pin')
    print('Press 4 for Bank Details')
    print('Press q for Quit')

def balance_enquiry(cno,pin):
    f = open('atm.txt','r')
    accounts=f.readlines()
    for account in accounts:
        parts = account.split(',')
        acc={}
        for part in parts:
            key,value=part.split(':')
            acc[key]=value
        acc['PIN'] = acc['PIN'].replace('\n', "")
        expiry_date = datetime.datetime.strptime(acc['Expiry_Date'], '%Y-%m-%d').date()
        date_diff=current_date-expiry_date
        num=date_diff.days
        if acc['CardNumber']==cno and acc['PIN']==pin:
            if num>=0:
                return 'Your Card had Expired.'
            else:
                return acc['Amount']
    else:
        return 'Invalid Card Details'
    f.close()

def cash_withdraw(cno,pin):
    f = open('atm.txt','r')
    accounts=f.readlines()
    for account in accounts:
        parts = account.split(',')
        acc={}
        for part in parts:
            key,value=part.split(':')
            acc[key] = value
        acc['PIN'] = acc['PIN'].replace('\n', "")
        expiry_date = datetime.datetime.strptime(acc['Expiry_Date'], '%Y-%m-%d').date()
        date_diff = current_date-expiry_date
        num = date_diff.days
        if acc['CardNumber']==cno and acc['PIN']==pin:
            if num<0:
                acc_balance=int(acc['Amount'])
                amount_withdraw=int(input('Enter amount for with draw : '))
                if amount_withdraw<=acc_balance:
                    print('Please Collect your amount')
                    aw=acc_balance-amount_withdraw
                    update_transaction("atm.txt",acc_balance,aw,cno)
                    return f'Remaining_Balance : {str(aw)}'
                else:
                    return 'In-sufficient Amount'
            else:
                return 'Your Card had Expired'
    return 'Invalid Card Details'
    f.close()

def changing_pin(cno,pin):
    f = open('atm.txt', 'r')
    accounts = f.readlines()
    for account in accounts:
        parts = account.split(',')
        acc = {}
        for part in parts:
            key, value = part.split(':')
            acc[key] = value
        acc['PIN'] = acc['PIN'].replace('\n', "")
        expiry_date = datetime.datetime.strptime(acc['Expiry_Date'], '%Y-%m-%d').date()
        date_diff = current_date - expiry_date
        num = date_diff.days
        if acc['CardNumber']==cno and pin==acc['PIN']:
            if num<0:
                new_pin1=input('Enter your new pin : ')
                new_pin2=input('Again enter your new pin : ')
                if new_pin1==new_pin2:
                    acc['PIN']=new_pin1
                    update_pin("atm.txt",pin,new_pin2)
                    return 'Successfully updated'
                else:
                    return 'Please try again'
            else:
                return 'Your Card had Expired'
    else:
        return 'Invalid Card Details'
    f.close()

def details(cno,pin):
    f = open('atm.txt', 'r')
    accounts = f.readlines()
    for account in accounts:
        parts = account.split(',')
        acc = {}
        for part in parts:
            key, value = part.split(':')
            acc[key] = value
        acc['PIN'] = acc['PIN'].replace('\n', "")
        expiry_date = datetime.datetime.strptime(acc['Expiry_Date'], '%Y-%m-%d').date()
        date_diff = current_date - expiry_date
        num = date_diff.days
        if acc['CardNumber'] == cno and pin == acc['PIN']:
            if num<0:
                for k,v in acc.items():
                    print(k,':',v)
                return
            else:
                return 'Your Card had Expired'
    else:
        return 'Invalid Card Details'
    f.close()

def update_pin(file_path, old_pin, new_pin):
    f=open(file_path, 'r')
    accounts = f.readlines()
    f=open(file_path, 'w')
    for account in accounts:
        if old_pin in account:
            account = account.replace(old_pin, new_pin)
        f.write(account)

def update_transaction(file_path, old_amount, new_amount,card_number):
    with open(file_path, 'r') as file:
        accounts = file.readlines()
    with open(file_path, 'w') as file:
        for account in accounts:
            str_old_amount = str(old_amount)
            str_new_amount = str(new_amount)
            if card_number in account:
                account = account.replace(str_old_amount, str_new_amount)
            file.write(account)

card_num=input('Please insert your card : ')
f=True
c=0
while f:
    menu()
    button=input()
    if button=='q':
        print('Thankyou for banking')
        break
    elif button=='1':
        pin=input('Please enter your pin : ')
        print('Balance :',balance_enquiry(card_num,pin))
    elif button=='2':
        pin=input('Please enter your pin : ')
        print(cash_withdraw(card_num,pin))
    elif button=='3':
        pin=input('Please enter your pin : ')
        print(changing_pin(card_num,pin))
    elif button=='4':
        pin=input('Please enter your pin : ')
        print(details(card_num,pin))
    else:
        if c==2:
            print('YOU HAD ENTERED WRONG INPUT\nMAXIMUM ATTEMPTS COMPLETED,PLEASE TRY AGAIN LATER !')
            f=False
            break
        print('Click Menu')
        c+=1