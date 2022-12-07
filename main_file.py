
#import class Patient
import class_patient as p

#run code
def main():

    #run patientsMenu
    patientsMenu()

#patients menu
def patientsMenu():

    #defines patient list
    list_patients = []

    #inputs for the new patient
    def enterPatientInfo():
        item = []
        item.append(input('Enter Patient ID: '))
        item.append(input('Enter Patient name: '))
        item.append(input('Enter Patient diagnosis: '))
        item.append(input('Enter Patient gender: '))
        item.append(input('Enter Patient age: '))
        new_patient_info = (p.Patient(item[0], item[1], item[2], item[3], item[4]))
        return new_patient_info

    #opens and reads the patient.txt file then closes the file
    def readPatientFile():
        file = open('C:/Users/sm161/OneDrive/Desktop/SAIT/sem_1/Obj Ori Pro/project_4/text files/patients.txt', 'r')
        for line in file:
            item = line.rstrip().split('_')
            patient_info = p.Patient(item[0], item[1], item[2], item[3], item[4])
            list_patients.append(patient_info)
        file.close()

    #searches for the patient ID
    def searchPatientByld():
        patient_num = 0
        patient_id = input('\nEnter the Patient ID: ')

        #check if patient id is in patient list
        for obj in list_patients[1:5]:
            patient_num += 1
            if f'{obj.id}' == patient_id:
                patient_info = obj

        # check if patiend id is not in patient list
        id_list = []
        for obj in list_patients[1:5]:
            id_list.append(f'{obj.id}')
        if str(patient_id) not in id_list:
            patient_info = f'Patient with ID {patient_id} is not in patient file.'

        return patient_info, patient_num

    #calls the patient info by ID and updates values
    def editPatientInfo():
        patient_info, patient_num = searchPatientByld()
        print(patient_info)

        item = []
        item.append(f'{patient_info.id}')
        item.append(input('Enter new name: '))
        item.append(input('Enter new diagnosis: '))
        item.append(input('Enter new gender: '))
        item.append(input('Enter new age: '))
        new_patient_info = (p.Patient(item[0], item[1], item[2], item[3], item[4]))

        #updates the patient's info in patient list
        list_patients[patient_num - 2] = new_patient_info

    #reads patients list and prints the contents
    def displayPatientsList():
        print('')
        for obj in list_patients:
            print(obj)

    #writes patient list back to patients.txt
    def writePatientsListToFile():
        file = open('C:/Users/sm161/OneDrive/Desktop/SAIT/sem_1/Obj Ori Pro/project_4/text files/patients.txt', 'w')
        for obj in list_patients:
            var6 = obj.formatPatientInfo()
            file.write(var6 + '\n')
        file.close()

    #calls the input function for the new patient and adds it to patient list
    def addPatientToList():
        list_patients.append(enterPatientInfo())



    #read the patients.txt file
    readPatientFile()

    #run menu inputs
    menu_input = ''
    while menu_input !=0:

        #select which menu option
        menu_input = int(input("\nPatient Menu\n0 - Return to Main Menu\n1 - Display patient's list\n2 - Search for Patient by ID\n3 - Add patient\n4 - Edit patient info\nEnter option: "))

        #writes patient list back to patients.txt and ends program
        if menu_input == 0:
            writePatientsListToFile()

        #displays info of patients
        elif menu_input == 1:
            displayPatientsList()
        
        #searches for patient by patint ID and prints contents
        elif menu_input == 2:
            patient_info, patient_num = searchPatientByld()
            print(patient_info)

        #adds a new patient to patients list
        elif menu_input == 3:
            addPatientToList()

        #edits patient info
        elif menu_input == 4:
            editPatientInfo()
            displayPatientsList()

#run main
if __name__ == '__main__':
    main()

# var1 = 10.5
# print(f'{var1:10n}')

