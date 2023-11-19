#The purpose of this program is to create a nested dictionary and add, remove, modify elements in it
Patients_records={'Name and Age':{               #Nested Dictionary
    'Femi Ijimayowa':18, 'Frank Peterson':28, 'Jake Blake':21,
    'John Smith':57, 'Robert Downey Jr.':58, 'Elon Musk':52, 
    'Mark Zuckerberg':39, 'Steve Jobs':56, 'Tim Cook':63
}, 'Blood Type':{
    'Femi Ijimayowa':'O-', 'Frank Peterson':'AB+', 'Jake Blake':'O+', 'John Smith':'B', 'Robert Downey Jr.':'AB-',
    'Elon Musk':'O', 'Mark Zuckerberg':'B+', 'Steve Jobs':'A-', 'Tim Cook':'B-'
}, 'Frequency Of Visit':{
    'Femi Ijimayowa':3, 'Frank Peterson':5, 'Jake Blake':7, 'John Smith':1, 'Robert Downey Jr.':9, 'Elon Musk':12,
    'Mark Zuckerberg':10, 'Steve Jobs':2, 'Tim Cook':15
}, 'Patient ID':{
    'Femi Ijimayowa':[117200518], 'Frank Peterson':[102819374], 
    'Jake Blake':[231923937], 'John Smith': [821649264],
    'Robert Downey Jr.':[245682036], 'Elon Musk':[789216703], 
    'Mark Zuckerberg':[320987459], 'Steve Jobs': [617603769], 
    'Tim Cook':[432093769]
}, 'Expected Vist':{
    'Femi Ijimayowa':'March 17, 2030', 'Frank Peterson':'October 20, 1796','Jake Blake':'September 19, 2003',
    'John Smith':'January 1, 2000', 'Robert Downey Jr.':'April 4, 1974', 'Elon Musk':'November 3, 2023',
    'Mark Zuck':'August 24, 2010', 'Steve Jobs':'December 11, 2024', 'TIme Cook':'July 4, 2005'
}}

start_command=input('Do you want to start the program. If not type in quit of q: ')#Start Command use throughout the program 

while start_command!='quit' or start_command!='q': #Ends the program with the user typing in "quit" or "q"
    try:#Try exception 
        if start_command=='add' or start_command=='ads':#Starts if the user types in add or ads
            user_input_name=input('Please name of the Patient\n')
            user_input_age=int(input('Please enter the age of the Patient:\n'))
            user_input_blood_type=input('Please enter the Patients Blood Type:\n')
            user_input_vist_frequency=int(input('Please enter the visit frequency in terms of a number:\n'))
            user_input_ID=int(input('Please enter the Patients ID: \n'))
            user_input_date_of_vist=input('Please enter the date of vist: ')
            def add_patient():#Function to add patient 
                adding_patient_name=user_input_name
                adding_patient_age=user_input_age
                adding_patient_blood_type=user_input_blood_type
                adding_patient_frequency=user_input_vist_frequency
                adding_patient_ID=[user_input_ID]
                adding_patient_visit=user_input_date_of_vist
                Patients_records['Name and Age'][adding_patient_name]=adding_patient_age
                Patients_records['Blood Type']['patient_0']=adding_patient_blood_type
                Patients_records['Frequency Of Visit']['patient_0']=adding_patient_frequency
                Patients_records['Patient ID'][adding_patient_name]=adding_patient_ID
                Patients_records['Expected Vist']['patient_0']=adding_patient_visit
            add_patient()#calling function
            print(Patients_records)
        elif start_command=='remove patient' or start_command=='rp':#Starts if user types in "remove patient" or "rp"
            user_input_to_remove_patient=input('Who\'s record do you want to remove?: ')
            def remove_patient():#Function to remove patient
                if user_input_to_remove_patient in Patients_records['Name and Age']:
                    del Patients_records['Name and Age'][user_input_to_remove_patient]
                    del Patients_records['Blood Type'][user_input_to_remove_patient]
                    del Patients_records['Frequency Of Visit'][user_input_to_remove_patient]
                    del Patients_records['Patient ID'][user_input_to_remove_patient]
                    del Patients_records['Expected Vist'][user_input_to_remove_patient]
                else:
                    print('Patient not in records')
            remove_patient()#Calling Function
            print(Patients_records)
        elif start_command=='print' or start_command=='p':#Starts if the user types in "print" or "p"
            user_input_to_print=input('Please enter the person you want to print records from.\nType in \'all\' to print every record: ')
            def print_patient_records():#Function to to print patient
                if user_input_to_print in Patients_records['Name and Age']:
                    print('Patient Age: ',Patients_records['Name and Age'][user_input_to_print])
                    print('Patient Blood Type: ',Patients_records['Blood Type'][user_input_to_print])
                    print('Patient Frequency Of Vist:',Patients_records['Frequency Of Visit'][user_input_to_print])
                    print('Patient ID:',Patients_records['Patient ID'][user_input_to_print])
                    print('Patient Expected Visit',Patients_records['Expected Vist'][user_input_to_print])
                elif user_input_to_print=='all':#If user types in "all" then program prints everything
                    print(Patients_records['Name and Age'],Patients_records['Blood Type'],Patients_records['Frequency Of Visit'])
                    print(Patients_records['Patient ID'],Patients_records['Expected Vist'])
            print_patient_records()#Calling function
        elif start_command=='update' or start_command=='us':#Program starts if user types in "update" or "us"
            def update_patient_info():#Function to update patient data
                current_patient_name = input('Please enter the current name of the patient: ')
                if current_patient_name in Patients_records['Name and Age']:
                    new_patient_name = input('Please enter the update name: ')
                    update_patient_ID = int(input('Please enter updated ID: '))
                    Patients_records['Name and Age'][new_patient_name] = Patients_records['Name and Age'][current_patient_name]
                    del Patients_records['Name and Age'][current_patient_name]
                    Patients_records['Patient ID'][new_patient_name] = Patients_records['Patient ID'][current_patient_name]
                    del Patients_records['Patient ID'][current_patient_name]
                    Patients_records['Patient ID'][new_patient_name][0] = update_patient_ID
                    print(f'\nPatient information updated for "{current_patient_name}"":')
                    print(f"New Name: {new_patient_name}")
                    print(f"New Patient ID: {update_patient_ID}")
                else:#Else statement incase user error
                    print(f"Patient '{current_patient_name}' not found.")
                    print(Patients_records)
            update_patient_info()#calling function
    except KeyError:#Fist exception
        print('You enter the wrong key please look over what you typed')
    except IndexError:#Second Exception
        print('Your index is either out of range or not neccessary for this program.\nPlease try agin')
    except ZeroDivisionError:#Third Exception
        print('There should\'nt be any math calculations in this program please look over what you typed')
    except ValueError:#Fourth Exception
        print('You either entered the wrond value type or overly typed. Please make sure you didn\'t type in a string instead of a interger')
    except:#Fifth Exception
        print('Please look over what you typed')
