def create():
    f = open('jashvith.txt','a')
    name = input('Enter Contact Name : ')
    number = input('Enter Contact Number : ')
    f.write(f'{name} : {number},{}')
    print('Contact saved successfully')
    f.close()

def display():
    f = open('jashvith.txt','r')
    print('Contacts...')
    contacts = f.read()
    print(contacts)
    f.close()

def search():
    f = open('jashvith.txt','r')
    key_name = input('Enter name to be searched : ')
    contacts = f.readlines()
    for contact in contacts:
        p_name,p_number = contact.strip().split(' : ')
        if p_name==key_name or p_number==key_name:
            print(contact)
            break
    else:
        print('Contact Not Found')
    f.close()

def delete():
    f=open('jashvith.txt','r')
    contacts = f.readlines()
    f.close()
    key = input('Enter name or number to be deleted :')
    for contact in contacts:
        p_name,p_number = contact.strip().split(' : ')
        if key==p_name or key==p_number:
            contacts.remove(contact)
            print('Contact deleted successfully')
            f=open('jashvith.txt','w')
            f.writelines(contacts)
            f.close()
            break
    else:
        print('Contact Not Found !')
def update():
    f = open('jashvith.txt', 'r')
    contacts = f.readlines()
    f.close()
    key = input('Enter name or number to be change :')
    for contact in contacts:
        p_name, p_number = contact.strip().split(' : ')
        if key == p_name or key == p_number:
            contacts.remove(contact)
            print('Contact found to update')
            f = open('jashvith.txt', 'w')
            f.writelines(contacts)
            f.close()
            f = open('jashvith.txt', 'a')
            name = input('Enter Contact Name to update : ')
            number = input('Enter Contact Number to update : ')
            f.write(f'{name} : {number}\n')
            print('Contact updated successfully')
            f.close()
            break
    else:
        print('Contact not found !')
def inpt():
    f=True
    c=0
    while f:
        n=int(input('select the option to proceed\nEnter 1 create to new contact\nEnter 2 To display contacts\nEnter 3 To search contact\nEnter 4 To delete contact\nEnter 5 To update contact\nEnter 0 to Exit\nEnter the input : '))
        if n==0:
            print('THANK YOU FOR CONTACTING US')
            f=False
            return
        elif n==1:
            create()
        elif n==2:
            display()
        elif n==3:
            search()
        elif n==4:
            delete()
        elif n==5:
            update()
        else:
            if c==2:
                print('YOU HAD ENTERED THE MAXIMUM ATTEMPTS,PLEASE TRY AGAIN LATER !')
                f=False
                return
            c+=1
inpt()