listpatient = [
    {
       'patient_code': 'A1',
       'name': 'Millicent Leonardo',
       'nationality': 'United States',
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
    },
    {
        'patient_code': 'B3',
        'name': 'Audrey Simmonds L',
        'nationality': 'Australia',
        'gender': 'Female',
        'age': 5,
        'diagnostic': 'Hearing Test'
    },
     {
        'patient_code': 'A3',
        'name': 'Joel Simmonds',
        'nationality': 'Australia',
        'gender': 'Male',
        'age': 19,
        'diagnostic': 'X Ray'
    }
 ]

# Function for show all list of Patient on Read/List Menu
def show_all_list_patient():
    data =sorted(listpatient, key=lambda k: k['patient_code'])
    if len(listpatient) == 0:
          print('*Table Patient is empty')
          print()
    else:
        print("="*90)
        print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
        for index, item in enumerate(data):
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

    filtered = list(filter(lambda i: i["patient_code"] == inputPatient, listpatient)) # untuk filter hasi list dalam listpatient,agar hasil True saja yang di proses/di extract
    if len(filtered) == 0:                                                            #jika tablenya kosong maka diartikan data pasien tidak ditemukan                                                           
        print("*Patient Data Is Not Existed")
        print()
    else:
        show_patient(filtered[0]["patient_code"])
        
    listPatientMenu()

#Function for show all patient Filter
def show_all_Patient_filter():
    while True:
        print('''
    Search Based Filter
    1.Nationality
    2.Gender
    3.Diagnostic Type
    4.Age

    For Cancel This Action Enter '5'
    ''')
        UserFilter = input("Based On What You Want to Search: ")
        if UserFilter == "1":
            UserFilter_Nationality = input("Enter What Nationality Would You Like To Find: ").title()
            filtered = list(filter(lambda i: i["nationality"] == UserFilter_Nationality, listpatient))

            if len(filtered) == 0:
                print("Data not found")
                print()
                listPatientMenu()

            print("="*90)
            print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
            for i in filtered:
                print(f"{i['patient_code']:<10} {i['name']:<20} {i['nationality']:<15} {i['age']:<10} {i['gender']:<10} {i['diagnostic']:<10}")

        elif UserFilter == "2":
            UserFilter_Gender = input("Enter What Gender Would You Like To Find: ").capitalize()
            filtered = list(filter(lambda i: i["gender"] == UserFilter_Gender, listpatient))

            if len(filtered) == 0:
                print("Data not found")
                print()
                listPatientMenu()
            print("="*90)
            print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
            for i in filtered:
                print(f"{i['patient_code']:<10} {i['name']:<20} {i['nationality']:<15} {i['age']:<10} {i['gender']:<10} {i['diagnostic']:<10}")
                

        elif UserFilter == "3":
            UserFilter_Diagnostic = input("Enter What Diagnostic Type Would You Like To Find: ").title()
            filtered = list(filter(lambda i: i["diagnostic"] == UserFilter_Diagnostic, listpatient))

            if len(filtered) == 0:
                print("Data not found")
                print() 
                listPatientMenu()
            print("="*90)
            print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
            for i in filtered:
                print(f"{i['patient_code']:<10} {i['name']:<20} {i['nationality']:<15} {i['age']:<10} {i['gender']:<10} {i['diagnostic']:<10}")
        
        elif UserFilter == "4":
            UserFilter_Age = input("Enter What Age Type Would You Like To Find: ")
            if UserFilter_Age == "":
                print("Data Not Found")
                print() 
                listPatientMenu()
            elif all(i.isnumeric()for i in UserFilter_Age):
                pass
            else:
                print("Data Not Found")
                print() 
                listPatientMenu()
            filtered = list(filter(lambda i: i["age"] == int(UserFilter_Age), listpatient))
            if len(filtered) == 0:
                print("Data not found")
                print() 
                listPatientMenu()
            print("="*90)
            print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
            for i in filtered:
                print(f"{i['patient_code']:<10} {i['name']:<20} {i['nationality']:<15} {i['age']:<10} {i['gender']:<10} {i['diagnostic']:<10}")
        
        elif UserFilter == "5":
            print()
            listPatientMenu()
        else:
            print("Button Only Available from 1 to 5")
            show_all_Patient_filter()
            print()
            
        print("="*90)
        print()
        listPatientMenu()

# Function Sort
def show_all_Patient_sort():
    if len(listpatient) == 0:
        print('*Table Patient is empty')
        print()
        listPatientMenu()
    while True:
        print('''
    Sort:
    1.Name
    2.Gender
    3.Diagnostic Type
    4.Age
    5.Nationality

    For Cancel This Action Enter '6'
        ''')

        inputsort = input(f'Based On What You Want To Sort: ')
        if inputsort == '1':
            while True:
                inputsort1 = input(f'Choose Sequence Type(ASC/DESC): ').upper()
                if inputsort1 == 'ASC':
                    dataASC_Name =sorted(listpatient, key=lambda k: k['name'])
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataASC_Name):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                elif inputsort1 == 'DESC':
                    dataDESC_Name =sorted(listpatient, key=lambda k: k['name'],reverse=True)
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataDESC_Name):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                else:
                    print(f'Your Input Is Invalid')
                    print()

        elif inputsort == '2':
            while True:
                inputsort2 = input(f'Choose Sequence Type(ASC/DESC): ').upper()
                if inputsort2 == 'ASC':
                    dataASC_Gender =sorted(listpatient, key=lambda k: k['gender'])
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataASC_Gender):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                elif inputsort2 == 'DESC':
                    dataDESC_Gender =sorted(listpatient, key=lambda k: k['gender'],reverse=True)
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataDESC_Gender):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                else:
                    print(f'Your Input Is Invalid')
                    print()
        elif inputsort == '3':
            while True:
                inputsort3 = input(f'Choose Sequence Type(ASC/DESC): ').upper()
                if inputsort3 == 'ASC':
                    dataASC_Diagnostic =sorted(listpatient, key=lambda k: k['diagnostic'])
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataASC_Diagnostic):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                elif inputsort3 == 'DESC':
                    dataDESC_Diagnostic =sorted(listpatient, key=lambda k: k['diagnostic'],reverse=True)
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataDESC_Diagnostic):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                else:
                    print(f'Your Input Is Invalid')
                    print()
        elif inputsort == '4':
            while True:
                inputsort3 = input(f'Choose Sequence Type(ASC/DESC): ').upper()
                if inputsort3 == 'ASC':
                    dataASC_Age =sorted(listpatient, key=lambda k: k['age'])
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataASC_Age):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                elif inputsort3 == 'DESC':
                    dataDESC_Age =sorted(listpatient, key=lambda k: k['age'],reverse=True)
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataDESC_Age):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
        elif inputsort == '5':
            while True:
                inputsort5 = input(f'Choose Sequence Type(ASC/DESC): ').upper()
                if inputsort5 == 'ASC':
                    dataASC_Nationality =sorted(listpatient, key=lambda k: k['nationality'])
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataASC_Nationality):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                elif inputsort5 == 'DESC':
                    dataDESC_Nationality =sorted(listpatient, key=lambda k: k['nationality'],reverse=True)
                    print("="*90)
                    print(f'{"Code":<10} {"Name":<20} {"Nationality":<15} {"Age":<10} {"Gender":<10} {"Diagnostic Test":<10}')
                    for index, item in enumerate(dataDESC_Nationality):
                            print(f"{item['patient_code']:<10} {item['name']:<20} {item['nationality']:<15} {item['age']:<10} {item['gender']:<10} {item['diagnostic']:<10}")
                    print("="*90)
                    print()
                    listPatientMenu()
                else:
                    print(f'Your Input Is Invalid')
                    print()
        elif inputsort == '6':
            print()
            listPatientMenu()
        else:
            print(f'Button Only Available from 1 to 6')
            print()

            

def listPatientMenu():
    print(f"{'='*10} List of Patient Menus {'='*10}")
    print('''
    1. Show All Patient's Table
    2. Show All Patient's Data Filter
    3. Show All Patient's Data Sort
    4. Search Patient Using Patient's Code
    5. Back to Menus
    ''')
    print('')
    SelectPatientMenu = input("Input Menus Number: ")
    print('')

    if SelectPatientMenu == "1":
        show_all_list_patient()
    elif SelectPatientMenu == "2":
        show_all_Patient_filter()
    elif SelectPatientMenu == "3":
        show_all_Patient_sort()
    elif SelectPatientMenu == "4":
        SearchPatientName()
    elif SelectPatientMenu == "5":
        menu()
    else:
        print('Menu buttons only Available from 1 to 5')
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
        elif any(i.isspace()for i in inputNewpatientCode):
            print("Must Mix Alpha and Number")
            print()
            continue
        elif inputNewpatientCode.isalpha():
            print("Must Mix Alpha and Number")
            print()
            continue
        elif inputNewpatientCode.isnumeric():
            print("Must Mix Alpha and Number")
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
            continue

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
            continue
            
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
        inputNewpatientDiagnostic = input("Enter Patient's Diagnostic Type: ").title()
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
            continue
    
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
            print()
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
                                while True:
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
                                while True:
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
                                while True:
                                    inputConfirm = input('Are You Sure Want To Save? Y/N: ').capitalize()
                                    if inputConfirm == 'Yes' or inputConfirm == 'Y':
                                        filtered[0]["age"] = int(inputNewPatientAge)
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
                                while True:
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
        deleteListmenu()
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
    2. Create New Patient
    3. Modify Patient's Data
    4. Delete Patient's Data
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