
import class_patient as p

def display_patient_list():
    #open file
    file = open('C:/Users/sm161/OneDrive/Desktop/SAIT/sem_1/Obj Ori Pro/project_4/text files/patients.txt', 'r')

    #format patients.txt info
    for line in file:
        item = line.rstrip().split('_')
        patient_info = p.Patient(item[0], item[1], item[2], item[3], item[4])
        print(patient_info)

    #close file
    file.close()

display_patient_list()
