Contact = {}

def ShowFuntion():
    print(Contact.items())
    print("Name \t Contact")
    for key in Contact:
        print("{} \t {}".format(key,Contact.get(key)))
while True:
    choice = int(input("1. Add New Contact\n"
                    "2. Search the Contact\n"
                    "3. Display the contact\n"
                    "4. Edit the contact\n"
                    "5. Delete  the contact\n"
                    "6. Exit\n"
                    "Please write the number between 1-6: "))


    if choice == 1:
        name = input("Add your contact name: ")
        phone = input("Add your phone number:")
        Contact[name] = phone

    elif choice == 2:
       ContactName =  input("search the contact: ")
       if ContactName in Contact:
           print(ContactName, "contact number is: ", Contact[ContactName])
       else:
           print("Not found the contact number")

    elif choice == 3:
        if not Contact:
            print("Contact book is empty")
        else:
            ShowFuntion()

    elif choice == 4:
        EditContact = input ("Edit your contact: ")
        if EditContact in Contact:
            phone = input("Change your number:")
            Contact[EditContact] = phone
            print ("Contact Updated Successfully")
            ShowFuntion()
        else:
            print("name is not found")

    elif choice == 5:
        Del_Contact = input("Which contact do you want to delete?")
        if Del_Contact in Contact:
            DeleteConfirm = input("do you want to delete this contact y/n")
            if DeleteConfirm == "y" or DeleteConfirm == "y":
                Contact.pop(Del_Contact)
            ShowFuntion()

        else:
            print("the name is not found in the contact")

    else:
        break