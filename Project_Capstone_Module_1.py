listpatient = [
    {
       'patient_code': 'A1',
       'name': 'Millicent Leonardo',
       'nationality': 'Australia',
       'gender': 'Female',
       'age': 20,
       'diagnostic': 'Ultrasound'
      
    },
    {
        'patient_code': 'A2',
        'name': 'Raj Alam',
        'nationality': 'Indonesia',
        'gender': 'Male',
        'age': 19,
        'diagnostic': 'Hearing Test'
    }
 ]

# Function for show all list of Patient on Read/List Menu
def show_all_list_patient():
    if len(listpatient) == 0:
          print('*Table Patient is empty')
          print()
    else:
        print("="*90)
        print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
        for index, item in enumerate(listpatient):
                print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
        print("="*90)
        print()
    listPatientMenu()

# Function For Looping Patient Code
def show_patient(code):
    # A001
    print("="*90)
    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
    for i in listpatient:
        if code == i['patient_code']:
            print(f"{i['patient_code']:<10} {i['name']:<20} {i['nationality']:<15} {i['age']:<10} {i['gender']:<10} {i['diagnostic']:<10}")
    print("="*90)
    print()

# Function For Search Patient's Name
def SearchPatientName():
    if len(listpatient) == 0:
          print('*Table Patient is empty*')
          listPatientMenu()

    inputPatient = input('Input Patient Code: ').capitalize()
    print()

    filtered = list(filter(lambda i: i["patient_code"] == inputPatient, listpatient)) # untuk filter hasi list dalam listpatient,
    if len(filtered) == 0:                                                            # agar hasil True saja yang di proses/di extract
        print("*Patient Data Is Not Existed")
        print()
    else:
        show_patient(filtered[0]["patient_code"])
        
    listPatientMenu()


#Sub Menu LIST/READ 
def listPatientMenu():
    print(f"{'='*10} List of Patient Menus {'='*10}")
    print('''
    1. Show All Patient Table
    2. Search Patient's Name
    3. Back to Menus
    ''')
    print('')
    SelectPatientMenu = input("Input Menus Number: ")
    print('')

    if SelectPatientMenu == "1":
        show_all_list_patient()
    elif SelectPatientMenu == "2":
        SearchPatientName()
    elif SelectPatientMenu == "3":
        menu()
    else:
        print('Menu buttons only Available from 1 to 3')
        print('Pleas Input Your Number Again')
        print()
        listPatientMenu()


#Sub Menu ADD LIST
def addListMenu():
    print(f"{'='*10} Add Patient Menus {'='*10}")
    print('''
    1. Adding New Patient
    2. Back To Menus
    ''')
    print('')
    addlistinput = input("Input Menus Number: ")
    print('')

    if addlistinput == "1":
         addpatient()
    elif addlistinput == "2":
         menu()
    else:
        print('Menu buttons only Available from 1 to 2')
        print('Pleas Input Your Number Again')
        print()
        addListMenu()

#Sub Menu UPDATE LIST
def updateListmenu():
    print(f"{'='*10} Update Patient Menus {'='*10}")
    print('''
    1. Upadate Patient's Data
    2. Back To Menus
    ''')
    print('')
    addlistinput = input("Input Menus Number: ")
    print('')

    if addlistinput == "1":
        updatePatient()
    elif addlistinput == "2":
        menu()
    else:
        print('Menu buttons only Available from 1 to 2')
        print('Pleas Input Your Number Again')
        print()
        updateListmenu()

#Sub Menu DELETE LIST
def deleteListmenu():
    print(f"{'='*10} Delete Patient Menus {'='*10}")
    print('''
    1. Delete Patient's Data
    2. Back To Menus
    ''')
    print('')
    addlistinput = input("Input Menus Number: ")
    print('')

    if addlistinput == "1":
        deletelist()
    elif addlistinput == "2":
        menu()
    else:
        print('Menu buttons only Available from 1 to 2')
        print('Pleas Input Your Number Again')
        print()
        deleteListmenu()

# Add Patient
def addpatient():
    while True:
        inputNewpatientCode = input('Enter New Code For Patient: ').capitalize()
        filtered = list(filter(lambda i: i["patient_code"] == inputNewpatientCode, listpatient)) # untuk filter hasil list dalam listpatient,agar hasil True saja yang di proses/di extract
        if inputNewpatientCode == "":
            print("Can't Input Blank Space!")
            print()
            continue
        elif len(filtered) == 0:                                                            
            break
        else:
            print('*Sorry, Patient Code Is Already Taken!*')
            print()
            continue
    
    while True:
        inputNewpatientName = input("Enter Patient's Name: ").title()
        if inputNewpatientName == "":
            print("Can't Input Blank Space!")
            print()
            continue
        elif all(i.isspace() for i in inputNewpatientName):
            print('Input Must Aplhabets!')
            print()
            continue
        elif all(i.isalpha() or i.isspace() for i in inputNewpatientName):
            break
        else:
            print("Input Must Aplhabets!")
            print()
            continue

    while True:
        inputNewpatientNationality = input("Enter Patient's Nationality: ").title()
        if inputNewpatientNationality == "":
            print("Can't Input Blank Space!")
            print()
            continue
        elif all(i.isspace() for i in inputNewpatientNationality):
            print('Input Must Aplhabets!')
            print()
            continue
        elif all(i.isalpha() or i.isspace() for i in inputNewpatientNationality):
            break
        else:
            print("Input Must Aplhabets!")
            print()

    while True:
        inputNewpatientGender = input("Enter Patient's Gender: ").capitalize()
        if inputNewpatientGender == "":
            print("Can't Input Blank Space!")
            print()
            continue
        elif all(i.isspace() for i in inputNewpatientGender):
            print('Input Must Aplhabets!')
            print()
            continue
        elif all(i.isalpha() or i.isspace() for i in inputNewpatientGender):
            break
        else:
            print("Input Must Aplhabets!")
            print()
            
    while True:
        inputNewpatientAge = input("Enter Patient's Age: ")
        if inputNewpatientAge == "":
            print("Can't Input Blank Space!")
            print()
            continue
        elif all(i.isnumeric()for i in inputNewpatientAge):
            break
        else:
            print("Input Must Numeric!")
            print()
            continue

    while True:
        inputNewpatientDiagnostic = input("Enter Patient's Diagnostic Type: ").capitalize()
        if inputNewpatientDiagnostic == "":
            print("Can't Input Blank Space!")
            print()
            continue
        elif all(i.isspace() for i in inputNewpatientDiagnostic):
            print('Input Must Aplhabets!')
            print()
            continue
        elif all(i.isalpha() or i.isspace() for i in inputNewpatientDiagnostic):
            break
        else:
            print("Input Must Aplhabets!")
            print()
    
    # Looping For Confirmation Save New Data
    while True:
        inputNewpatientConfirm = input('To Finish This Action, Please Confirm Y/N: ')

        if inputNewpatientConfirm.capitalize() == 'Yes' or inputNewpatientConfirm.capitalize() == 'Y':
            listPatientnew ={
                 
                'patient_code': inputNewpatientCode,
                'name'        : inputNewpatientName,
                'nationality' : inputNewpatientNationality,
                'gender'      : inputNewpatientGender,
                'age'         : inputNewpatientAge,
                'diagnostic'  : inputNewpatientDiagnostic
                      
            }
            listpatient.append(listPatientnew)
            print("New Patient's Record Has Been Saved!")
            print(listpatient)
            addListMenu()
        elif inputNewpatientConfirm.capitalize() == 'No' or inputNewpatientConfirm.capitalize() == 'N':
            print('Adding New Patient Action is Cancel')
            addListMenu()
            print()
        else:
             print('*Your Input is Invalid*')
             print()

#Update Patient
def updatePatient():
    while True:
        inputUpdateCode = input("Enter Patient's Code: ").capitalize()
        filtered = list(filter(lambda i: i["patient_code"] == inputUpdateCode, listpatient))
        if len(filtered) == 0:                                                           
            print("*Patient Data Is Not Existed")
            print()
            updatePatient()
        else:
            show_patient(filtered[0]["patient_code"])
            while True:
                confirm = input("Is This The Right Patient's Code You want To Update? Y/N: ").capitalize()
                if confirm == 'Yes' or confirm == 'Y':
                    print('''
        List Table Rows:
        1. Name
        2. Nationality
        3. Age
        4. Diagnostic Type

    For Cancel This Action Enter '5'
                ''')
                    while True:
                        inputSelect = input("Which Column You Want To Change: ")
                        print()
                        if inputSelect == "":
                            print('Your Input Is Invalid!')
                            print()
                            continue
                        if inputSelect == "1":
                            while True:
                                inputNewPatientName = input("Enter New Name: ").title()
                                if inputNewPatientName =="":
                                    print("Can't Input Blank Space!")
                                    print()
                                    continue
                                elif all(i.isspace() for i in inputNewPatientName):
                                    print('Input Must Aplhabets!')
                                    print()
                                    continue
                                elif all(i.isalpha() or i.isspace() for i in inputNewPatientName):
                                    pass
                                else:
                                    print("Input Must Aplhabets!")
                                    print()
                                    continue
                                inputConfirm = input('Are You Sure Want To Save? Y/N: ').capitalize()
                                if inputConfirm == 'Yes' or inputConfirm == 'Y':
                                    filtered[0]["name"] = inputNewPatientName
                                    print("*Updating Data Is Success!*")
                                    print()
                                    updateListmenu()
                                elif inputConfirm == 'No' or inputConfirm == 'N':
                                    print("*Updating Data Is Cancel!*")
                                    print()
                                    updateListmenu()
                                else:
                                    print("Your Input Is Invalid!")
                                    print()
                                    continue

                        elif inputSelect == "2":
                            while True:
                                inputNewPatientNatioanlity = input('Enter New Nationality: ').title()
                                if inputNewPatientNatioanlity == "":
                                    continue
                                elif all(i.isspace() for i in inputNewPatientNatioanlity):
                                    print('Input Must Aplhabets!')
                                    print()
                                    continue
                                elif all(i.isalpha() or i.isspace() for i in inputNewPatientNatioanlity):
                                    pass
                                else:
                                    print("Input Must Aplhabets!")
                                    print()
                                    continue
                                inputConfirm = input('Are You Sure Want To Save? Y/N: ').capitalize()
                                if inputConfirm == 'Yes' or inputConfirm == 'Y':
                                    filtered[0]["nationality"] = inputNewPatientNatioanlity
                                    print("*Updating Data Is Success!*")
                                    print()
                                    updateListmenu()
                                elif inputConfirm == 'No' or inputConfirm == 'N':
                                    print("*Updating Data Is Cancel!*")
                                    print()
                                    updateListmenu()
                                else:
                                    print("Your Input Is Invalid!")
                                    print()
                                    continue

                        elif inputSelect == "3":
                            while True:
                                inputNewPatientAge = input('Enter New Age: ').capitalize()
                                if inputNewPatientAge == "":
                                    print("Can't Input Blank Space!")
                                    continue
                                elif all(i.isnumeric()for i in inputNewPatientAge):
                                    pass
                                else:
                                    print("Input Must Numeric!")
                                    print()
                                    continue
                                inputConfirm = input('Are You Sure Want To Save? Y/N: ').capitalize()
                                if inputConfirm == 'Yes' or inputConfirm == 'Y':
                                    filtered[0]["age"] = inputNewPatientAge
                                    print("*Updating Data Is Success!*")
                                    print()
                                    updateListmenu()
                                elif inputConfirm == 'No' or inputConfirm == 'N':
                                    print("*Updating Data Is Cancel!*")
                                    print()
                                    updateListmenu()
                                else:
                                    print("Your Input Is Invalid!")
                                    print()
                                    continue

                        elif inputSelect == "4":
                            while True:
                                inputNewPatientDiagnostic = input('Enter New Diagnostic: ').capitalize()
                                if inputNewPatientDiagnostic == "":
                                    continue
                                elif all(i.isspace() for i in inputNewPatientDiagnostic):
                                    print('Input Must Aplhabets!')
                                    print()
                                    continue
                                elif all(i.isalpha() or i.isspace() for i in inputNewPatientDiagnostic):
                                    pass
                                else:
                                    print("Input Must Aplhabets!")
                                    print()
                                    continue
                                inputConfirm = input('Are You Sure Want To Save? Y/N: ').capitalize()
                                if inputConfirm == 'Yes' or inputConfirm == 'Y':
                                    filtered[0]["diagnostic"] = inputNewPatientDiagnostic
                                    print("*Updating Data Is Success!*")
                                    print()
                                    updateListmenu()
                                elif inputConfirm == 'No' or inputConfirm == 'N':
                                    print("*Updating Data Is Cancel!*")
                                    print()
                                    updateListmenu()
                                else:
                                    print("Your Input Is Invalid!")
                                    print()
                                    continue
                        elif inputSelect == "5":
                            updateListmenu()
                        else:
                            print("*Option Only Available From 1 to 5*")
                            print()
                            continue
                elif confirm  == 'No' or confirm == 'N':
                    print('*Your Action Has Been Cancel*')
                    print()
                    updateListmenu()
                else:
                    print("Your Input Is Invalid!")
                    print()
                    continue

#Delete Patient                
def deletelist():
    print("Warning: You Can't Revert Back The Changes After Confirmation")
    inputDeletePatientCode = input("Enter Which Patient's Code Will Be Remove: ").capitalize()
    filtered = list(filter(lambda i: i["patient_code"] == inputDeletePatientCode, listpatient)) #Ini digunakan untuk cek apakah Code ada di list atau tidak.
    if len(filtered) == 0:                                                     
        print("*Patient Data Is Not Existed*")
        print()
        deletelist()
    else:
        for i, item in enumerate(listpatient):
            if inputDeletePatientCode == item["patient_code"]:
                while True:
                    inputConfirm = input('Are You Sure Want Delete This Data? Y/N: ').capitalize()
                    if inputConfirm == 'Yes' or inputConfirm == 'Y':
                        del listpatient[i]
                        print("*Deleting Patient'S Data Is Success*")
                        print()
                        deleteListmenu()
                    elif inputConfirm == 'No' or inputConfirm == 'N':
                        print('*Your Action Has Been Cancel*')
                        print()
                        deleteListmenu()
                    else:
                        print("Your Input Is Invalid!")
                        print()
                    

def menu():
    print()
    print(f"{'='*10} Osborne Park Hospital Patient's Data {'='*10}")
    print('''
    List Menu:
    1. List of Patient
    2. Add list
    3. Update list
    4. Delete list
    5. Exit Program''')

    print('')
    print('J&A® 1990-1993' )
    print('')
    selectMenu = input("Input Menus Number: ")
    print('')

    if selectMenu == "1":
            listPatientMenu()
    elif selectMenu == "2":
            addListMenu()
    elif selectMenu == "3":
            updateListmenu()
    elif selectMenu == "4":
            deleteListmenu()
    elif selectMenu == "5":
            print(f"{'':<5}We show empathy, kindness and compassion to all :)")
            print()
            exit()
    else:
            print('*Menu buttons only Available from 1 to 5*')
            print('*Please Input Your Number Again*')
            print()
            menu()
            
menu()