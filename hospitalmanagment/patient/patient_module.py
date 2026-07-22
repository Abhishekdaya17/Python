patients = []

def add_patient():
    patient = {}

    patient["id"] = input("Enter Patient ID: ")
    patient["name"] = input("Enter Patient Name: ")
    patient["age"] = int(input("Enter Age: "))
    patient["gender"] = input("Enter Gender: ")
    patient["disease"] = input("Enter Disease: ")
    patient["mobile"] = input("Enter Mobile Number: ")

    patients.append(patient)

    print("Patient Added Successfully")


def display_patients():

    if len(patients) == 0:
        print("No Patients Found")
        return

    for p in patients:
        print("--------------------------")
        print("ID :", p["id"])
        print("Name :", p["name"])
        print("Age :", p["age"])
        print("Gender :", p["gender"])
        print("Disease :", p["disease"])
        print("Mobile :", p["mobile"])


def search_patient():

    pid = input("Enter Patient ID: ")

    for p in patients:
        if p["id"] == pid:
            print("Patient Found")
            print(p)
            return

    print("Patient Not Found")