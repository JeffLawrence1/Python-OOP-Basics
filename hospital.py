# Assignment: Hospital
# You're going to build a hospital with patients in it! Create a hospital class.

# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?

# Patient:
# Attributes:

#  Id: an id number

#  Name

#  Allergies

#  Bed number: should be none by default
# Hospital
# Attributes:

#  Patients: an empty array

#  Name: hospital name

#  Capacity: an integer indicating the maximum number of patients the hospital can hold.
# Methods:

#  Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.

#  Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.

class Hospital(object):

    def __init__(self, hospitalname, capacity):
        self.hospitalname = hospitalname
        self.capacity = capacity
        self.bed = self.bedcounter()
        self.patients = []

    def bedcounter(self):
        bed = []
        for b in range(0, self.capacity):
            bed.append({"Bed Number": b, "Open": True})
        return bed

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            for b in range(0, len(self.bed)):
                if self.bed[b]["Open"]:
                    patient.bed = self.bed[b]["Bed Number"]
                    self.bed[b]["Open"] = False                    
                    break
            print "Patient {} has been assigned bed {}".format(patient.id, patient.bed)
        else:            
            print "Patient {} the hospital is full gtfo!".format(patient.id)
        return self

    def discharge(self, patient):
        for bed in self.bed:
            if bed["Bed Number"] == patient.bed:
                bed["Open"] = True
                break
        self.patients.remove(patient)
        print "Patient {} discharged, bed {} now available for use".format(patient.id, patient.bed)
        return self

class Patient(object):
    Patients = 1
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.Patients
        self.bed = None
        Patient.Patients += 1

    # def display(self):
    #     print "Patient Name: {}, Allergies: {}, ID: {}, Bed: {}".format(self.name, self.allergies, self.id, self.bed)
    #     return self

hospital1 = Hospital("Swedish", 5)
hospital2 = Hospital("Harborview", 4)
patient1 = Patient("Frank", "none")
patient2 = Patient("Alice", "eggs")
patient3 = Patient("Fred", "peanuts")
patient4 = Patient("Cindy", "none")
patient5 = Patient("Terry", "bees")
patient6 = Patient("Deadydead", "everything")

hospital1.admit(patient1).admit(patient2).admit(patient3).admit(patient4).admit(patient5).admit(patient6).discharge(patient1).discharge(patient2).discharge(patient3).admit(patient1).admit(patient2).admit(patient3).admit(patient1).admit(patient2).admit(patient3)
hospital2.admit(patient1).admit(patient2).admit(patient3).admit(patient4).admit(patient5).admit(patient6)
