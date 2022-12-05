
class Patient:

    #creates object info
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age

    #converts info to string
    def __str__(self):
        return f'{self.id} {self.name} {self.diagnosis} {self.gender} {self.age}'



    #formats text to be writen into patients.txt
    def formatPatientInfo(self):

        pass


