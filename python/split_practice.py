import datetime
current_date = datetime.date.today()
'''
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
        date_diff=expiry_date-current_date
        num=date_diff.days
        if acc['CardNumber']==cno and acc['PIN']==pin:
            if num>=0:
                return 'Your Card had Expired.'
            else:
                return acc['Amount']
    else:
        return 'Invalid Card Details'
    f.close()
print(balance_enquiry(122323454507,7777))
'''

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
                    return 'Successfully updated'
                else:
                    return 'Please try again'
            else:
                return 'Your Card had Expired'
    else:
        return 'Invalid Card Details'
    f.close()
print(changing_pin(122323454506,6666))