doctors = []

def add_doctor():

    doctor = {}

    doctor["id"] = input("Enter Doctor ID: ")
    doctor["name"] = input("Enter Doctor Name: ")
    doctor["specialization"] = input("Enter Specialization: ")
    doctor["experience"] = int(input("Enter Experience: "))
    doctor["fees"] = float(input("Enter Consultation Fees: "))

    doctors.append(doctor)

    print("Doctor Added Successfully")


def display_doctors():

    if len(doctors) == 0:
        print("No Doctors Available")
        return

    for d in doctors:
        print("----------------------")
        print("ID :", d["id"])
        print("Name :", d["name"])
        print("Specialization :", d["specialization"])
        print("Experience :", d["experience"])
        print("Fees :", d["fees"])