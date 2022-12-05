
#import class Patient
import class_patient as p



#run code
def main():
    patientsMenu()
    # display_patient_list()

def patientsMenu():
    menu_input = int(input('\nPatient Menu\n0 - Return to Main Menu\n2 - Search for Patient by ID\n3 - Add patient\n4 - Edit patient info\nEnter option: '))

    if menu_input == 0:
        pass

    elif menu_input == 1:
        displayPatientsList()

    elif menu_input == 2:
        pass

    elif menu_input == 3:
        pass

    elif menu_input == 4:
        pass
    


def enterPatientInfo():
    #create new patient obj
    #return object
    pass



def readPatientFile(patient_obj_list):

    #open file
    file = open('C:/Users/sm161/OneDrive/Desktop/SAIT/sem_1/Obj Ori Pro/project_4/text files/patients.txt', 'r')

    #format and create object and object list from patient.txt
    for line in file:
        item = [] #not necessary to define list
        item = line.rstrip().split('_')
        patient_info = p.Patient(item[0], item[1], item[2], item[3], item[4])
        patient_obj_list.append(patient_info)
    file.close()



def searchPatientByld():
    #search for patient by patiend ID through objects list
    pass



def editPatientInfo():
    #call object by patient ID to edit
    #update obj through class attributes
    pass



def displayPatientsList():
    patient_list = []
    readPatientFile(patient_list)
    for obj in patient_list:
        print(f'{obj.id} {obj.name} {obj.diagnosis} {obj.gender} {obj.age}')



def writePatientsListToFile():
    #format text using the class
    #write to file
    pass



def AddPatientToList():
    #call enterPatientInfo
    #add to object list
    pass



#run main
if __name__ == '__main__':
    main()









# var1 = 10.5
# print(f'{var1:10n}')